# MongoDB Presentation Template

## ⚠️ Known Issues

**PPTX Compatibility**: Speaker and published PPTX files may not open properly in Apple Keynote but work fine in Google Slides and Microsoft PowerPoint. This is a known limitation with the Pandoc PPTX generation. For Keynote users, we recommend:
- Using the HTML versions for presentation
- Importing PPTX files through Google Slides first
- Using the base PPTX version which has better compatibility

A comprehensive template for creating MongoDB-focused presentations with multiple output formats and speaker notes.

## Overview

This template provides a complete structure for building MongoDB presentations that can be delivered in multiple formats: base presentation, speaker notes version, and published learning guide. The build system uses Pandoc for document conversion and includes custom Python scripts for merging notes.

## Content Coverage

- **Base Presentation**: Clean presentation content without notes
- **Speaker Notes**: Concise talking points for presenters
- **Published Guide**: Comprehensive explanations for self-paced learning

## Target Audience

Node.js & Mongoose developers of all levels who need to create technical presentations about MongoDB topics.

## Prerequisites

- Pandoc (for document conversion)
- Python 3 (for note merging scripts)
- Make (for build automation)
- Basic understanding of Markdown

## Learning Outcomes

After using this template, you will:

- Create professional presentations with multiple output formats
- Structure content for different delivery methods
- Automate build processes for consistent output
- Generate speaker notes and published guides from the same source

## Presentation Formats

This template supports multiple formats:

### Base Presentation
- **File**: `{{GUIDE_NAME}}.md`
- **Purpose**: Clean presentation content for live delivery
- **Duration**: Variable based on content
- **Output**: PPTX, HTML

### Speaker Notes Version
- **File**: `speaker.md`
- **Purpose**: Concise talking points for presenters
- **Usage**: Reference during live presentations
- **Output**: PPTX (with presenter notes), HTML (with expandable notes)

### Published Learning Guide
- **File**: `published.md`
- **Purpose**: Comprehensive explanations for self-paced learning
- **Usage**: Reference material and detailed explanations
- **Output**: PPTX (with full notes), HTML (with expandable notes)

## Quick Start

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

### Build Presentations
```bash
# Build all versions (6 outputs total)
make all

# Build specific versions
make base          # Base PPTX and HTML
make speaker       # Speaker PPTX and HTML with notes
make published     # Published PPTX and HTML with full notes

# Individual targets
make base-pptx     # Base PowerPoint only
make base-html     # Base HTML only
make speaker-pptx  # Speaker PowerPoint with notes
make speaker-html  # Speaker HTML with expandable notes
make published-pptx # Published PowerPoint with full notes
make published-html # Published HTML with expandable notes
```

### Development
```bash
make dev            # Build base HTML and open in browser
make dev-speaker    # Build speaker HTML and open in browser
make dev-published  # Build published HTML and open in browser
```

### Output Structure
All generated files are placed in the `build/{{GUIDE_NAME}}/` directory:
```
build/{{GUIDE_NAME}}/
├── {{GUIDE_NAME}}.pptx              # Base PowerPoint
├── {{GUIDE_NAME}}.html              # Base HTML
├── {{GUIDE_NAME}}-speaker.pptx      # Speaker PowerPoint (with presenter notes)
├── {{GUIDE_NAME}}-speaker.html      # Speaker HTML (with expandable notes)
├── {{GUIDE_NAME}}-published.pptx    # Published PowerPoint (with full notes)
└── {{GUIDE_NAME}}-published.html    # Published HTML (with expandable notes)
```

## Content Structure

### Main Presentation (`{{GUIDE_NAME}}.md`)
- **Format**: Pandoc-compatible markdown with `---` slide separators
- **Frontmatter**: Title, subtitle, author, date
- **Content**: Main presentation slides with headings, lists, code examples
- **No notes**: Clean presentation content only

### Speaker Notes (`speaker.md`)
- **Format**: Markdown with `---` slide separators
- **Content**: Concise talking points for each slide
- **Purpose**: Presenter reference during delivery
- **Style**: Brief, action-oriented, presentation-focused

### Published Notes (`published.md`)
- **Format**: Markdown with `---` slide separators
- **Content**: Comprehensive explanations and additional context
- **Purpose**: Self-paced learning and reference material
- **Style**: Detailed, educational, learning-focused

## Build System

### Technology Stack
- **Pandoc**: Universal document converter for PPTX and HTML generation
- **Python 3**: Custom scripts for merging notes and content processing
- **Make**: Build automation and dependency management
- **Custom HTML Templates**: Responsive presentation templates with slide navigation

### Key Features
- **Presenter Notes**: Speaker and published notes appear in PowerPoint's presenter notes section
- **Interactive HTML**: Slide navigation with expandable notes sections
- **Cross-Platform**: Works on macOS, Linux, and Windows
- **Automated Builds**: Single command builds all formats

## Available Make Targets

### Primary Targets
```bash
all              # Build all 6 outputs (base, speaker, published)
base             # Build base PPTX and HTML
speaker          # Build speaker PPTX and HTML
published        # Build published PPTX and HTML
```

### Individual Targets
```bash
base-pptx        # Build base PowerPoint
base-html        # Build base HTML
speaker-pptx     # Build speaker PowerPoint with notes
speaker-html     # Build speaker HTML with expandable notes
published-pptx   # Build published PowerPoint with full notes
published-html   # Build published HTML with expandable notes
```

### Development Targets
```bash
dev              # Build and open base HTML in browser
dev-speaker      # Build and open speaker HTML in browser
dev-published    # Build and open published HTML in browser
```

### Utility Targets
```bash
clean            # Clean generated files
stats            # Show presentation statistics
validate-slides  # Validate slide structure
help             # Show this help message
```

## Content Guidelines

### Slide Structure
- Use `#` for slide titles
- Use `##` for section headings within slides
- Use `---` to separate slides
- Keep slides focused and concise

### Code Examples
```markdown
```javascript
// Example code
const result = db.collection.find({ field: value });
```
```

### Images and Media
```markdown
![Alt text](image.png)
```

### Speaker Notes Guidelines
- Keep notes concise and action-oriented
- Include key talking points
- Add timing cues if needed
- Reference specific examples or data

### Published Notes Guidelines
- Provide comprehensive explanations
- Include additional context and background
- Add links to resources and documentation
- Include troubleshooting tips and gotchas

## Customization

### Modifying the Build Process
- **Scripts**: Located in `../scripts/` directory
- **HTML Templates**: Custom templates in `../scripts/template-html-with-notes-v2.html`
- **Makefile**: Guide-specific build automation

### Adding Custom Styling
- Modify the HTML template for custom themes
- Add custom CSS for specific styling needs
- Customize JavaScript for additional interactivity

## Troubleshooting

### Common Issues
1. **PPTX corruption**: Usually caused by HTML comments in notes
2. **HTML navigation not working**: Check that slide separators are properly formatted
3. **Notes not appearing**: Verify note files exist and are properly formatted
4. **Build errors**: Ensure Pandoc and Python 3 are installed

### Getting Help
- Check `make help` for available commands
- Review the main project README for system requirements
- Ensure all dependencies are properly installed 