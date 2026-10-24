"""SEO hooks: 为每个页面注入 Open Graph / Twitter Card 元标签。"""
import re
from pathlib import Path


def on_post_build(config, **kwargs):
    site_name = config.get("site_name", "")
    site_desc = config.get("site_description", "")
    base = Path(config["site_dir"])
    n = 0
    for html in base.rglob("index.html"):
        text = html.read_text(encoding="utf-8")
        if "og:title" in text:
            continue
        # 从 <title> 提取页面标题
        m = re.search(r"<title>([^<]*)</title>", text)
        title = m.group(1) if m else site_name
        # 从现有 description meta 提取描述，否则用全局
        m = re.search(r'<meta name="description" content="([^"]*)"', text)
        desc = m.group(1) if m else site_desc
        # 从 canonical link 提取 URL
        m = re.search(r'<link rel="canonical" href="([^"]*)"', text)
        url = m.group(1) if m else config.get("site_url", "")
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
        html.write_text(text, encoding="utf-8")
        n += 1
    print(f"[seo_hooks] injected OG/Twitter tags into {n} pages")
