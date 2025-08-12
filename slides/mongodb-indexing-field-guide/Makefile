# Makefile for MongoDB Indexing Field Guide
# Builds presentation in multiple formats using Pandoc

PRESENTATION_NAME = mongodb-indexing-field-guide
MAIN_FILE = $(PRESENTATION_NAME).md
SPEAKER_FILE = speaker.md
PUBLISHED_FILE = published.md
BUILD_DIR = ../build/$(PRESENTATION_NAME)

# Pandoc slide processing scripts
MERGE_NOTES_SCRIPT = ../scripts/merge-notes-for-pandoc-v2.py
HTML_TEMPLATE = $(shell realpath ../scripts/template-html-with-notes-v2.html)

# Output files
BASE_PPTX = $(BUILD_DIR)/$(PRESENTATION_NAME).pptx
BASE_HTML = $(BUILD_DIR)/$(PRESENTATION_NAME).html
SPEAKER_PPTX = $(BUILD_DIR)/$(PRESENTATION_NAME)-speaker.pptx
SPEAKER_HTML = $(BUILD_DIR)/$(PRESENTATION_NAME)-speaker.html
PUBLISHED_PPTX = $(BUILD_DIR)/$(PRESENTATION_NAME)-published.pptx
PUBLISHED_HTML = $(BUILD_DIR)/$(PRESENTATION_NAME)-published.html

# Default target - builds all 6 outputs
.PHONY: all
all: base speaker published
	@echo "🎉 All 6 outputs built successfully!"

# Base version targets
.PHONY: base base-pptx base-html
base: base-pptx base-html
	@echo "✅ Base version complete!"

base-pptx:
	@echo "🚀 Building base PPTX..."
	@mkdir -p $(BUILD_DIR)
	@sed 's/^---$$/##/' $(MAIN_FILE) | pandoc --from markdown --to pptx -o $(BASE_PPTX) --slide-level=1
	@echo "✅ Base PPTX saved to $(BASE_PPTX)"

base-html:
	@echo "🚀 Building base HTML..."
	@echo "🔍 Debug: HTML_TEMPLATE = $(HTML_TEMPLATE)"
	@echo "🔍 Debug: CURDIR = $(CURDIR)"
	@echo "🔍 Debug: Checking if template exists..."
	@ls -la "$(HTML_TEMPLATE)" || echo "❌ Template file not found!"
	@echo "🔍 Debug: Checking scripts directory..."
	@ls -la "../scripts/" || echo "❌ Scripts directory not found!"
	@echo "🔍 Debug: Checking if template exists in scripts..."
	@ls -la "../scripts/template-html-with-notes-v2.html" || echo "❌ Template not found in scripts!"
	@echo "🔍 Debug: Pandoc version and data dir..."
	@pandoc --version | head -1 || echo "❌ Pandoc not found!"
	@pandoc --data-dir="../scripts" --print-default-data-file=templates/template-html-with-notes-v2.html > /dev/null 2>&1 && echo "✅ Template found via --data-dir" || echo "❌ Template not found via --data-dir"
	@mkdir -p $(BUILD_DIR)
	@sed 's/^---$$/#/' $(MAIN_FILE) | pandoc --from markdown --to html -o $(BASE_HTML) --template="template-html-with-notes-v2.html" --data-dir="../scripts" --slide-level=1
	@echo "✅ Base HTML saved to $(BASE_HTML)"

# Speaker version targets
.PHONY: speaker speaker-pptx speaker-html
speaker: speaker-pptx speaker-html
	@echo "✅ Speaker version complete!"

speaker-pptx:
	@echo "🎤 Building speaker PPTX..."
	@mkdir -p $(BUILD_DIR)
	@python3 $(MERGE_NOTES_SCRIPT) $(MAIN_FILE) $(SPEAKER_FILE) $(BUILD_DIR)/$(PRESENTATION_NAME)-speaker.md --notes-type=Speaker
	@sed 's/^---$$/##/' $(BUILD_DIR)/$(PRESENTATION_NAME)-speaker.md | pandoc --from markdown --to pptx -o $(SPEAKER_PPTX) --slide-level=1
	@echo "✅ Speaker PPTX saved to $(SPEAKER_PPTX)"

speaker-html:
	@echo "🎤 Building speaker HTML..."
	@echo "🔍 Debug: HTML_TEMPLATE = $(HTML_TEMPLATE)"
	@echo "🔍 Debug: Checking template for speaker HTML..."
	@ls -la "../scripts/template-html-with-notes-v2.html" || echo "❌ Template not found in scripts!"
	@mkdir -p $(BUILD_DIR)
	@python3 $(MERGE_NOTES_SCRIPT) $(MAIN_FILE) $(SPEAKER_FILE) $(BUILD_DIR)/$(PRESENTATION_NAME)-speaker.md --notes-type=Speaker
	@pandoc --from markdown --to html -o $(SPEAKER_HTML) --template="template-html-with-notes-v2.html" --data-dir="../scripts" $(BUILD_DIR)/$(PRESENTATION_NAME)-speaker.md
	@echo "✅ Speaker HTML saved to $(SPEAKER_HTML)"

# Published version targets
.PHONY: published published-pptx published-html
published: published-pptx published-html
	@echo "✅ Published version complete!"

published-pptx:
	@echo "📖 Building published PPTX..."
	@mkdir -p $(BUILD_DIR)
	@python3 $(MERGE_NOTES_SCRIPT) $(MAIN_FILE) $(PUBLISHED_FILE) $(BUILD_DIR)/$(PRESENTATION_NAME)-published.md --notes-type=Published
	@sed 's/^---$$/##/' $(BUILD_DIR)/$(PRESENTATION_NAME)-published.md | pandoc --from markdown --to pptx -o $(PUBLISHED_PPTX) --slide-level=1
	@echo "✅ Published PPTX saved to $(PUBLISHED_PPTX)"

published-html:
	@echo "📖 Building published HTML..."
	@echo "🔍 Debug: HTML_TEMPLATE = $(HTML_TEMPLATE)"
	@echo "🔍 Debug: Checking template for published HTML..."
	@ls -la "../scripts/template-html-with-notes-v2.html" || echo "❌ Template not found in scripts!"
	@mkdir -p $(BUILD_DIR)
	@python3 $(MERGE_NOTES_SCRIPT) $(MAIN_FILE) $(PUBLISHED_FILE) $(BUILD_DIR)/$(PRESENTATION_NAME)-published.md --notes-type=Published
	@pandoc --from markdown --to html -o $(PUBLISHED_HTML) --template="template-html-with-notes-v2.html" --data-dir="../scripts" $(BUILD_DIR)/$(PRESENTATION_NAME)-published.md
	@echo "✅ Published HTML saved to $(PUBLISHED_HTML)"

# Development targets
.PHONY: dev dev-speaker dev-published
dev: base-html
	@echo "🚀 Opening base HTML in browser..."
	open $(BASE_HTML)

dev-speaker: speaker-html
	@echo "🚀 Opening speaker HTML in browser..."
	open $(SPEAKER_HTML)

dev-published: published-html
	@echo "🚀 Opening published HTML in browser..."
	open $(PUBLISHED_HTML)

# Utility targets
.PHONY: clean stats validate-slides help
clean:
	@echo "🧹 Cleaning generated files..."
	rm -rf $(BUILD_DIR)

stats:
	@echo "📊 MongoDB Indexing Field Guide Statistics:"
	@echo "   Main slides: $$(grep -c '^# ' $(MAIN_FILE))"
	@echo "   File size: $$(wc -c < $(MAIN_FILE) | tr -d ' ') characters"
	@echo "   Word count: $$(wc -w < $(MAIN_FILE) | tr -d ' ') words"
	@if [ -f $(SPEAKER_FILE) ]; then \
		echo "   Speaker notes: $$(wc -c < $(SPEAKER_FILE) | tr -d ' ') characters"; \
	fi
	@if [ -f $(PUBLISHED_FILE) ]; then \
		echo "   Published notes: $$(wc -c < $(PUBLISHED_FILE) | tr -d ' ') characters"; \
	fi

validate-slides:
	@echo "🔍 Validating slide structure..."
	@if [ ! -f $(MAIN_FILE) ]; then \
		echo "❌ Main file $(MAIN_FILE) not found!"; \
		exit 1; \
	fi
	@echo "✅ Main file exists"
	@if [ ! -f $(SPEAKER_FILE) ]; then \
		echo "⚠️  Speaker file $(SPEAKER_FILE) not found"; \
	else \
		echo "✅ Speaker file exists"; \
	fi
	@if [ ! -f $(PUBLISHED_FILE) ]; then \
		echo "⚠️  Published file $(PUBLISHED_FILE) not found"; \
	else \
		echo "✅ Published file exists"; \
	fi

help:
	@echo "🚀 MongoDB Indexing Field Guide - Build System"
	@echo ""
	@echo "📋 Available targets:"
	@echo "  all            - Build all 6 outputs (base, speaker, published)"
	@echo "  base           - Build base PPTX and HTML"
	@echo "  speaker        - Build speaker PPTX and HTML"
	@echo "  published      - Build published PPTX and HTML"
	@echo ""
	@echo "🎯 Individual targets:"
	@echo "  base-pptx      - Build base PPTX"
	@echo "  base-html      - Build base HTML"
	@echo "  speaker-pptx   - Build speaker PPTX"
	@echo "  speaker-html   - Build speaker HTML"
	@echo "  published-pptx - Build published PPTX"
	@echo "  published-html - Build published HTML"
	@echo ""
	@echo "🔧 Development targets:"
	@echo "  dev            - Build and open base HTML in browser"
	@echo "  dev-speaker    - Build and open speaker HTML in browser"
	@echo "  dev-published  - Build and open published HTML in browser"
	@echo ""
	@echo "🛠️  Utility targets:"
	@echo "  clean          - Clean generated files"
	@echo "  stats          - Show presentation statistics"
	@echo "  validate-slides - Validate slide structure"
	@echo "  help           - Show this help message"
	@echo ""
	@echo "💡 Output files:"
	@echo "  $(BASE_PPTX)"
	@echo "  $(BASE_HTML)"
	@echo "  $(SPEAKER_PPTX)"
	@echo "  $(SPEAKER_HTML)"
	@echo "  $(PUBLISHED_PPTX)"
	@echo "  $(PUBLISHED_HTML)" 