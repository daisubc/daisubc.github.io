# Complete Setup Guide for Website Automation

This guide will help you set up the automated publication system for the DAIS Lab website.

## Prerequisites

- GitHub repository access
- Python 3.7+ installed
- Basic command line knowledge

## Step 1: Get API Access

### Option A: Semantic Scholar API (Recommended)

Semantic Scholar offers free API access with registration.

1. **Register for API Key:**
   - Visit: https://www.semanticscholar.org/product/api
   - Click "Get API Key"
   - Fill out the form (it's free for academic use)
   - You'll receive an API key via email

2. **Find Your Author ID:**
   - Go to: https://www.semanticscholar.org/
   - Search for "R. Bhushan Gopaluni"
   - Your author ID is in the URL: `/author/R.-B.-Gopaluni/1766686`
   - Save this ID: **1766686**

### Option B: Manual Entry (Easiest to Start)

If you prefer manual control or the API isn't working:
- Use the `quick_add_publication.py` script with DOIs
- Or manually create YAML entries

## Step 2: Configure GitHub Secrets

GitHub Secrets store sensitive information securely.

1. **Navigate to Repository Settings:**
   ```
   Your Repository → Settings → Secrets and variables → Actions
   ```

2. **Add Secrets:**

   Click "New repository secret" and add each of these:

   | Name | Value | Description |
   |------|-------|-------------|
   | `SEMANTIC_SCHOLAR_AUTHOR_ID` | `1766686` | Your Semantic Scholar author ID |
   | `SEMANTIC_SCHOLAR_API_KEY` | Your API key | From Step 1 (if you got one) |

## Step 3: Update Automation Scripts

If you have an API key, update the scripts to use it:

### Edit `automation/update_publications.py`:

Find the `fetch_from_semantic_scholar` function and add the API key header:

```python
headers = {}
api_key = os.getenv('SEMANTIC_SCHOLAR_API_KEY')
if api_key:
    headers['x-api-key'] = api_key

response = requests.get(url, params=params, headers=headers, timeout=30)
```

## Step 4: Test Locally

### Install Dependencies:

```bash
cd /path/to/daisubc.github.io
pip install -r automation/requirements.txt
```

### Test Manual Addition:

```bash
# Add a publication by creating YAML manually
python automation/quick_add_publication.py \
  --doi 10.1002/smll.202504877 \
  --output _data/new_pub.yml
```

If the DOI fetch fails, you can create entries manually using this template:

```yaml
- title: "Your Paper Title"
  type: "paper"  # or "conference"
  year: "2025"
  authors: "Author 1, Author 2, R. Bhushan Gopaluni"
  journal: "Journal Name"
  url: "https://doi.org/10.xxxx/xxxxx"
  description: "Brief description of the paper..."
```

### Test Automated Fetching (if you have API key):

```bash
export SEMANTIC_SCHOLAR_API_KEY="your-api-key-here"
python automation/update_publications.py \
  --year 2025 \
  --author-id 1766686 \
  --output _data/test_pubs.yml
```

## Step 5: Enable GitHub Actions Workflow

The workflow file is already created at `.github/workflows/update-publications.yml`

### Manual Trigger:

1. Go to your repository on GitHub
2. Click "Actions" tab
3. Select "Update Publications" workflow
4. Click "Run workflow"
5. Select year (or leave blank for current year)
6. Click "Run workflow" button

### Automatic Schedule:

The workflow runs automatically on the 1st of each month at 9am UTC.

No additional setup needed - it will use the secrets you configured.

## Step 6: Review and Merge Pull Requests

When publications are found:

1. **Automated PR Created:**
   - Go to "Pull Requests" tab
   - Look for "[Automated] New Publications Found"

2. **Review Changes:**
   - Check publication titles and authors
   - Verify journal names and years
   - Add missing information:
     - PDF links
     - Thumbnails
     - Better descriptions
     - ArXiv links
     - Code repositories

3. **Merge:**
   - Once satisfied, click "Merge pull request"
   - Website updates automatically!

## Alternative: Fully Manual Workflow

If automation isn't working or you prefer manual control:

### Create Publications Manually:

1. Copy the YAML template:
```yaml
- title: "Paper Title"
  type: "paper"
  year: "2025"
  authors: "Author 1, Author 2, R. Bhushan Gopaluni"
  journal: "Journal Name"
  url: "https://link-to-paper"
  description: "Description..."
```

2. Add to `_data/publications.yml` at the top (newest first)

3. Commit and push:
```bash
git add _data/publications.yml
git commit -m "Add new publication: Paper Title"
git push
```

### Use Google Scholar Manually:

1. Go to your Google Scholar profile
2. Find new publications
3. Click on each paper
4. Copy: title, authors, journal, year, DOI/URL
5. Create YAML entry manually
6. Add to `_data/publications.yml`

## Troubleshooting

### API Returns 403 Forbidden

**Cause:** Missing or invalid API key, or rate limiting

**Solutions:**
1. Register for Semantic Scholar API key
2. Add key to GitHub Secrets
3. Wait a few minutes if rate limited
4. Use manual entry as fallback

### No Publications Found

**Cause:** Papers not indexed yet, wrong author ID, or year mismatch

**Solutions:**
1. Verify author ID: https://www.semanticscholar.org/author/R.-B.-Gopaluni/1766686
2. Check if papers are indexed on Semantic Scholar
3. Try different year
4. Add manually if very recent

### Workflow Doesn't Run

**Cause:** Workflow not enabled, secrets missing, or repository settings

**Solutions:**
1. Check Actions are enabled: Settings → Actions → General
2. Verify secrets are set correctly
3. Try manual trigger first
4. Check workflow logs for errors

## Best Practices

1. **Review Before Merging:**
   - Always review automated PRs
   - Add missing details manually
   - Verify accuracy

2. **Update Regularly:**
   - Run workflow after publishing new papers
   - Check monthly for missed publications
   - Keep descriptions informative

3. **Backup:**
   - Keep local copy of `_data/publications.yml`
   - Use version control (already done via git)

4. **Customize:**
   - Edit scripts for your specific needs
   - Add thumbnails, PDFs, code links manually
   - Adjust automation frequency as needed

## Next Steps

Once publications automation is working, consider:

- Automating people/alumni updates
- Adding award tracking
- Integrating with arXiv for preprints
- Creating news/announcement automation
- Building a dashboard for lab metrics

## Need Help?

- Check automation logs in GitHub Actions
- Review `automation/README.md` for detailed documentation
- File an issue on GitHub with specific errors
- Reach out to lab members who set this up

---

*Last Updated: October 2025*
