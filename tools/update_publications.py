#!/usr/bin/env python3
"""
Fetch publications from Google Scholar and generate missing _papers/ entries.

Usage:
    pip install scholarly pyyaml
    python scripts/update_publications.py

The script:
  1. Pulls all publications for the configured Google Scholar profile.
  2. Compares against existing _papers/*.md files (by title similarity).
  3. Writes new .md stubs for any missing publications into _papers/.
  4. Prints a summary so you can review before committing.

Run this locally (Google Scholar is blocked from CI/cloud environments).
"""

import os
import re
import sys
from pathlib import Path
from difflib import SequenceMatcher

try:
    from scholarly import scholarly
except ImportError:
    print("Install scholarly first:  pip install scholarly")
    sys.exit(1)

import yaml

SCHOLAR_ID = "KKmRbGgAAAAJ"
PAPERS_DIR = Path(__file__).resolve().parent.parent / "_papers"

JOURNAL_KEYWORDS = [
    "transactions", "journal", "letters", "magazine",
    "sensors", "energies", "processes", "automatica",
]


def is_journal(venue: str) -> bool:
    v = venue.lower()
    return any(k in v for k in JOURNAL_KEYWORDS)


def load_existing_titles():
    titles = set()
    for f in PAPERS_DIR.glob("*.md"):
        text = f.read_text(encoding="utf-8")
        m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', text, re.MULTILINE)
        if m:
            titles.add(m.group(1).strip().lower())
    return titles


def similar(a: str, b: str) -> float:
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def next_order(year: int) -> int:
    max_order = 0
    for f in PAPERS_DIR.glob("*.md"):
        text = f.read_text(encoding="utf-8")
        m = re.search(r'^order:\s*(\d+)', text, re.MULTILINE)
        if m:
            max_order = max(max_order, int(m.group(1)))
    return max_order + 1


def next_filename(year: int, pub_type: str, first_author_last: str, venue_short: str) -> str:
    prefix = f"{year}J" if pub_type == "paper" else f"{year}C"
    existing = sorted(PAPERS_DIR.glob(f"{prefix}*.md"))
    if existing:
        last = existing[-1].stem
        m = re.match(r'\d{4}[JC](\d+)', last)
        num = int(m.group(1)) + 1 if m else 1
    else:
        num = 1
    slug = re.sub(r'[^a-z0-9]', '_', first_author_last.lower())
    venue_slug = re.sub(r'[^a-z0-9]', '_', venue_short.lower())[:20]
    return f"{prefix}{num:02d}_{slug}_{venue_slug}.md"


def make_frontmatter(pub, order):
    venue = pub.get("bib", {}).get("venue", "") or pub.get("bib", {}).get("journal", "") or ""
    pub_type = "paper" if is_journal(venue) else "conference"
    year = pub.get("bib", {}).get("pub_year", "")
    title = pub.get("bib", {}).get("title", "")
    authors = pub.get("bib", {}).get("author", "")
    url = pub.get("pub_url", "")

    fm = {
        "layout": "publication",
        "title": title,
        "type": pub_type,
        "order": order,
        "year": int(year) if year else 0,
        "authors": authors,
        "journal": venue,
    }
    if url:
        fm["external_url"] = url
    return fm


def main():
    print(f"Fetching Google Scholar profile {SCHOLAR_ID} ...")
    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["publications"])
    pubs = author.get("publications", [])
    print(f"Found {len(pubs)} publications on Scholar.")

    existing = load_existing_titles()
    print(f"Found {len(existing)} existing _papers/ entries.\n")

    order = next_order(0)
    added = 0

    for pub in pubs:
        pub = scholarly.fill(pub)
        bib = pub.get("bib", {})
        title = bib.get("title", "")
        if not title:
            continue

        if any(similar(title, ex) > 0.85 for ex in existing):
            continue

        year = bib.get("pub_year", "")
        if not year:
            continue

        fm = make_frontmatter(pub, order)
        first_author = (bib.get("author", "").split(" and ")[0]).split()[-1] if bib.get("author") else "unknown"
        venue_short = (bib.get("venue", "") or bib.get("journal", ""))[:20]
        fname = next_filename(int(year), fm["type"], first_author, venue_short)
        fpath = PAPERS_DIR / fname

        content = "---\n" + yaml.dump(fm, default_flow_style=False, allow_unicode=True) + "---\n"
        fpath.write_text(content, encoding="utf-8")
        print(f"  + {fname}: {title}")
        order += 1
        added += 1
        existing.add(title.lower())

    print(f"\nDone. Added {added} new publication(s).")
    if added:
        print("Review the new files, then:  git add _papers/ && git commit && git push")


if __name__ == "__main__":
    main()
