# Makefile for {{GUIDE_TITLE}}
# Builds presentation in multiple formats using MARP

PRESENTATION_NAME = {{GUIDE_NAME}}
MAIN_FILE = $(PRESENTATION_NAME).md
SPEAKER_FILE = speaker.md
PUBLISHED_FILE = published.md
BUILD_DIR = ../build/$(PRESENTATION_NAME)
MERGE_SCRIPT = ../scripts/merge-presentation.py
BUILD_SCRIPT = ../scripts/build-slides.sh

# Default output format (can be overridden with TYPE=html or TYPE=pdf)
TYPE ?= pptx

# Default target
.PHONY: all
all: build

# Build targets
.PHONY: build build-html build-pdf build-pptx
build:
	@echo "🚀 Building $(PRESENTATION_NAME) as $(TYPE)..."
	@$(BUILD_SCRIPT) $(PRESENTATION_NAME) $(BUILD_DIR) $(TYPE)

# Explicit format targets (for convenience)
build-html:
	@$(MAKE) build TYPE=html

build-pdf:
	@$(MAKE) build TYPE=pdf

build-pptx:
	@$(MAKE) build TYPE=pptx

# Speaker mode targets
.PHONY: speaker speaker-html speaker-pdf speaker-pptx
speaker:
	@echo "🎤 Building speaker version as $(TYPE)..."
	@mkdir -p $(BUILD_DIR)
	@echo "📝 Creating merged speaker presentation..."
	python3 $(MERGE_SCRIPT) $(PRESENTATION_NAME) speaker $(BUILD_DIR)/$(PRESENTATION_NAME)-speaker.md
	@echo "🎯 Building $(TYPE) from merged presentation..."
	npx marp $(BUILD_DIR)/$(PRESENTATION_NAME)-speaker.md --$(TYPE) --output $(BUILD_DIR)/$(PRESENTATION_NAME)-speaker.$(TYPE)

# Explicit speaker format targets (for convenience)
speaker-html:
	@$(MAKE) speaker TYPE=html

speaker-pdf:
	@$(MAKE) speaker TYPE=pdf

speaker-pptx:
	@$(MAKE) speaker TYPE=pptx

# Legacy targets for compatibility
build-speaker: speaker
build-speaker-html: speaker-html
build-speaker-pdf: speaker-pdf
build-speaker-pptx: speaker-pptx

# Published mode targets
.PHONY: published published-html published-pdf published-pptx
published:
	@echo "📖 Building published version as $(TYPE)..."
	@mkdir -p $(BUILD_DIR)
	@echo "📝 Creating merged published presentation..."
	python3 $(MERGE_SCRIPT) $(PRESENTATION_NAME) published $(BUILD_DIR)/$(PRESENTATION_NAME)-published.md
	@echo "🎯 Building $(TYPE) from merged presentation..."
	npx marp $(BUILD_DIR)/$(PRESENTATION_NAME)-published.md --$(TYPE) --output $(BUILD_DIR)/$(PRESENTATION_NAME)-published.$(TYPE)

# Explicit published format targets (for convenience)
published-html:
	@$(MAKE) published TYPE=html

published-pdf:
	@$(MAKE) published TYPE=pdf

published-pptx:
	@$(MAKE) published TYPE=pptx

# Legacy targets for compatibility
build-published: published
build-published-html: published-html
build-published-pdf: published-pdf
build-published-pptx: published-pptx

# Development targets
.PHONY: dev dev-speaker dev-published watch preview
dev:
	@$(MAKE) build TYPE=html
	@echo "🚀 Opening $(BUILD_DIR)/$(PRESENTATION_NAME).html in browser..."
	open $(BUILD_DIR)/$(PRESENTATION_NAME).html

dev-speaker:
	@$(MAKE) speaker TYPE=html
	@echo "🚀 Opening $(BUILD_DIR)/$(PRESENTATION_NAME)-speaker.html in browser..."
	open $(BUILD_DIR)/$(PRESENTATION_NAME)-speaker.html

dev-published:
	@$(MAKE) published TYPE=html
	@echo "🚀 Opening $(BUILD_DIR)/$(PRESENTATION_NAME)-published.html in browser..."
	open $(BUILD_DIR)/$(PRESENTATION_NAME)-published.html

watch:
	@echo "👀 Watching for changes and rebuilding..."
	@mkdir -p $(BUILD_DIR)
	npx marp --watch $(MAIN_FILE) --html --output $(BUILD_DIR)/$(PRESENTATION_NAME).html

preview:
	@echo "👁️  Starting preview server..."
	npx marp --preview $(MAIN_FILE)

# Utility targets
.PHONY: install clean stats validate-slides
install:
	@echo "📦 Installing dependencies..."
	npm install

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
		echo "   Published content: $$(wc -c < $(PUBLISHED_FILE) | tr -d ' ') characters"; \
	fi

validate-slides:
	@echo "✅ Validating slide structure..."
	@mkdir -p $(BUILD_DIR)
	@echo "📝 Testing speaker merge..."
	@python3 $(MERGE_SCRIPT) $(PRESENTATION_NAME) speaker $(BUILD_DIR)/$(PRESENTATION_NAME)-speaker.md > /dev/null
	@echo "📝 Testing published merge..."
	@python3 $(MERGE_SCRIPT) $(PRESENTATION_NAME) published $(BUILD_DIR)/$(PRESENTATION_NAME)-published.md > /dev/null
	@echo "✅ All slide validations passed!"

help:
	@echo "{{GUIDE_TITLE}} Build System"
	@echo ""
	@echo "🎯 Primary targets (default: TYPE=pptx):"
	@echo "  build                  - Build presentation (default: pptx)"
	@echo "  speaker                - Build speaker version (default: pptx)"
	@echo "  published              - Build published version (default: pptx)"
	@echo ""
	@echo "🔧 Format control:"
	@echo "  TYPE=html              - Override to HTML format"
	@echo "  TYPE=pdf               - Override to PDF format"
	@echo "  TYPE=pptx              - Explicit PowerPoint format"
	@echo ""
	@echo "📋 Examples:"
	@echo "  make build             - Build PowerPoint presentation"
	@echo "  make build TYPE=html   - Build HTML presentation"
	@echo "  make speaker           - Build speaker PowerPoint"
	@echo "  make speaker TYPE=pdf  - Build speaker PDF"
	@echo "  make published TYPE=html - Build published HTML"
	@echo ""
	@echo "🚀 Development targets:"
	@echo "  dev                    - Build HTML and open in browser"
	@echo "  dev-speaker            - Build speaker HTML and open"
	@echo "  dev-published          - Build published HTML and open"
	@echo "  watch                  - Watch for changes and rebuild"
	@echo "  preview                - Start MARP preview server"
	@echo ""
	@echo "🛠️ Utility targets:"
	@echo "  install                - Install dependencies"
	@echo "  clean                  - Remove build directory"
	@echo "  stats                  - Show presentation statistics"
	@echo "  validate-slides        - Validate slide structure"
	@echo "  help                   - Show this help" 