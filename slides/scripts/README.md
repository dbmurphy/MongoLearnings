# MongoDB Performance Guides - Scripts Directory

This directory contains the Python scripts and HTML templates used by the MongoDB Performance Guides build system.

## Core Scripts

### Note Merging
- **`merge-notes-for-pandoc-v2.py`** - Merges speaker or published notes into main presentation content for Pandoc processing
  - Converts slide separators to `---SLIDE---` format
  - Cleans HTML comments from notes for PPTX compatibility
  - Converts `#` headers to `##` in notes to avoid slide separation conflicts
  - Uses `::: notes` syntax for Pandoc presenter notes

### HTML Templates
- **`template-html-with-notes-v2.html`** - Custom HTML template for Pandoc presentations
  - Responsive dark theme optimized for developer audiences
  - JavaScript-powered slide navigation with left/right arrows
  - Expandable notes sections for speaker and published versions
  - Automatic slide splitting by `---SLIDE---` separators

## Usage

### Note Merging Script
```bash
# Merge speaker notes
python3 merge-notes-for-pandoc-v2.py main.md speaker.md output.md --notes-type=Speaker

# Merge published notes  
python3 merge-notes-for-pandoc-v2.py main.md published.md output.md --notes-type=Published
```

### Makefile Integration
The scripts are integrated into guide Makefiles:

```makefile
# Script variables
MERGE_NOTES_SCRIPT = ../scripts/merge-notes-for-pandoc-v2.py
HTML_TEMPLATE = ../scripts/template-html-with-notes-v2.html

# Usage in targets
speaker-html:
	@python3 $(MERGE_NOTES_SCRIPT) $(MAIN_FILE) $(SPEAKER_FILE) $(BUILD_DIR)/$(PRESENTATION_NAME)-speaker.md --notes-type=Speaker
	@pandoc --from markdown --to html -o $(SPEAKER_HTML) --template=$(HTML_TEMPLATE) $(BUILD_DIR)/$(PRESENTATION_NAME)-speaker.md
```

## Build Process

### 1. Note Merging
The `merge-notes-for-pandoc-v2.py` script:
- Extracts slides from main presentation using `---` separators
- Extracts notes from speaker.md or published.md
- Merges notes into slides using `::: notes` syntax
- Converts slide separators to `---SLIDE---` for HTML processing
- Cleans HTML comments and formats notes for PPTX compatibility

### 2. HTML Generation
The `template-html-with-notes-v2.html` template:
- Processes merged content with Pandoc
- Splits content by `---SLIDE---` separators using JavaScript
- Creates individual slide divs with proper navigation
- Processes `::: notes` blocks into expandable sections
- Provides slide navigation with arrow keys and buttons

### 3. PPTX Generation
Pandoc processes the merged content:
- `::: notes` syntax creates presenter notes in PowerPoint
- Clean note content (no HTML comments) ensures PPTX compatibility
- Slide separators create proper slide breaks

## File Structure

```
scripts/
├── merge-notes-for-pandoc-v2.py      # Active note merging script
├── template-html-with-notes-v2.html  # Active HTML template
└── README.md                         # This documentation
```

## Technical Details

### Note Merging Process
1. **Extract slides**: Split main content by `---` separators
2. **Extract notes**: Split notes content by `---` separators  
3. **Match slides**: Align slides with corresponding notes
4. **Merge content**: Insert notes using `::: notes` syntax
5. **Clean content**: Remove HTML comments, convert headers
6. **Format separators**: Use `---SLIDE---` for HTML processing

### HTML Template Features
- **Responsive design**: Works on desktop and mobile
- **Dark theme**: Optimized for developer audiences
- **Slide navigation**: Left/right arrows and slide counter
- **Expandable notes**: Click to show/hide speaker/published notes
- **Keyboard shortcuts**: Arrow keys for navigation
- **Custom styling**: Professional presentation appearance

### PPTX Compatibility
- **Presenter notes**: Notes appear in PowerPoint's notes section
- **Clean content**: No HTML or markdown formatting in notes
- **Proper slide breaks**: Each slide is properly separated
- **Cross-platform**: Works in PowerPoint, Keynote, and other presentation software

## Development

### Modifying the Merge Script
The `merge-notes-for-pandoc-v2.py` script can be customized for:
- Different note formats
- Alternative slide separators
- Custom content processing
- Additional output formats

### Modifying the HTML Template
The `template-html-with-notes-v2.html` template can be customized for:
- Different themes and styling
- Alternative navigation methods
- Custom note display formats
- Additional interactive features

## Troubleshooting

### Common Issues
1. **PPTX corruption**: Usually caused by HTML comments in notes
2. **HTML navigation not working**: Check that `---SLIDE---` separators are present
3. **Notes not appearing**: Verify `::: notes` syntax is correct
4. **Slide count wrong**: Ensure slide separators are properly formatted

### Debugging
- Check merged markdown files in `build/` directory
- Verify HTML output structure
- Test PPTX files in presentation software
- Review console errors in browser for HTML issues
