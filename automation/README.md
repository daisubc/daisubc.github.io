# DAIS Lab Website Automation Scripts

This directory contains automation scripts for maintaining the UBC DAIS Lab website.

## Publications Auto-Update

### Overview

The `update_publications.py` script automatically fetches publications from Semantic Scholar API and formats them into the website's YAML structure.

### Setup

1. **Find Your Semantic Scholar Author ID**

   Visit [Semantic Scholar](https://www.semanticscholar.org/) and search for "Bhushan Gopaluni"

   The author ID is in the URL: `https://www.semanticscholar.org/author/R.-Bhushan-Gopaluni/XXXXXXX`

   For Bhushan Gopaluni, it appears to be available via their API.

2. **Install Dependencies**

   ```bash
   pip install requests pyyaml
   ```

3. **Set Up GitHub Secrets (for automation)**

   Go to: Settings → Secrets and variables → Actions → New repository secret

   Add:
   - Name: `SEMANTIC_SCHOLAR_AUTHOR_ID`
   - Value: Your Semantic Scholar author ID

### Manual Usage

Fetch publications for the current year:

```bash
python automation/update_publications.py --author-id <YOUR_AUTHOR_ID> --year 2025
```

This creates `_data/publications_new.yml` with the new publications.

**Review and merge:**
1. Review the generated file
2. Add missing descriptions, PDFs, thumbnails
3. Merge into `_data/publications.yml`

### Automated Usage (GitHub Actions)

The workflow runs automatically:
- **Schedule**: Monthly on the 1st at 9am UTC
- **Manual**: Go to Actions → Update Publications → Run workflow

When publications are found, it creates a Pull Request for review.

### Available Options

```bash
python automation/update_publications.py [OPTIONS]

Options:
  --year YEAR           Year to fetch (default: current year)
  --author-id ID        Semantic Scholar author ID (required)
  --output FILE         Output file path (default: _data/publications_new.yml)
  --append              Append to existing publications file
```

## Alternative: Manual Input Helper

If you prefer more control, you can use the script with DOIs:

```python
# Add this to update_publications.py for DOI-based fetching
def fetch_by_doi_list(dois: List[str]):
    """Fetch multiple publications by DOI"""
    fetcher = PublicationFetcher()
    formatter = PublicationFormatter()

    publications = []
    for doi in dois:
        paper = fetcher.fetch_by_doi(doi)
        if paper:
            publications.append(formatter.format_to_yaml(paper))

    return publications
```

Then create a `dois.txt` file with one DOI per line and run:

```bash
python automation/update_publications.py --from-dois dois.txt
```

## Updating People Information

Currently manual, but you can create a similar script for:
- Tracking student status changes
- Adding new members
- Moving people to alumni

**Suggested structure:**
```
automation/
  update_people.py      # Script to manage people updates
  people_config.yml     # Configuration for status changes
```

## Troubleshooting

### Semantic Scholar API Issues

- **Rate limits**: The API has rate limits. Add delays between requests if needed.
- **Missing papers**: Not all papers may be indexed. Manual verification recommended.

### Alternative APIs

If Semantic Scholar doesn't work well, consider:

1. **ORCID API**: Requires ORCID iD
   ```bash
   https://pub.orcid.org/v3.0/<ORCID-ID>/works
   ```

2. **CrossRef API**: Good for DOI-based lookups
   ```bash
   https://api.crossref.org/works/<DOI>
   ```

3. **Google Scholar**: No official API, scraping is unreliable

## Future Enhancements

- [ ] Add support for ORCID API
- [ ] Automatic thumbnail generation from paper PDFs
- [ ] Integration with arXiv for preprints
- [ ] Slack/email notifications for new publications
- [ ] People status change automation
- [ ] Award and news auto-updates

## Contributing

To improve these scripts:
1. Test changes locally first
2. Update this documentation
3. Create a PR with your improvements

## Support

For issues or questions:
- Check existing GitHub Issues
- Create a new issue with details
- Tag with `automation` label
