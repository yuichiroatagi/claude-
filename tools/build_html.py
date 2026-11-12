"""notes/*.md を 1 枚の HTML（Artifact 用）に変換する。
GitHub の `> [!CAUTION]` ブロックを Claude 提案として赤字で表示する。
使い方: python3 tools/build_html.py <出力パス>
"""
import re, sys, pathlib, html, datetime
import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
notes = sorted((ROOT / "notes").glob("*.md"))

def convert_alerts(text):
    out, lines, i = [], text.split("\n"), 0
    while i < len(lines):
        if lines[i].strip() == "> [!CAUTION]":
            i += 1
            block = []
            while i < len(lines) and lines[i].startswith(">"):
                block.append(lines[i][1:].lstrip(" ") if lines[i] != ">" else "")
                i += 1
            out += ['<div class="prop" markdown="1">', "", *block, "", "</div>"]
        else:
            out.append(lines[i]); i += 1
    return "\n".join(out)

LIST = re.compile(r"^\s*([-*]|\d+\.) ")

def fix_lists(text):
    # python-markdown は段落直後のリストを認識しないため空行を補う。入れ子は 4 スペースに揃える
    out = []
    for line in text.split("\n"):
        m = re.match(r"^( +)([-*]|\d+\.) ", line)
        if m:
            line = " " * (len(m.group(1)) // 2 * 4) + line.lstrip(" ")
        if LIST.match(line) and out and out[-1].strip() and not LIST.match(out[-1]) and not out[-1].startswith(" "):
            out.append("")
        out.append(line)
    return "\n".join(out)

sections, nav = [], []
for p in notes:
    src = p.read_text(encoding="utf-8")
    title = re.search(r"^# (.+)$", src, re.M).group(1).replace(" 治療方針ノート", "")
    slug = re.sub(r"^\d+_", "", p.stem).replace("_", "-")
    body = markdown.markdown(fix_lists(convert_alerts(src)), extensions=["tables", "md_in_html", "sane_lists"])
    body = body.replace("<a href=\"http", "<a target=\"_blank\" rel=\"noopener\" href=\"http")
    body = body.replace("<table>", "<div class=\"tw\"><table>").replace("</table>", "</table></div>")
    nav.append(f'<a href="#{slug}">{html.escape(title)}</a>')
    sections.append(f'<section id="{slug}">{body}</section>')

today = datetime.date.today().isoformat()
page = f"""<title>泌尿器科 治療方針ノート</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>
/* layout: 単一カラムの読み物。上部に疾患ナビ、本文 70ch。提案は赤 */
:root{{--bg:#fbfbfa;--fg:#1d2330;--muted:#5f6878;--line:#dde1e7;--accent:#24508f;--prop:#c0262d;--propbg:#fdf1f1;--thbg:#f0f2f5;
--body:"Noto Sans JP",system-ui,-apple-system,"Hiragino Sans",sans-serif;--head:"Noto Sans JP",system-ui,sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#14171d;--fg:#e6e9ee;--muted:#9aa3b2;--line:#2c323d;--accent:#8db4f0;--prop:#ff7b7b;--propbg:#2a1719;--thbg:#1d2129;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#14171d;--fg:#e6e9ee;--muted:#9aa3b2;--line:#2c323d;--accent:#8db4f0;--prop:#ff7b7b;--propbg:#2a1719;--thbg:#1d2129;color-scheme:dark}}
*{{box-sizing:border-box}}
body{{background:var(--bg);color:var(--fg);font:15px/1.75 var(--body);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:0 48px}}
.wrap{{max-width:46rem;margin:0 auto}}
header{{padding-block:24px 8px}} header h1{{font:700 1.35rem/1.3 var(--head);margin:0}} header p{{color:var(--muted);margin:4px 0 0;font-size:.85rem}}
nav{{position:sticky;top:env(safe-area-inset-top,0px);background:var(--bg);display:flex;gap:6px;flex-wrap:wrap;padding-block:10px;border-bottom:1px solid var(--line);z-index:5}}
nav a{{font-size:.85rem;padding:4px 10px;border:1px solid var(--line);border-radius:999px;color:var(--fg);text-decoration:none}}
nav a:hover,nav a:focus-visible{{border-color:var(--accent);color:var(--accent);outline:none}}
section{{padding-top:24px;border-bottom:1px solid var(--line);padding-bottom:24px;scroll-margin-top:64px}}
h1{{font:700 1.3rem/1.35 var(--head);text-wrap:balance}} h2{{font:700 1.08rem/1.4 var(--head);margin-top:2em;padding-top:.6em;border-top:1px solid var(--line);text-wrap:balance}}
hr{{display:none}} a{{color:var(--accent)}} ul{{padding-left:1.3em}} li{{margin:.15em 0}}
strong{{font-weight:700}}
.tw{{overflow-x:auto;margin:1em 0}} table{{border-collapse:collapse;font-size:.88rem;min-width:100%}} th,td{{border:1px solid var(--line);padding:6px 9px;text-align:left;vertical-align:top}} th{{background:var(--thbg)}}
.prop{{color:var(--prop);background:var(--propbg);border-left:3px solid var(--prop);padding:.6em 1em;margin:1em 0;border-radius:0 6px 6px 0}}
.prop a{{color:var(--prop);text-decoration:underline}} .prop strong{{color:var(--prop)}}
code{{font-size:.85em;background:var(--thbg);padding:1px 5px;border-radius:4px}}
</style>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&display=swap">
<div class="wrap">
<header><h1>泌尿器科 治療方針ノート</h1><p>黒字＝自分の方針／<span style="color:var(--prop)">赤字＝Claude 提案（リンク付き）</span>　生成日 {today}</p></header>
<nav>{''.join(nav)}</nav>
{''.join(sections)}
</div>
"""
out = pathlib.Path(sys.argv[1]); out.write_text(page, encoding="utf-8"); print(out)
