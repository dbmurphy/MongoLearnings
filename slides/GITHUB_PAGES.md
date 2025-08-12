# GitHub Pages Deployment Guide

This guide explains how to deploy your MongoDB Performance Guides to GitHub Pages.

## Quick Start

### Option 1: Manual Deployment
```bash
# Build and prepare for GitHub Pages
cd slides
make github-pages

# Commit and push to trigger deployment
git add docs/
git commit -m "Update GitHub Pages"
git push origin main
```

### Option 3: Generate Index Only
```bash
# Just regenerate the index.html (if guides already built)
make generate-index
```

### Option 2: Automatic Deployment (Recommended)
The GitHub Actions workflow will automatically build and deploy when you push to the `main` branch.

**Note**: The workflow assumes the slides are in the `slides/` directory at the repository root.

## Setup Steps

### 1. Enable GitHub Pages
1. Go to your repository settings
2. Navigate to "Pages" in the sidebar
3. Under "Source", select "Deploy from a branch"
4. Choose branch: `main` (or `gh-pages` if using Actions)
5. Choose folder: `/docs` (or `/` if using Actions)
6. Click "Save"

### 2. Configure Repository
- Ensure your repository is public (or you have GitHub Pro for private repos)
- The `docs/` directory will be served at `https://yourusername.github.io/MongoLearnings/`
- The slides are located in the `slides/` directory at the repository root

## File Structure

After deployment, your site will have this structure:
```
https://yourusername.github.io/MongoLearnings/
├── index.html                                    # Auto-generated landing page
├── mongodb-indexing-field-guide/
│   ├── mongodb-indexing-field-guide.html         # Base version
│   ├── mongodb-indexing-field-guide-speaker.html # Speaker notes
│   └── mongodb-indexing-field-guide-published.html # Published notes
└── aggregation-operators-guide/
    ├── aggregation-operators-guide.html          # Base version
    ├── aggregation-operators-guide-speaker.html  # Speaker notes
    └── aggregation-operators-guide-published.html # Published notes
```

## Dynamic Index Generation

The `index.html` is automatically generated and includes:

- **Auto-detection**: Finds all `*-guide` directories
- **Smart metadata**: Extracts duration and description from each guide's README.md
- **Version detection**: Shows only available HTML versions (base, speaker, published)
- **Template-based**: Uses `template/index-template.html` for consistent styling
- **SEO optimized**: Includes proper meta tags and Open Graph data

When you add a new guide:
1. Create the guide directory (ending with `-guide`)
2. Add a README.md with duration and coverage information
3. Build the guide: `make build-guide GUIDE=your-new-guide`
4. Regenerate index: `make generate-index` or `make github-pages`

## Available Commands

```bash
# Build all guides and prepare for GitHub Pages
make github-pages

# Generate index.html only (if guides already built)
make generate-index

# Show deployment instructions
make deploy-pages

# Build specific guide for GitHub Pages
make build-guide GUIDE=mongodb-indexing-field-guide
make github-pages
```

## Customization

### Update Landing Page
The `docs/index.html` is automatically generated from `template/index-template.html`. To customize:

1. **Edit the template**: Modify `template/index-template.html` to change styling, branding, etc.
2. **Regenerate**: Run `make generate-index` to apply changes
3. **Template variables available**:
   - `{{SITE_TITLE}}` - Page title
   - `{{SITE_DESCRIPTION}}` - Meta description
   - `{{HEADER_TITLE}}` - Main heading
   - `{{HEADER_DESCRIPTION}}` - Subtitle
   - `{{GUIDE_CARDS}}` - Auto-generated guide cards
   - `{{FOOTER_TEXT}}` - Footer text
   - `{{GITHUB_URL}}` - GitHub repository URL

**Note**: Don't edit `docs/index.html` directly as it gets overwritten on each build.

### Add Custom CSS/JS
You can add custom assets to the `docs/` directory:
```
docs/
├── index.html
├── css/
│   └── custom.css
├── js/
│   └── analytics.js
└── guides/
    └── ...
```

### SEO Optimization
- Add meta tags to `docs/index.html`
- Include Open Graph tags for social sharing
- Add structured data for search engines

## Troubleshooting

### Build Issues
```bash
# Check if all dependencies are installed
make check-requirements

# Clean and rebuild
make clean
make all
make github-pages
```

**Note**: Make sure you're in the `slides/` directory when running these commands.

### Deployment Issues
- Ensure the `docs/` directory is committed to git
- Check GitHub Actions logs if using automatic deployment
- Verify GitHub Pages is enabled in repository settings

### Performance
- HTML files are optimized for presentation
- Consider adding image optimization for any embedded images
- Use CDN for external resources if needed

## Analytics (Optional)

Add Google Analytics to `docs/index.html`:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

## Security

- All content is static HTML
- No server-side processing
- Consider adding Content Security Policy headers
- Review external dependencies for security updates
