# 📚 MongoDB Performance Guides

## ⚠️ Known Issues

**PPTX Compatibility**: Speaker and published PPTX files may not open properly in Apple Keynote but work fine in Google Slides and Microsoft PowerPoint. This is a known limitation with the Pandoc PPTX generation. For Keynote users, we recommend:
- Using the HTML versions for presentation
- Importing PPTX files through Google Slides first
- Using the base PPTX version which has better compatibility

A comprehensive collection of in-depth field guides covering MongoDB performance optimization for Node.js/Mongoose developers.

## 🎯 Available Guides

### 📖 [MongoDB Indexing Field Guide](./mongodb-indexing-field-guide/)
**Duration:** ~70-85 minutes (with Q&A)  
**Format:** Comprehensive technical deep-dive with practical examples

**Coverage:**
- MongoDB query optimizer internals
- ESR (Equality, Sort, Range) indexing pattern
- Compound vs single field indexes
- Aggregation pipeline optimization ($lookup performance pitfalls)
- Update/Delete query optimization
- Mongoose-specific best practices
- Critical anti-patterns and gotchas:
  - Multiple range query limitations
  - Large $in array performance degradation
  - Array index scalability problems
  - Group/sort ordering issues
  - Compound index selectivity traps
  - Regex optimization nuances (static text vs operators)
- Performance monitoring and analysis

### 📊 [Aggregation Operators Performance Guide](./aggregation-operators-guide/)
**Duration:** ~90-120 minutes (with Q&A)  
**Format:** Complete operator-by-operator performance analysis with comprehensive coverage

**Coverage:**
- **40+ pipeline operators** with detailed performance analysis
- **Complete operator categories:** $match, $project, $addFields, $replaceRoot, $lookup, $graphLookup, $unionWith, $group, $bucket, $facet, $setWindowFields, $geoNear, $search, $out, $merge, and more
- **Memory management by operator type:** streaming vs blocking operations
- **Version-specific optimizations** across MongoDB 6, 7, and 8:
  - MongoDB 6.0: $topN/$bottomN, enhanced $lookup, $densify/$fill 
  - MongoDB 7.0: Enhanced slot-based execution, better query planning
  - MongoDB 8.0: Block processing (200% faster), improved memory management
- **Production optimization patterns:** Complete ESR principle for aggregations
- **Critical anti-patterns for every operator:** $lookup scaling, $group memory explosions, $sort limits, $unwind explosions, $facet accumulation
  - $group memory traps and unlimited accumulation
  - $sort without index support causing 100MB limit hits
  - $unwind array explosion and document multiplication
- Real-world optimization case studies:
  - E-commerce analytics: 45-second → 3-second pipeline optimization
  - IoT time-series processing with MongoDB 8.0 block processing
  - Large-scale reporting with incremental aggregation strategies
- Production monitoring, debugging, and performance profiling techniques

## 🚀 Quick Start

### Prerequisites
```bash
# Install Pandoc (required for all builds)
# macOS
brew install pandoc

# Ubuntu/Debian
sudo apt-get install pandoc

# Windows
# Download from https://pandoc.org/installing.html

# Python 3 (required for note merging)
# Should be pre-installed on most systems
```

### Build All Guides
```bash
# Build all guides (all 6 outputs each)
make all

# Build specific guide
make build-guide GUIDE=mongodb-indexing-field-guide
make build-guide GUIDE=aggregation-operators-guide

# Build specific versions
make base-all      # Base versions only
make speaker-all   # Speaker versions only  
make published-all # Published versions only
```

### Development & Preview
```bash
# Open HTML files in browser
make dev-all           # All base HTML files
make dev-speaker-all   # All speaker HTML files
make dev-published-all # All published HTML files

# Individual guide development
cd mongodb-indexing-field-guide
make dev-speaker       # Build and open speaker HTML
make dev-published     # Build and open published HTML
```

### Utility Commands
```bash
# List available guides
make list-guides

# Check system requirements
make check-requirements

# Clean all build files
make clean

# Show statistics
make stats

# Validate guide structures
make validate

# GitHub Pages deployment
make github-pages      # Build all guides and prepare for GitHub Pages
make generate-index    # Generate index.html only (if guides already built)
make deploy-pages      # Show deployment instructions
```

## 📁 Output Structure

Each guide generates 6 output files in `build/guide-name/`:

```
build/mongodb-indexing-field-guide/
├── mongodb-indexing-field-guide.pptx              # Base PPTX
├── mongodb-indexing-field-guide.html              # Base HTML
├── mongodb-indexing-field-guide-speaker.pptx      # Speaker PPTX (with presenter notes)
├── mongodb-indexing-field-guide-speaker.html      # Speaker HTML (with expandable notes)
├── mongodb-indexing-field-guide-published.pptx    # Published PPTX (with full notes)
└── mongodb-indexing-field-guide-published.html    # Published HTML (with expandable notes)
```

## 🛠️ Build System

### Technology Stack
- **Pandoc**: Universal document converter for PPTX and HTML generation
- **Python 3**: Custom scripts for merging notes and content processing
- **Make**: Build automation and dependency management
- **Custom HTML Templates**: Responsive presentation templates with slide navigation

### Key Features
- **Presenter Notes**: Speaker and published notes appear in PowerPoint's presenter notes section
- **Interactive HTML**: Slide navigation with expandable notes sections
- **Cross-Platform**: Works on macOS, Linux, and Windows
- **Automated Builds**: Single command builds all guides in all formats
- **GitHub Pages Ready**: Automatic deployment with dynamic index generation

## 📋 Guide Structure

Each guide follows this structure:
```
guide-name/
├── guide-name.md      # Main presentation content
├── speaker.md         # Speaker notes (concise, presentation-focused)
├── published.md       # Published notes (comprehensive, learning-focused)
├── Makefile          # Build automation
└── README.md         # Guide-specific documentation
```

## 🎯 Presentation Formats

### Base Version
- **Content**: Main presentation slides only
- **Use Case**: Clean presentation without notes
- **Output**: PPTX, HTML

### Speaker Version  
- **Content**: Main slides + speaker notes
- **Use Case**: Presenter reference with talking points
- **Output**: PPTX (notes in presenter section), HTML (expandable notes)

### Published Version
- **Content**: Main slides + comprehensive notes
- **Use Case**: Self-paced learning and reference
- **Output**: PPTX (full notes in presenter section), HTML (expandable notes)

## 🔧 Customization

### Adding New Guides
1. Create a new directory ending with `-guide`
2. Copy the template structure from `template/`
3. Add your content to the three markdown files
4. The build system will automatically detect and build your guide

### Modifying Build Process
- **Scripts**: Located in `scripts/` directory
- **HTML Templates**: Custom templates in `scripts/template-html-with-notes-v2.html`
- **Makefiles**: Each guide has its own Makefile, parent Makefile orchestrates builds

## 🌐 GitHub Pages Deployment

The guides can be easily deployed to GitHub Pages for web hosting:

```bash
# Build and prepare for GitHub Pages
cd slides
make github-pages

# Deploy (commit and push)
git add docs/
git commit -m "Update GitHub Pages"
git push origin main
```

**Features:**
- **Dynamic Index**: Automatically generates landing page with all available guides
- **Smart Metadata**: Extracts duration and descriptions from guide READMEs
- **Version Detection**: Shows only available HTML versions (base, speaker, published)
- **Template-based**: Customizable styling via `template/index-template.html`
- **SEO Optimized**: Includes proper meta tags and Open Graph data

See [GITHUB_PAGES.md](./GITHUB_PAGES.md) for detailed deployment instructions.

## 📞 Support

For issues or questions about the build system:
- Check `make help` for available commands
- Review individual guide README files
- Ensure Pandoc and Python 3 are properly installed 