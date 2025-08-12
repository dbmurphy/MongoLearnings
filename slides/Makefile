# Parent Makefile for all MongoDB Learning Guides
# Orchestrates builds across multiple guide directories

# Find all guide directories (only those ending with "-guide")
GUIDE_DIRS := $(wildcard *-guide/. )
GUIDE_NAMES := $(patsubst %/.,%,$(filter-out scripts/. template/. build/.,$(GUIDE_DIRS)))
# Filter to only include folders that end with "-guide"
GUIDE_NAMES := $(filter %-guide,$(GUIDE_NAMES))

# Default target - builds all guides
.PHONY: all
all: build-all
	@echo "🎉 All guides built successfully!"

# Build all guides
.PHONY: build-all
build-all:
	@echo "🚀 Building all guides..."
	@for guide in $(GUIDE_NAMES); do \
		echo "📚 Building $$guide..."; \
		$(MAKE) -C $$guide all; \
		echo "✅ $$guide complete!"; \
		echo ""; \
	done

# GitHub Pages deployment targets
.PHONY: github-pages
github-pages: build-all
	@echo "🌐 Preparing GitHub Pages deployment..."
	@mkdir -p docs
	@echo "📁 Copying HTML files to docs/..."
	@for guide in $(GUIDE_NAMES); do \
		echo "📚 Copying $$guide files..."; \
		mkdir -p docs/$$guide; \
		cp build/$$guide/*.html docs/$$guide/; \
	done
	@echo "📝 Generating dynamic index.html..."
	@python3 scripts/generate-index.py
	@echo "✅ GitHub Pages files ready in docs/ directory!"

.PHONY: generate-index
generate-index:
	@echo "📝 Generating dynamic index.html..."
	@python3 scripts/generate-index.py

.PHONY: deploy-pages
deploy-pages: github-pages
	@echo "🚀 Deploying to GitHub Pages..."
	@echo "📝 Commit and push changes to trigger deployment:"
	@echo "   git add docs/"
	@echo "   git commit -m 'Update GitHub Pages'"
	@echo "   git push origin main"

# Build specific guide
.PHONY: build-guide
build-guide:
	@if [ -z "$(GUIDE)" ]; then \
		echo "❌ Please specify GUIDE=guide-name"; \
		echo "Available guides: $(GUIDE_NAMES)"; \
		exit 1; \
	fi
	@if [ ! -d "$(GUIDE)" ]; then \
		echo "❌ Guide '$(GUIDE)' not found!"; \
		echo "Available guides: $(GUIDE_NAMES)"; \
		exit 1; \
	fi
	@echo "🚀 Building $(GUIDE)..."
	@$(MAKE) -C $(GUIDE) all

# Build base versions of all guides
.PHONY: base-all
base-all:
	@echo "🚀 Building base versions of all guides..."
	@for guide in $(GUIDE_NAMES); do \
		echo "📚 Building base version of $$guide..."; \
		$(MAKE) -C $$guide base; \
		echo "✅ $$guide base complete!"; \
		echo ""; \
	done

# Build speaker versions of all guides
.PHONY: speaker-all
speaker-all:
	@echo "🎤 Building speaker versions of all guides..."
	@for guide in $(GUIDE_NAMES); do \
		echo "📚 Building speaker version of $$guide..."; \
		$(MAKE) -C $$guide speaker; \
		echo "✅ $$guide speaker complete!"; \
		echo ""; \
	done

# Build published versions of all guides
.PHONY: published-all
published-all:
	@echo "📖 Building published versions of all guides..."
	@for guide in $(GUIDE_NAMES); do \
		echo "📚 Building published version of $$guide..."; \
		$(MAKE) -C $$guide published; \
		echo "✅ $$guide published complete!"; \
		echo ""; \
	done

# Development targets
.PHONY: dev-all dev-base-all dev-speaker-all dev-published-all
dev-all:
	@echo "🚀 Opening all guide HTML files in browser..."
	@for guide in $(GUIDE_NAMES); do \
		echo "📚 Opening $$guide base HTML..."; \
		$(MAKE) -C $$guide dev; \
	done

dev-base-all:
	@echo "🚀 Opening base HTML files in browser..."
	@for guide in $(GUIDE_NAMES); do \
		echo "📚 Opening $$guide base HTML..."; \
		$(MAKE) -C $$guide dev; \
	done

dev-speaker-all:
	@echo "🎤 Opening speaker HTML files in browser..."
	@for guide in $(GUIDE_NAMES); do \
		echo "📚 Opening $$guide speaker HTML..."; \
		$(MAKE) -C $$guide dev-speaker; \
	done

dev-published-all:
	@echo "📖 Opening published HTML files in browser..."
	@for guide in $(GUIDE_NAMES); do \
		echo "📚 Opening $$guide published HTML..."; \
		$(MAKE) -C $$guide dev-published; \
	done

# Utility targets
.PHONY: clean clean-all stats stats-all validate validate-all help
clean: clean-all

clean-all:
	@echo "🧹 Cleaning all guide build directories..."
	@for guide in $(GUIDE_NAMES); do \
		echo "🧹 Cleaning $$guide..."; \
		$(MAKE) -C $$guide clean; \
	done
	@echo "✅ All guides cleaned!"

stats: stats-all

stats-all:
	@echo "📊 Statistics for all guides:"
	@echo ""
	@for guide in $(GUIDE_NAMES); do \
		echo "📚 $$guide:"; \
		$(MAKE) -C $$guide stats; \
		echo ""; \
	done

validate: validate-all

validate-all:
	@echo "🔍 Validating all guide structures..."
	@for guide in $(GUIDE_NAMES); do \
		echo "🔍 Validating $$guide..."; \
		$(MAKE) -C $$guide validate-slides; \
		echo ""; \
	done

# List available guides
.PHONY: list-guides
list-guides:
	@echo "📚 Available guides:"
	@for guide in $(GUIDE_NAMES); do \
		echo "  • $$guide"; \
	done
	@echo ""
	@echo "💡 To build a specific guide: make build-guide GUIDE=guide-name"

# Check system requirements
.PHONY: check-requirements
check-requirements:
	@echo "🔍 Checking system requirements..."
	@if ! command -v pandoc >/dev/null 2>&1; then \
		echo "❌ Pandoc not found! Please install Pandoc:"; \
		echo "   macOS: brew install pandoc"; \
		echo "   Ubuntu: sudo apt-get install pandoc"; \
		echo "   Windows: https://pandoc.org/installing.html"; \
		exit 1; \
	else \
		echo "✅ Pandoc found: $$(pandoc --version | head -1)"; \
	fi
	@if ! command -v python3 >/dev/null 2>&1; then \
		echo "❌ Python 3 not found! Please install Python 3"; \
		exit 1; \
	else \
		echo "✅ Python 3 found: $$(python3 --version)"; \
	fi
	@echo "✅ All requirements met!"

help:
	@echo "🚀 MongoDB Learning Guides - Parent Build System"
	@echo ""
	@echo "📋 Available guides:"
	@for guide in $(GUIDE_NAMES); do \
		echo "  • $$guide"; \
	done
	@echo ""
	@echo "🎯 Primary targets:"
	@echo "  all              - Build all guides (all 6 outputs each)"
	@echo "  build-guide      - Build specific guide (use GUIDE=name)"
	@echo "  base-all         - Build base versions of all guides"
	@echo "  speaker-all      - Build speaker versions of all guides"
	@echo "  published-all    - Build published versions of all guides"
	@echo ""
	@echo "🔧 Development targets:"
	@echo "  dev-all          - Open all guide HTML files in browser"
	@echo "  dev-base-all     - Open base HTML files in browser"
	@echo "  dev-speaker-all  - Open speaker HTML files in browser"
	@echo "  dev-published-all - Open published HTML files in browser"
	@echo ""
	@echo "🛠️  Utility targets:"
	@echo "  clean            - Clean all guide build directories"
	@echo "  stats            - Show statistics for all guides"
	@echo "  validate         - Validate all guide structures"
	@echo "  list-guides      - List available guides"
	@echo "  check-requirements - Check system requirements"
	@echo "  help             - Show this help message"
	@echo ""
	@echo "💡 Usage examples:"
	@echo "  make all                           - Build all guides"
	@echo "  make build-guide GUIDE=mongodb-indexing-field-guide"
	@echo "  make base-all                      - Build base versions only"
	@echo "  make dev-speaker-all               - Open speaker HTML files"
	@echo ""
	@echo "📁 Output structure:"
	@echo "  build/guide-name/"
	@echo "  ├── guide-name.pptx              (base PPTX)"
	@echo "  ├── guide-name.html              (base HTML)"
	@echo "  ├── guide-name-speaker.pptx      (speaker PPTX)"
	@echo "  ├── guide-name-speaker.html      (speaker HTML)"
	@echo "  ├── guide-name-published.pptx    (published PPTX)"
	@echo "  └── guide-name-published.html    (published HTML)" 