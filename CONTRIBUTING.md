# Contributing

Thank you for helping. Rules for an entry:

1. The tool must be **free to use** (open source preferred). Mark closed-source tools clearly ("Not open source").
2. One line in this form: `- [Name](https://link) - what it is for, platforms, and **its main limit**.`
3. Link to the **official** page or repository, not a download site or a review.
4. No affiliate links, no tracking links, no "best of" paid tools.
5. Put it in the section that matches what it does; keep sections alphabetical except where order helps a beginner.
6. Do not claim features you have not verified. If unsure, say so.

Run the checks before opening a pull request:

```
python scripts/check_format.py        # entry format, duplicates, local links
python scripts/check_links.py         # needs internet; checks every URL
```
