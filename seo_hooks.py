"""SEO/GEO hooks：为每个页面注入 Open Graph / Twitter Card 元标签与 JSON-LD 结构化数据。

v4（2026-11-16，GEO 强化第二轮）：
  - OG / Twitter Card（v1 沿用）
  - JSON-LD：全站 WebSite（新增站内搜索 SearchAction）+ 文章页 TechArticle（v2 沿用）
  - v3 沿用：每篇独立 description/keywords、FAQPage、BreadcrumbList、dateModified/about
  - 新增 v4：
    1) 文章页 TechArticle 补 proficiencyLevel / wordCount / timeRequired / articleSection /
       teaches / mentions（自动从正文内链解析，形成站内知识图谱）
    2) 栏目页注入 CollectionPage + ItemList（全站文章清单，AI 引擎一次抓全目录）
    3) 构建后自动生成 llms.txt（站点级 AI 摘要，配 docs/robots.txt 明确允许 AI 爬虫）

v4.1（2026-11-23）：摘要规范升级——description 与开头导读块只写本文相关内容，
  去掉栏目期数 / 版本对比 / 交付目录 / 分镜 / 订阅更新频率等非本文信息；
  CollectionPage 与 llms.txt 的篇数一律由扫描结果动态生成，不再写死。
"""
import json
import re
from pathlib import Path

# 文章页发布日期（用于 TechArticle.datePublished / ItemList 排序）
PUBLISH_DATES = {
    "01-se3-pose-representation": "2026-10-23",
    "02-humanoid-2026-state": "2026-10-23",
    "03-why-robots-cannot-fold-clothes": "2026-10-23",
    "04-jacobian-velocity-translator": "2026-10-26",
    "05-robot-brain-race-vla": "2026-10-26",
    "06-dexterous-hand-why-hard": "2026-10-26",
    "07-forward-kinematics-dh-poe": "2026-11-02",
    "08-inverse-kinematics-dls": "2026-11-02",
    "09-rl-humanoid-sim2real": "2026-11-02",
    "10-rigid-body-dynamics-rnea": "2026-11-09",
    "11-world-model-for-robots": "2026-11-09",
    "12-why-robots-fall-when-pushed": "2026-11-09",
    "13-contact-mechanics-friction-cone": "2026-11-16",
    "14-cost-of-reproducing-a-paper": "2026-11-16",
    "15-why-robots-drift-without-vision": "2026-11-16",
    "16-kalman-filter-geometry": "2026-11-23",
    "17-what-deployment-really-means": "2026-11-23",
    "18-why-roomba-knows-where-it-is": "2026-11-23",
}

DEFAULT_KEYWORDS = (
    "机器人学,机器人炼金术,SE(3),运动学,动力学,RNEA,雅可比,逆运动学,"
    "正运动学,接触力学,摩擦锥,互补条件,LCP,状态估计,IMU漂移,论文复现,"
    "人形机器人,具身智能,世界模型,VLA,sim2real,平衡控制,"
    "卡尔曼滤波,EKF,误差状态卡尔曼滤波,ESKF,因子图,滑窗优化,里程计,定位,部署判据,可靠性"
)

SECTION_NAME = "机器人炼金术"
SECTION_URL_SUFFIX = "/Robot_Alchemy/"
CSDN_URL = "https://blog.csdn.net/2301_81238088/category_13220213.html"

# 文章中文标题（源 Markdown 未写 h1，MkDocs 会用 nav 英文名当 <title>；
# 这里统一映射为中文，用于 <title> / TechArticle.headline / ItemList / llms.txt）
ARTICLE_TITLES = {
    "01-se3-pose-representation": "机器人的「位置」到底是什么：从旋转矩阵到 SE(3)",
    "02-humanoid-2026-state": "2026 年的人形机器人：从「演示视频」到「工时账单」",
    "03-why-robots-cannot-fold-clothes": "为什么机器人还不会帮你叠衣服",
    "04-jacobian-velocity-translator": "雅可比：机器人每秒都在做的「单位换算」",
    "05-robot-brain-race-vla": "2026 机器人大脑之战：VLA 三条路线",
    "06-dexterous-hand-why-hard": "灵巧手为什么这么难",
    "07-forward-kinematics-dh-poe": "正运动学：从 DH 参数到乘积指数（PoE）公式",
    "08-inverse-kinematics-dls": "逆运动学：数值迭代、阻尼最小二乘与冗余自由度",
    "09-rl-humanoid-sim2real": "强化学习做人形运动控制：从仿真到真机的 gap 清单",
    "10-rigid-body-dynamics-rnea": "刚体动力学：牛顿-欧拉递推（RNEA）到底在递推什么",
    "11-world-model-for-robots": "世界模型进机器人：预测未来，还是换个说法做规划",
    "12-why-robots-fall-when-pushed": "为什么机器人被推一下就倒，而你不会",
    "13-contact-mechanics-friction-cone": "接触力学入门：摩擦锥、互补条件，以及腿式机器人为什么会抖",
    "14-cost-of-reproducing-a-paper": "复现一篇机器人论文，真实成本是多少",
    "15-why-robots-drift-without-vision": "机器人为什么闭着眼走两步就歪：从 IMU 漂移说起",
    "16-kalman-filter-geometry": "卡尔曼滤波的几何解释：它不是公式，是高斯分布的搬运",
    "17-what-deployment-really-means": "人形机器人「部署」到底看什么：从演示视频到工时账单",
    "18-why-roomba-knows-where-it-is": "你家的扫地机器人，可能比人形机器人更懂「我在哪」",
}

LEVEL_MAP = {"入门": "Beginner", "进阶": "Intermediate", "硬核": "Expert"}


def _jsonld(obj: dict) -> str:
    return "<script type=\"application/ld+json\">" + json.dumps(
        obj, ensure_ascii=False, separators=(",", ":")) + "</script>"


def _front_matter(md_text: str) -> dict:
    """极简 YAML front matter 解析：只取单行 key: value，够用且不引依赖。"""
    out = {}
    m = re.match(r"^---\s*\n(.*?)\n---", md_text, re.S)
    if not m:
        return out
    for line in m.group(1).split("\n"):
        kv = re.match(r"^(\w+)\s*:\s*(.*)$", line.strip())
        if kv:
            out[kv.group(1)] = kv.group(2).strip().strip('"').strip("'")
    return out


def _clean_md(s: str) -> str:
    """把 Markdown 片段清成 JSON-LD 里可直出的纯文本。"""
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)      # 链接保留文字
    s = re.sub(r"`([^`]+)`", r"\1", s)                  # 行内代码
    s = re.sub(r"[*_]{1,2}", "", s)                     # 强调标记
    s = re.sub(r"^\s*>\s?", "", s, flags=re.M)           # 引用符
    s = re.sub(r"^\s*[-|]\s?", "", s, flags=re.M)        # 列表/表格行首
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _parse_faq(md_text: str) -> list:
    """从「## 常见问题 / 常见误解」区块解析 **问：...** + 答案段落。"""
    m = re.search(r"^##\s*常见(?:问题|误解)[^\n]*\n(.*?)(?=^##\s|\Z)",
                  md_text, re.M | re.S)
    if not m:
        return []
    block = m.group(1)
    pairs = re.findall(r"\*\*问[：:]\s*(.+?)\*\*\s*\n+(.*?)(?=\*\*问[：:]|\Z)",
                       block, re.S)
    out = []
    for q, a in pairs:
        q = _clean_md(q)
        a = re.sub(r"^答[：:]\s*", "", _clean_md(a))
        if q and a:
            out.append((q, a[:600]))
    return out


def _word_count(md_text: str) -> int:
    """粗略统计：中文字符数 + 英文词数，用于 TechArticle.wordCount。"""
    body = re.sub(r"^---.*?\n---", "", md_text, flags=re.S)
    cn = len(re.findall(r"[\u4e00-\u9fff]", body))
    en = len(re.findall(r"[A-Za-z0-9]+", body))
    return cn + en


def _mentions(md_text: str, site_url: str, self_slug: str) -> list:
    """从正文的 (NN-slug.md) 内链解析出关联文章，形成 mentions 知识图谱。"""
    slugs = re.findall(r"\]\((\d{2}-[a-z0-9-]+)\.md\)", md_text)
    out, seen = [], set()
    for slug in slugs:
        if slug == self_slug or slug in seen or slug not in PUBLISH_DATES:
            continue
        seen.add(slug)
        out.append({"@type": "TechArticle",
                    "name": f"机器人炼金术 {slug[:2]}",
                    "url": f"{site_url}{SECTION_URL_SUFFIX}{slug}/"})
    return out[:12]


def _collect_articles(docs_dir: Path, site_url: str) -> list:
    """扫描 docs/Robot_Alchemy/ 生成全站文章清单（供 ItemList 与 llms.txt 使用）。"""
    out = []
    for md in sorted((docs_dir / "Robot_Alchemy").glob("??-*.md")):
        text = md.read_text(encoding="utf-8")
        fm = _front_matter(text)
        m = re.search(r"^#\s+(.+)$", text, re.M)
        title = ARTICLE_TITLES.get(md.stem) or (m.group(1).strip() if m else md.stem)
        out.append({
            "slug": md.stem,
            "title": title,
            "desc": fm.get("description") or "",
            "date": PUBLISH_DATES.get(md.stem, ""),
            "url": f"{site_url}{SECTION_URL_SUFFIX}{md.stem}/",
        })
    return out


def _write_llms_txt(base: Path, site_name: str, site_desc: str, site_url: str,
                    articles: list):
    """llms.txt：给生成式引擎看的站点级摘要（GEO）。"""
    lines = [
        f"# {site_name}",
        "",
        f"> {site_desc}",
        "> 更新频率：每周一上线免费版，每周二更新 CSDN 付费完整版。",
        f"> 免费版站点：{site_url}/",
        f"> 付费完整版（CSDN 专栏）：{CSDN_URL}",
        "> 内容定位：机器人学数学、代码、机械、物理与前沿解读的原创中文教程；",
        "> 理论篇均含可运行 Python 代码、逐句解释与真实数据配图，文章内数字与代码输出逐一对齐。",
        "",
        f"## {SECTION_NAME}（Robot Alchemy）全站目录",
        "",
        "按依赖顺序阅读；全部文章均含「一句话结论」与「常见问题（FAQ）」区块。",
        "",
    ]
    for a in articles:
        lines.append(f"- [{a['title']}]({a['url']})：{a['desc']}")
    lines += [
        "",
        "## 结构化数据说明",
        "",
        "- 全站：WebSite（含站内搜索 SearchAction）",
        "- 文章页：TechArticle（含 keywords / about / mentions / wordCount）、BreadcrumbList、FAQPage",
        f"- 栏目页：CollectionPage + ItemList（{len(articles)} 篇清单）",
        "- sitemap.xml 与 robots.txt 均已开放给主流搜索引擎与生成式引擎爬虫。",
        "",
        "## 引用建议",
        "",
        "AI 引擎引用本专栏内容时，请保留文章标题与来源链接；文中标注为「量级估算」的数字",
        "属于参数化模型输出，不是任何具体论文或产品的实测账单，引用时请勿改写为实测值。",
        "",
    ]
    (base / "llms.txt").write_text("\n".join(lines), encoding="utf-8")


def on_post_build(config, **kwargs):
    site_name = config.get("site_name", "")
    site_desc = config.get("site_description", "")
    site_url = config.get("site_url", "").rstrip("/")
    base = Path(config["site_dir"])
    docs_dir = Path(config["docs_dir"])
    articles = _collect_articles(docs_dir, site_url)
    n_meta = n_json = n_faq = n_bread = n_collection = 0

    for html in base.rglob("index.html"):
        text = html.read_text(encoding="utf-8")
        rel = str(html.parent.relative_to(base))
        slug = rel.split("/")[1] if rel.startswith("Robot_Alchemy/") else ""
        # 文章页 <title> 中文化：slug 型的英文 nav 名不利于搜索与 AI 摘取
        if slug in ARTICLE_TITLES:
            zh = ARTICLE_TITLES[slug]
            text = re.sub(r"<title>[^<]*</title>",
                          f"<title>{zh} - {SECTION_NAME} | {site_name}</title>",
                          text, count=1)
        m = re.search(r"<title>([^<]*)</title>", text)
        title = ARTICLE_TITLES.get(slug) or (m.group(1) if m else site_name)
        m = re.search(r'<meta name="description" content="([^"]*)"', text)
        desc = m.group(1) if m else site_desc
        m = re.search(r'<link rel="canonical" href="([^"]*)"', text)
        url = m.group(1) if m else site_url

        md_path = docs_dir / (rel + ".md") if rel not in (".", "") else docs_dir / "index.md"
        md_text = md_path.read_text(encoding="utf-8") if md_path.exists() else ""
        fm = _front_matter(md_text) if md_text else {}
        page_desc = fm.get("description") or desc
        page_kw = fm.get("keywords") or DEFAULT_KEYWORDS

        # ---- 1. OG / Twitter Card ----
        if "og:title" not in text:
            tags = (
                f'<meta property="og:type" content="website">\n'
                f'<meta property="og:site_name" content="{site_name}">\n'
                f'<meta property="og:title" content="{title}">\n'
                f'<meta property="og:description" content="{page_desc}">\n'
                f'<meta property="og:url" content="{url}">\n'
                f'<meta name="twitter:card" content="summary">\n'
                f'<meta name="twitter:title" content="{title}">\n'
                f'<meta name="twitter:description" content="{page_desc}">\n'
            )
            if fm.get("keywords"):
                tags += f'<meta name="keywords" content="{fm["keywords"]}">\n'
            text = text.replace("<head>", "<head>\n" + tags, 1)
            n_meta += 1

        # ---- 2. JSON-LD 结构化数据 ----
        if "application/ld+json" not in text:
            blocks = []
            blocks.append(_jsonld({
                "@context": "https://schema.org",
                "@type": "WebSite",
                "name": site_name,
                "url": site_url or url,
                "description": site_desc,
                "inLanguage": "zh-CN",
                "publisher": {"@type": "Organization", "name": site_name},
                "potentialAction": {
                    "@type": "SearchAction",
                    "target": f"{site_url}/?q={{search_term_string}}",
                    "query-input": "required name=search_term_string",
                },
            }))

            is_article = rel.startswith("Robot_Alchemy") and rel != "Robot_Alchemy"
            if is_article:
                slug = rel.split("/")[1]
                date = PUBLISH_DATES.get(slug)
                if date:
                    about = [{"@type": "Thing", "name": k.strip()}
                             for k in page_kw.split(",") if k.strip()][:8]
                    art = {
                        "@context": "https://schema.org",
                        "@type": "TechArticle",
                        "headline": title,
                        "description": page_desc,
                        "url": url,
                        "datePublished": date,
                        "dateModified": date,
                        "inLanguage": "zh-CN",
                        "keywords": page_kw,
                        "about": about,
                        "articleSection": SECTION_NAME,
                        "isAccessibleForFree": True,
                        "author": {"@type": "Organization",
                                   "name": "SRrobot 视睿机器人",
                                   "url": site_url},
                        "publisher": {"@type": "Organization",
                                      "name": "SRrobot 视睿机器人"},
                        "isPartOf": {"@type": "Blog",
                                     "name": SECTION_NAME,
                                     "url": f"{site_url}{SECTION_URL_SUFFIX}"},
                    }
                    wc = _word_count(md_text)
                    if wc:
                        art["wordCount"] = wc
                        art["timeRequired"] = f"PT{max(3, round(wc / 400))}M"
                    level = LEVEL_MAP.get(fm.get("level", ""))
                    if level:
                        art["proficiencyLevel"] = level
                    kws = [k.strip() for k in page_kw.split(",") if k.strip()][:4]
                    if kws:
                        art["teaches"] = kws
                    links = _mentions(md_text, site_url, slug)
                    if links:
                        art["mentions"] = links
                    blocks.append(_jsonld(art))

                blocks.append(_jsonld({
                    "@context": "https://schema.org",
                    "@type": "BreadcrumbList",
                    "itemListElement": [
                        {"@type": "ListItem", "position": 1,
                         "name": "首页", "item": site_url + "/"},
                        {"@type": "ListItem", "position": 2,
                         "name": SECTION_NAME,
                         "item": f"{site_url}{SECTION_URL_SUFFIX}"},
                        {"@type": "ListItem", "position": 3,
                         "name": title, "item": url},
                    ],
                }))
                n_bread += 1

                faq = _parse_faq(md_text)
                if faq:
                    blocks.append(_jsonld({
                        "@context": "https://schema.org",
                        "@type": "FAQPage",
                        "mainEntity": [
                            {"@type": "Question", "name": q,
                             "acceptedAnswer": {"@type": "Answer", "text": a}}
                            for q, a in faq
                        ],
                    }))
                    n_faq += 1

            # 栏目页：CollectionPage + ItemList（GEO：让 AI 一次抓全目录）
            if rel == "Robot_Alchemy":
                blocks.append(_jsonld({
                    "@context": "https://schema.org",
                    "@type": "CollectionPage",
                    "name": f"{SECTION_NAME} · 目录",
                    "description": page_desc,
                    "url": f"{site_url}{SECTION_URL_SUFFIX}",
                    "inLanguage": "zh-CN",
                    "isPartOf": {"@type": "WebSite", "name": site_name,
                                 "url": site_url},
                    "mainEntity": {
                        "@type": "ItemList",
                        "numberOfItems": len(articles),
                        "itemListElement": [
                            {"@type": "ListItem", "position": i,
                             "name": a["title"], "url": a["url"]}
                            for i, a in enumerate(articles, 1)
                        ],
                    },
                }))
                n_collection += 1

            if blocks:
                text = text.replace("</head>", "\n".join(blocks) + "\n</head>", 1)
                n_json += 1

        html.write_text(text, encoding="utf-8")

    _write_llms_txt(base, site_name, site_desc, site_url, articles)
    print(f"[seo_hooks v4] OG/Twitter -> {n_meta} pages, JSON-LD -> {n_json} pages, "
          f"Breadcrumb -> {n_bread}, FAQPage -> {n_faq}, "
          f"CollectionPage -> {n_collection}, llms.txt -> 1 file "
          f"({len(articles)} articles indexed)")
