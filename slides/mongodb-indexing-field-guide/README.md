# MongoDB Indexing Field Guide

## ⚠️ Known Issues

**PPTX Compatibility**: Speaker and published PPTX files may not open properly in Apple Keynote but work fine in Google Slides and Microsoft PowerPoint. This is a known limitation with the Pandoc PPTX generation. For Keynote users, we recommend:
- Using the HTML versions for presentation
- Importing PPTX files through Google Slides first
- Using the base PPTX version which has better compatibility

This comprehensive field guide covers MongoDB indexing and query optimization for Node.js/Mongoose developers of all levels.

## 🎯 Presentation Overview

**Target Audience:** Node.js & Mongoose developers  
**Duration:** ~70-85 minutes (with Q&A)
**Format:** Technical deep-dive with practical examples and critical anti-patterns

### Topics Covered:
- MongoDB query optimizer internals
- ESR (Equality, Sort, Range) indexing pattern
- Compound vs single field indexes
- Aggregation pipeline optimization
- Update/Delete query optimization
- $lookup performance pitfalls and scalability issues
- Mongoose-specific best practices
- Critical anti-patterns and gotchas:
  - Multiple range query limitations
  - Large $in array performance degradation
  - Array index scalability problems
  - Group/sort ordering issues
  - Compound index selectivity traps
  - Regex optimization nuances (static text vs operators)
- Performance monitoring and analysis

## 🛠️ Building the Presentation

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

### Generate Slides

#### 1. Build All Formats (6 outputs)
```bash
make all
```

#### 2. Build Specific Versions
```bash
make base          # Base PPTX and HTML
make speaker       # Speaker PPTX and HTML with notes
make published     # Published PPTX and HTML with full notes
```

#### 3. Individual Format Builds
```bash
make base-pptx     # Base PowerPoint only
make base-html     # Base HTML only
make speaker-pptx  # Speaker PowerPoint with notes
make speaker-html  # Speaker HTML with expandable notes
make published-pptx # Published PowerPoint with full notes
make published-html # Published HTML with expandable notes
```

### Development Options

#### Development Mode (opens in browser)
```bash
make dev            # Build base HTML and open in browser
make dev-speaker    # Build speaker HTML and open in browser
make dev-published  # Build published HTML and open in browser
```

#### Utility Commands
```bash
make clean          # Clean generated files
make stats          # Show presentation statistics
make validate-slides # Validate slide structure
make help           # Show available commands
```

## 📁 File Structure

```
mongodb-indexing-field-guide/
├── mongodb-indexing-field-guide.md    # Main presentation
├── speaker.md                         # Speaker notes for presenters
├── published.md                       # Comprehensive learning guide
├── README.md                          # This file
├── package.json                       # Build dependencies and scripts
├── Makefile                          # Make targets for building
└── .gitignore                        # Build artifacts exclusion
```

### Output Structure
All generated files are placed in `../build/mongodb-indexing-field-guide/`:
```
build/mongodb-indexing-field-guide/
├── mongodb-indexing-field-guide.pptx              # Base PowerPoint
├── mongodb-indexing-field-guide.html              # Base HTML
├── mongodb-indexing-field-guide-speaker.pptx      # Speaker PowerPoint (with notes)
├── mongodb-indexing-field-guide-speaker.html      # Speaker HTML (with notes)
├── mongodb-indexing-field-guide-published.pptx    # Published PowerPoint (with full notes)
└── mongodb-indexing-field-guide-published.html    # Published HTML (with full notes)
```

## 🎨 Customization

### Build System
The presentation uses a Pandoc-based build system with:
- **Pandoc**: Universal document converter for PPTX and HTML generation
- **Python 3**: Custom scripts for merging notes and content processing
- **Make**: Build automation and dependency management
- **Custom HTML Templates**: Responsive presentation templates with slide navigation

### Adding Custom Styles
Modify the HTML template in `../scripts/template-html-with-notes-v2.html` for custom themes and styling.

## 📊 Presentation Tips

### For Speakers:
1. **Timing**: Allow 2-3 minutes per slide for technical content
2. **Interaction**: Pause for questions after each major section
3. **Live Demo**: Consider having MongoDB Compass ready for live examples
4. **Audience Level**: Adjust technical depth based on audience experience

### Key Sections to Emphasize:
- **ESR Rule** (slides 7-8) - Core concept for developers
- **Query Optimizer Stages** (slides 5-6) - Understanding the "why"
- **Anti-Patterns** (slides 20-21) - Common mistakes to avoid
- **Mongoose Integration** (slides 17-18) - Practical application

## 🔧 Development Workflow

### Quick Build Script
```bash
#!/bin/bash
# build-slides.sh
echo "Building MongoDB Indexing Field Guide..."
make all
echo "✅ Generated: All 6 output formats"
```

### Make it executable:
```bash
chmod +x build-slides.sh
./build-slides.sh
```

## 📈 Analytics and Feedback

### Post-Presentation:
- Collect feedback on technical depth
- Note questions for FAQ section
- Update examples based on real-world scenarios
- Consider creating follow-up workshops

## 🚀 Next Steps

### Advanced Topics (Future Presentations):
- MongoDB Sharding and Index Distribution
- Time Series Collections and Indexing
- Atlas Search and Full-Text Indexing
- Index Maintenance and Rebuild Strategies

### Workshop Ideas:
- Hands-on Index Analysis with Real Data
- Performance Tuning Lab Session
- Mongoose Schema Design Workshop

## 📞 Support

For questions about:
- **Pandoc usage**: [Pandoc Documentation](https://pandoc.org/)
- **Build system**: Check `make help` for available commands
- **Presentation content**: Contact the development team
- **MongoDB specifics**: [MongoDB University](https://university.mongodb.com/)

---

*Created with ❤️ for the developer community* 