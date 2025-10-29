#!/usr/bin/env python3
"""
Quick Publication Adder - Manually add a publication by DOI or URL

Usage:
    python quick_add_publication.py --doi 10.1002/smll.202504877
    python quick_add_publication.py --url https://ieeexplore.ieee.org/document/10967512/
"""

import requests
import yaml
import argparse
import re
from typing import Optional, Dict

def extract_doi_from_url(url: str) -> Optional[str]:
    """Extract DOI from various URL formats"""
    patterns = [
        r'doi.org/(10\.\d+/[^\s]+)',
        r'dx.doi.org/(10\.\d+/[^\s]+)',
        r'/doi/(10\.\d+/[^\s]+)',
        r'sciencedirect.com/science/article/(?:abs/)?pii/([A-Z0-9]+)',
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return None

def fetch_from_crossref(doi: str) -> Optional[Dict]:
    """Fetch publication metadata from CrossRef API"""
    try:
        url = f"https://api.crossref.org/works/{doi}"
        headers = {
            'User-Agent': 'UBC-DAIS-Lab-Website/1.0 (mailto:bhushan.gopaluni@ubc.ca)',
            'Accept': 'application/json'
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json().get('message', {})
    except Exception as e:
        print(f"Error fetching from CrossRef: {e}")
        print(f"Note: Some publishers may require manual entry. You can still create an entry manually.")
        return None

def format_crossref_to_yaml(data: Dict) -> Dict:
    """Format CrossRef data to website YAML format"""

    # Extract authors
    authors_list = data.get('author', [])
    authors = ', '.join([
        f"{a.get('given', '')} {a.get('family', '')}".strip()
        for a in authors_list
    ])

    # Determine type
    pub_type = data.get('type', '')
    is_conference = 'proceedings' in pub_type or 'conference' in data.get('container-title', [''])[0].lower()
    paper_type = 'conference' if is_conference else 'paper'

    # Get journal/venue name
    venue = data.get('container-title', [''])[0] if data.get('container-title') else data.get('publisher', '')

    # Get year
    year = str(data.get('published', {}).get('date-parts', [[None]])[0][0] or
               data.get('issued', {}).get('date-parts', [[None]])[0][0] or
               '')

    # Build entry
    entry = {
        'title': data.get('title', [''])[0],
        'type': paper_type,
        'year': year,
        'authors': authors,
        'journal': venue,
        'url': data.get('URL', ''),
        'description': data.get('abstract', '').replace('<jats:p>', '').replace('</jats:p>', ''),
    }

    return entry

def interactive_edit(entry: Dict) -> Dict:
    """Allow user to edit the generated entry"""
    print("\n" + "="*60)
    print("Generated Publication Entry:")
    print("="*60)
    print(yaml.dump([entry], default_flow_style=False, allow_unicode=True, sort_keys=False))

    print("\nWould you like to edit any fields? (y/n): ", end='')
    if input().lower() == 'y':
        for key in entry.keys():
            if key == 'description':
                print(f"\n{key} (current length: {len(entry[key])} chars)")
                print(f"Keep current? (y/n): ", end='')
                if input().lower() == 'n':
                    print(f"Enter new {key} (or press Enter to skip): ")
                    new_value = input()
                    if new_value:
                        entry[key] = new_value
            else:
                print(f"\n{key}: {entry[key]}")
                print(f"Change? (y/n): ", end='')
                if input().lower() == 'y':
                    new_value = input(f"Enter new {key}: ")
                    if new_value:
                        entry[key] = new_value

    return entry

def main():
    parser = argparse.ArgumentParser(description='Quick add a publication by DOI or URL')
    parser.add_argument('--doi', help='Publication DOI')
    parser.add_argument('--url', help='Publication URL (DOI will be extracted)')
    parser.add_argument('--output', default='_data/publication_to_add.yml',
                       help='Output file')
    parser.add_argument('--no-edit', action='store_true',
                       help='Skip interactive editing')

    args = parser.parse_args()

    # Get DOI
    doi = args.doi
    if args.url and not doi:
        doi = extract_doi_from_url(args.url)
        if not doi:
            print(f"Could not extract DOI from URL: {args.url}")
            print("Please provide DOI directly with --doi")
            return

    if not doi:
        print("Please provide either --doi or --url")
        return

    print(f"Fetching publication data for DOI: {doi}")

    # Fetch from CrossRef
    data = fetch_from_crossref(doi)
    if not data:
        print("Failed to fetch publication data")
        return

    # Format to YAML
    entry = format_crossref_to_yaml(data)

    # Interactive editing
    if not args.no_edit:
        entry = interactive_edit(entry)

    # Write to file
    with open(args.output, 'w') as f:
        yaml.dump([entry], f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"\n✓ Publication saved to: {args.output}")
    print("\nNext steps:")
    print("1. Review the file and add any missing information")
    print("2. Add to _data/publications.yml (at the top for newest first)")
    print("3. Add optional fields: pdf, thumbnail, code, arxiv, etc.")

if __name__ == '__main__':
    main()
