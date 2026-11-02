"""SEO/GEO hooks: 为每个页面注入 Open Graph / Twitter Card 元标签与 JSON-LD 结构化数据。

v2（2026-11-02）：
  - OG / Twitter Card（原有）
  - 新增 JSON-LD：全站 WebSite + WebPage；Robot_Alchemy 文章页用 TechArticle
    （headline / description / datePublished / author / inLanguage / keywords）
    —— 结构化数据是 Google 富结果与生成式引擎（GEO）引用抓取的主要依据。
"""
import json
import re
from pathlib import Path

# 文章页发布日期（用于 TechArticle.datePublished）
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
}

KEYWORDS = "机器人学,机器人炼金术,正运动学,逆运动学,雅可比,SE(3),人形机器人,具身智能,VLA,运动学,阻尼最小二乘,sim2real"


def _jsonld(obj: dict) -> str:
    return "<script type=\"application/ld+json\">" + json.dumps(
        obj, ensure_ascii=False, separators=(",", ":")) + "</script>"


def on_post_build(config, **kwargs):
    site_name = config.get("site_name", "")
    site_desc = config.get("site_description", "")
    site_url = config.get("site_url", "").rstrip("/")
    base = Path(config["site_dir"])
    n_meta = n_json = 0
    for html in base.rglob("index.html"):
        text = html.read_text(encoding="utf-8")
        # 从 <title> 提取页面标题
        m = re.search(r"<title>([^<]*)</title>", text)
        title = m.group(1) if m else site_name
        # 从现有 description meta 提取描述，否则用全局
        m = re.search(r'<meta name="description" content="([^"]*)"', text)
        desc = m.group(1) if m else site_desc
        # 从 canonical link 提取 URL
        m = re.search(r'<link rel="canonical" href="([^"]*)"', text)
        url = m.group(1) if m else site_url
        rel = str(html.parent.relative_to(base))

        # ---- 1. OG / Twitter Card ----
        if "og:title" not in text:
            tags = (
                f'<meta property="og:type" content="website">\n'
                f'<meta property="og:site_name" content="{site_name}">\n'
                f'<meta property="og:title" content="{title}">\n'
                f'<meta property="og:description" content="{desc}">\n'
                f'<meta property="og:url" content="{url}">\n'
                f'<meta name="twitter:card" content="summary">\n'
                f'<meta name="twitter:title" content="{title}">\n'
                f'<meta name="twitter:description" content="{desc}">\n'
            )
            text = text.replace("<head>", "<head>\n" + tags, 1)
            n_meta += 1

        # ---- 2. JSON-LD 结构化数据 ----
        if "application/ld+json" not in text:
            blocks = []
            # 全站 WebSite（sitelinks 搜索框依据）
            blocks.append(_jsonld({
                "@context": "https://schema.org",
                "@type": "WebSite",
                "name": site_name,
                "url": site_url or url,
                "description": site_desc,
                "inLanguage": "zh-CN",
            }))
            # Robot_Alchemy 文章页 → TechArticle
            if rel.startswith("Robot_Alchemy") and rel != "Robot_Alchemy":
                slug = rel.split("/")[1]
                date = PUBLISH_DATES.get(slug)
                if date:
                    blocks.append(_jsonld({
                        "@context": "https://schema.org",
                        "@type": "TechArticle",
                        "headline": title,
                        "description": desc,
                        "url": url,
                        "datePublished": date,
                        "inLanguage": "zh-CN",
                        "keywords": KEYWORDS,
                        "author": {"@type": "Organization",
                                   "name": "SRrobot 视睿机器人",
                                   "url": site_url},
                        "publisher": {"@type": "Organization",
                                      "name": "SRrobot 视睿机器人"},
                        "isPartOf": {"@type": "Blog",
                                     "name": "机器人炼金术",
                                     "url": f"{site_url}/Robot_Alchemy/"},
                    }))
            if blocks:
                text = text.replace("</head>", "\n".join(blocks) + "\n</head>", 1)
                n_json += 1

        html.write_text(text, encoding="utf-8")
    print(f"[seo_hooks] OG/Twitter -> {n_meta} pages, JSON-LD -> {n_json} pages")
