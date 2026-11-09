"""Check every http(s) link in README.md. Needs internet. Exit code 1 if any link is broken."""
import re
import sys
import urllib.error
import urllib.request

urls = sorted(set(re.findall(r"\]\((https://[^)\s]+)\)", open("README.md", encoding="utf-8").read())))
bad = []
for u in urls:
    if "licensebuttons.net" in u:
        continue
    ok = False
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(u, method=method, headers={"User-Agent": "awesome-list-link-check"})
            with urllib.request.urlopen(req, timeout=30) as r:
                ok = r.status < 400
        except urllib.error.HTTPError as e:
            ok = e.code in (401, 403, 429)       # blocked for bots but the page exists
        except (urllib.error.URLError, TimeoutError, OSError):
            ok = False
        if ok:
            break
    print(("ok    " if ok else "BROKEN"), u)
    if not ok:
        bad.append(u)
sys.exit(1 if bad else 0)
