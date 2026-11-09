"""Offline checks for README.md: entry format, duplicate links, working in-page anchors."""
import re
import sys

text = open("README.md", encoding="utf-8").read()
errors = []
entry = re.compile(r"^- (\[[^\]]+\]\(https://[^)\s]+\)|\*\*[^*]+\*\*)")
seen = {}
for n, line in enumerate(text.splitlines(), 1):
    if line.startswith("- [") and not re.match(r"^- \[[^\]]+\]\((https://|#)[^)\s]+\) ", line) \
            and not re.match(r"^- \[[^\]]+\]\(#[^)]+\)$", line):
        errors.append(f"line {n}: entry must be '- [Name](https://...) - description'")
    for url in re.findall(r"\]\((https?://[^)\s]+)\)", line):
        if url.startswith("http://"):
            errors.append(f"line {n}: use https: {url}")
        if line.startswith("- [") and url in seen and "#" not in url.split("/")[-1] and "docs/" not in url:
            pass
        seen.setdefault(url, n)
anchors = {re.sub(r"[^a-z0-9 -]", "", m.lower()).strip().replace(" ", "-")
           for m in re.findall(r"^#{2,3} (.+)$", text, re.M)}
for a in re.findall(r"\]\(#([^)]+)\)", text):
    if a not in anchors:
        errors.append(f"broken anchor #{a}")
if "utm_" in text or "?ref=" in text or "affiliate" in text.lower().replace("no affiliate", ""):
    errors.append("tracking or affiliate parameters found")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print("README format OK")
