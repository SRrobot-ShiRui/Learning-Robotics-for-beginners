"""SEO/GEO hooks: 为每个页面注入 Open Graph / Twitter Card 元标签与 JSON-LD 结构化数据。

v3（2026-11-09，GEO 强化）：
  - OG / Twitter Card（v1 沿用）
  - JSON-LD：全站 WebSite + 文章页 TechArticle（v2 沿用）
  - 新增 v3：
    1) 每篇文章从源 Markdown front matter 读取**独立** description / keywords，
       写进 TechArticle（取代 v2 的全站统一关键词，AI 引擎按主题抓取更精准）
    2) 解析文章里的「常见问题 / 常见误解」区块，生成 **FAQPage** 结构化数据
       —— 结构化问答对是生成式引擎（GEO）检索时最容易直接引用/复述的内容
    3) 文章页加 **BreadcrumbList**：首页 → 机器人炼金术 → 本文，
       让搜索引擎与 AI 明确页面在站点知识树中的位置
    4) TechArticle 补 dateModified / about（主题实体标注）/ isAccessibleForFree
"""
import json
import re
from pathlib import Path

# 文章页发布日期（用于 TechArticle.datePublished）；dateModified 取同日
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
}

# 全站兜底关键词（文章 front matter 未写 keywords 时使用）
DEFAULT_KEYWORDS = (
    "机器人学,机器人炼金术,SE(3),运动学,动力学,RNEA,雅可比,逆运动学,"
    "正运动学,人形机器人,具身智能,世界模型,VLA,sim2real,接触力学,平衡控制"
)

SECTION_NAME = "机器人炼金术"


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
    """从「## 常见问题 / 常见误解」区块解析 **问：...** + 答案段落，返回 [(q, a), ...]。

    只认本专栏约定的写法；答案取到下一个问题或区块结束为止。
    """
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
        a = _clean_md(a)
        a = re.sub(r"^答[：:]\s*", "", a)   # 去掉正文里的「答：」引导词
        if q and a:
            out.append((q, a[:600]))
    return out


def on_post_build(config, **kwargs):
    site_name = config.get("site_name", "")
    site_desc = config.get("site_description", "")
    site_url = config.get("site_url", "").rstrip("/")
    base = Path(config["site_dir"])
    docs_dir = Path(config["docs_dir"])
    n_meta = n_json = n_faq = n_bread = 0

    for html in base.rglob("index.html"):
        text = html.read_text(encoding="utf-8")
        m = re.search(r"<title>([^<]*)</title>", text)
        title = m.group(1) if m else site_name
        m = re.search(r'<meta name="description" content="([^"]*)"', text)
        desc = m.group(1) if m else site_desc
        m = re.search(r'<link rel="canonical" href="([^"]*)"', text)
        url = m.group(1) if m else site_url
        rel = str(html.parent.relative_to(base))

        # 对应源 Markdown（用于 front matter 与 FAQ 解析）
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
            }))

            is_article = rel.startswith("Robot_Alchemy") and rel != "Robot_Alchemy"
            if is_article:
                slug = rel.split("/")[1]
                date = PUBLISH_DATES.get(slug)
                if date:
                    about = [{"@type": "Thing", "name": k.strip()}
                             for k in page_kw.split(",") if k.strip()][:8]
                    blocks.append(_jsonld({
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
                        "isAccessibleForFree": True,
                        "author": {"@type": "Organization",
                                   "name": "SRrobot 视睿机器人",
                                   "url": site_url},
                        "publisher": {"@type": "Organization",
                                      "name": "SRrobot 视睿机器人"},
                        "isPartOf": {"@type": "Blog",
                                     "name": SECTION_NAME,
                                     "url": f"{site_url}/Robot_Alchemy/"},
                    }))

                # BreadcrumbList：首页 → 栏目 → 本文
                blocks.append(_jsonld({
                    "@context": "https://schema.org",
                    "@type": "BreadcrumbList",
                    "itemListElement": [
                        {"@type": "ListItem", "position": 1,
                         "name": "首页", "item": site_url + "/"},
                        {"@type": "ListItem", "position": 2,
                         "name": SECTION_NAME,
                         "item": f"{site_url}/Robot_Alchemy/"},
                        {"@type": "ListItem", "position": 3,
                         "name": title, "item": url},
                    ],
                }))
                n_bread += 1

                # FAQPage：从源 Markdown 的「常见问题」区块解析问答对
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

            if blocks:
                text = text.replace("</head>", "\n".join(blocks) + "\n</head>", 1)
                n_json += 1

        html.write_text(text, encoding="utf-8")
    print(f"[seo_hooks v3] OG/Twitter -> {n_meta} pages, JSON-LD -> {n_json} pages, "
          f"Breadcrumb -> {n_bread} pages, FAQPage -> {n_faq} pages")
