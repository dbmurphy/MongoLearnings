# Makefile for {{GUIDE_TITLE}}
# Builds presentation in multiple formats using Pandoc

PRESENTATION_NAME = {{GUIDE_NAME}}
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
	@mkdir -p $(BUILD_DIR)
	@sed 's/^---$$/#/' $(MAIN_FILE) | pandoc --from markdown --to html -o $(BASE_HTML) --template="$(HTML_TEMPLATE)" --slide-level=1
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
	@mkdir -p $(BUILD_DIR)
	@python3 $(MERGE_NOTES_SCRIPT) $(MAIN_FILE) $(SPEAKER_FILE) $(BUILD_DIR)/$(PRESENTATION_NAME)-speaker.md --notes-type=Speaker
	@pandoc --from markdown --to html -o $(SPEAKER_HTML) --template="$(HTML_TEMPLATE)" $(BUILD_DIR)/$(PRESENTATION_NAME)-speaker.md
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
	@mkdir -p $(BUILD_DIR)
	@python3 $(MERGE_NOTES_SCRIPT) $(MAIN_FILE) $(PUBLISHED_FILE) $(BUILD_DIR)/$(PRESENTATION_NAME)-published.md --notes-type=Published
	@pandoc --from markdown --to html -o $(PUBLISHED_HTML) --template="$(HTML_TEMPLATE)" $(BUILD_DIR)/$(PRESENTATION_NAME)-published.md
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
	@echo "📊 {{GUIDE_TITLE}} Statistics:"
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
	@echo "🚀 {{GUIDE_TITLE}} - Build System"
	@echo ""
	@echo "Available targets:"
	@echo "  all          - Build all 6 outputs (base, speaker, published)"
	@echo "  base         - Build base version (PPTX + HTML)"
	@echo "  speaker      - Build speaker version (PPTX + HTML)"
	@echo "  published    - Build published version (PPTX + HTML)"
	@echo ""
	@echo "Development:"
	@echo "  dev          - Build and open base HTML"
	@echo "  dev-speaker  - Build and open speaker HTML"
	@echo "  dev-published - Build and open published HTML"
	@echo ""
	@echo "Utilities:"
	@echo "  clean        - Remove all generated files"
	@echo "  stats        - Show presentation statistics"
	@echo "  validate-slides - Validate slide structure"
	@echo "  help         - Show this help message"
