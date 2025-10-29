#!/usr/bin/env python3
"""
Automated Publications Updater for UBC DAIS Lab Website

This script fetches publications from Semantic Scholar API and formats them
into the YAML structure used by the website.

Usage:
    python update_publications.py --year 2025 --author-id <semantic-scholar-id>
"""

import requests
import yaml
import argparse
from datetime import datetime
from typing import List, Dict, Optional
import time

class PublicationFetcher:
    """Fetches publications from various academic APIs"""

    def __init__(self):
        self.semantic_scholar_base = "https://api.semanticscholar.org/graph/v1"
        self.crossref_base = "https://api.crossref.org/works"

    def fetch_from_semantic_scholar(self, author_id: str, year: int) -> List[Dict]:
        """
        Fetch publications from Semantic Scholar API

        Args:
            author_id: Semantic Scholar author ID
            year: Year to filter publications

        Returns:
            List of publications
        """
        publications = []

        # Fetch author's papers
        url = f"{self.semantic_scholar_base}/author/{author_id}/papers"
        params = {
            'fields': 'title,authors,year,venue,publicationDate,externalIds,abstract,url,publicationTypes',
            'limit': 100
        }

        try:
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            for paper in data.get('data', []):
                if paper.get('year') == year:
                    publications.append(paper)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching from Semantic Scholar: {e}")

        return publications

    def fetch_by_doi(self, doi: str) -> Optional[Dict]:
        """
        Fetch publication details by DOI using CrossRef

        Args:
            doi: Digital Object Identifier

        Returns:
            Publication details or None
        """
        try:
            url = f"{self.crossref_base}/{doi}"
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return response.json().get('message', {})
        except requests.exceptions.RequestException as e:
            print(f"Error fetching DOI {doi}: {e}")
            return None

class PublicationFormatter:
    """Formats publications into website YAML format"""

    @staticmethod
    def determine_type(paper: Dict) -> str:
        """
        Determine if paper is conference or journal

        Args:
            paper: Publication data from Semantic Scholar

        Returns:
            'conference' or 'paper'
        """
        pub_types = paper.get('publicationTypes', [])
        venue = paper.get('venue', '').lower()

        # Check for conference indicators
        if 'Conference' in pub_types:
            return 'conference'

        # Check venue name for conference keywords
        conference_keywords = ['conference', 'proceedings', 'workshop', 'symposium', 'icml', 'neurips', 'cvpr', 'iccv']
        if any(keyword in venue for keyword in conference_keywords):
            return 'conference'

        return 'paper'

    @staticmethod
    def format_authors(authors: List[Dict]) -> str:
        """
        Format author list as comma-separated string

        Args:
            authors: List of author dictionaries

        Returns:
            Formatted author string
        """
        author_names = [author.get('name', '') for author in authors if author.get('name')]
        return ', '.join(author_names)

    @staticmethod
    def extract_urls(paper: Dict) -> Dict[str, str]:
        """
        Extract various URLs from paper data

        Args:
            paper: Publication data

        Returns:
            Dictionary of URL types to URLs
        """
        urls = {}
        external_ids = paper.get('externalIds', {})

        # DOI URL
        if external_ids.get('DOI'):
            urls['doi'] = f"https://doi.org/{external_ids['DOI']}"

        # ArXiv URL
        if external_ids.get('ArXiv'):
            urls['arxiv'] = f"https://arxiv.org/abs/{external_ids['ArXiv']}"

        # Paper URL
        if paper.get('url'):
            urls['url'] = paper['url']

        return urls

    def format_to_yaml(self, paper: Dict) -> Dict:
        """
        Format a paper into the website's YAML structure

        Args:
            paper: Publication data from Semantic Scholar

        Returns:
            Dictionary in website YAML format
        """
        urls = self.extract_urls(paper)
        paper_type = self.determine_type(paper)

        # Build the YAML entry
        entry = {
            'title': paper.get('title', ''),
            'type': paper_type,
            'year': str(paper.get('year', '')),
            'authors': self.format_authors(paper.get('authors', [])),
            'journal': paper.get('venue', ''),
        }

        # Add URLs
        if 'url' in urls:
            entry['url'] = urls['url']
        elif 'doi' in urls:
            entry['url'] = urls['doi']

        if 'arxiv' in urls:
            entry['arxiv'] = urls['arxiv']

        # Add description (abstract if available)
        if paper.get('abstract'):
            entry['description'] = paper['abstract'][:500] + '...' if len(paper.get('abstract', '')) > 500 else paper.get('abstract')
        else:
            entry['description'] = ""

        return entry

def main():
    parser = argparse.ArgumentParser(description='Update publications from academic APIs')
    parser.add_argument('--year', type=int, default=datetime.now().year,
                       help='Year to fetch publications for (default: current year)')
    parser.add_argument('--author-id', required=True,
                       help='Semantic Scholar author ID (e.g., 3rB_SGYAAAAJ)')
    parser.add_argument('--output', default='_data/publications_new.yml',
                       help='Output YAML file path')
    parser.add_argument('--append', action='store_true',
                       help='Append to existing publications file')

    args = parser.parse_args()

    print(f"Fetching publications for year {args.year}...")

    # Initialize fetcher and formatter
    fetcher = PublicationFetcher()
    formatter = PublicationFormatter()

    # Fetch publications
    papers = fetcher.fetch_from_semantic_scholar(args.author_id, args.year)

    if not papers:
        print(f"No publications found for year {args.year}")
        return

    print(f"Found {len(papers)} publications")

    # Format publications
    formatted_pubs = []
    for paper in papers:
        formatted = formatter.format_to_yaml(paper)
        formatted_pubs.append(formatted)
        print(f"  - {formatted['title'][:60]}...")

    # Load existing publications if appending
    if args.append and os.path.exists('_data/publications.yml'):
        with open('_data/publications.yml', 'r') as f:
            existing_pubs = yaml.safe_load(f) or []
        formatted_pubs = formatted_pubs + existing_pubs

    # Write to YAML file
    with open(args.output, 'w') as f:
        yaml.dump(formatted_pubs, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"\nPublications written to {args.output}")
    print("\nNext steps:")
    print("1. Review the generated file for accuracy")
    print("2. Manually add any missing information (descriptions, thumbnails, etc.)")
    print("3. Move/merge with _data/publications.yml")

if __name__ == '__main__':
    import os
    main()
