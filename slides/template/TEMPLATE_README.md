# 📋 Presentation Template Guide

This template provides a complete framework for creating new presentation guides with consistent structure and tooling.

## 🎯 Template Overview

The template includes:
- **Main presentation** (`{{GUIDE_NAME}}.md`) - Core slide content
- **Speaker notes** (`speaker.md`) - Presenter talking points and stories
- **Published guide** (`published.md`) - Comprehensive learning transcript
- **Build system** (`Makefile`, `package.json`) - Multi-format generation with shared scripts
- **Documentation** (`README.md`) - Guide-specific information
- **Configuration** (`.gitignore`) - Project cleanup rules

## 🔄 Creating a New Guide

### Step 1: Copy Template
```bash
# From the slides/ directory
make new-guide GUIDE_NAME=your-new-guide-name
```

### Step 2: Replace Placeholders

All template files contain placeholders in the format `{{PLACEHOLDER_NAME}}`. Replace these with your specific content:

#### Core Identity Placeholders
- `{{GUIDE_NAME}}` - Kebab-case name (e.g., "mongodb-sharding-guide")
- `{{GUIDE_TITLE}}` - Human-readable title (e.g., "MongoDB Sharding Guide")
- `{{GUIDE_DESCRIPTION}}` - One-line description for the guide
- `{{GUIDE_TOPIC}}` - Main topic area (e.g., "MongoDB Sharding")
- `{{GUIDE_HEADER}}` - MARP header text for slides
- `{{GUIDE_FOOTER}}` - MARP footer text for slides

#### Content Structure Placeholders
- `{{TARGET_AUDIENCE}}` - Who should attend (e.g., "Node.js developers")
- `{{PREREQUISITES}}` - Required knowledge (e.g., "Basic MongoDB knowledge")
- `{{DURATION}}` - Estimated presentation time (e.g., "45-60 minutes")
- `{{CODE_LANGUAGE}}` - Primary language for code examples (e.g., "javascript")

#### Topic Areas (Main Content)
- `{{TOPIC_AREA_1}}`, `{{TOPIC_AREA_2}}`, `{{TOPIC_AREA_3}}` - Major content sections
- `{{MAIN_FEATURE}}` - Central technology/concept being discussed
- `{{SKILL_1}}` through `{{SKILL_9}}` - Specific skills covered
- `{{APPLICATION_1}}` through `{{APPLICATION_3}}` - Real-world applications

#### Technical Content
- `{{PROCESS_STEP_1}}` through `{{PROCESS_STEP_4}}` - Key process steps
- `{{CODE_EXAMPLE}}` - Main code demonstration
- `{{EXAMPLE_TITLE}}` - Title for code example
- `{{IMPACT_1}}` through `{{IMPACT_3}}` - Performance/feature impacts

#### Learning Outcomes
- `{{TAKEAWAY_1}}` through `{{TAKEAWAY_6}}` - Key learning points
- `{{PRINCIPLE_CATEGORY_1}}` through `{{PRINCIPLE_CATEGORY_3}}` - Principle groupings
- `{{ACTION_1}}` through `{{ACTION_3}}` - Immediate action items
- `{{ACTION_1_DESCRIPTION}}` through `{{ACTION_3_DESCRIPTION}}` - Action details

#### Discussion & Engagement
- `{{DISCUSSION_1}}` through `{{DISCUSSION_3}}` - Discussion topics
- `{{EXPERIENCE_1}}`, `{{EXPERIENCE_2}}` - Experience sharing prompts
- `{{CHALLENGE_1}}`, `{{CHALLENGE_2}}` - Common challenges
- `{{OPENING_HOOK}}` - Engaging opening statement
- `{{AUDIENCE_ENGAGEMENT}}` - Audience connection strategy
- `{{SESSION_PROMISE}}` - What attendees will gain

#### Resources & References
- `{{RESOURCE_1}}`, `{{RESOURCE_2}}` - Official documentation links
- `{{RESOURCE_1_URL}}`, `{{RESOURCE_2_URL}}` - Resource URLs
- `{{COMMUNITY_RESOURCE_1}}`, `{{COMMUNITY_RESOURCE_2}}` - Community links
- `{{TOOL_1}}`, `{{TOOL_2}}` - Recommended tools
- `{{TOOL_1_URL}}`, `{{TOOL_2_URL}}` - Tool URLs
- `{{TOOL_1_DESCRIPTION}}`, `{{TOOL_2_DESCRIPTION}}` - Tool descriptions
- `{{ADVANCED_TOPIC_1}}`, `{{ADVANCED_TOPIC_2}}` - Advanced learning areas

#### Project Metadata
- `{{AUTHOR_NAME}}` - Author/presenter name
- `{{LICENSE}}` - License type (e.g., "MIT")
- `{{REPOSITORY_URL}}` - Git repository URL
- `{{ISSUES_URL}}` - Issues/bug tracking URL
- `{{HOMEPAGE_URL}}` - Project homepage URL
- `{{PROJECT_NAME}}` - Overall project name
- `{{KEYWORD_1}}`, `{{KEYWORD_2}}`, `{{KEYWORD_3}}` - NPM keywords

#### Detailed Content (for published.md)
- `{{DETAILED_INTRODUCTION}}` - Comprehensive introduction
- `{{COMPREHENSIVE_COVERAGE}}` - What the guide covers in detail
- `{{LEARNING_METHODOLOGY}}` - How the content is structured
- `{{DETAILED_OUTCOMES}}` - Comprehensive learning outcomes
- `{{MASTERY_EXPLANATION}}` - Mastery framework explanation
- `{{DETAILED_SKILL_1}}` through `{{DETAILED_SKILL_9}}` - Skill explanations
- `{{COMPREHENSIVE_OVERVIEW}}` - Technical deep dive overview
- `{{ARCHITECTURAL_EXPLANATION}}` - Architecture details
- `{{PERFORMANCE_ANALYSIS}}` - Performance characteristics
- `{{USE_CASE_ANALYSIS}}` - Use case analysis

## 🛠️ Quick Replacement Strategy

### Using find/replace (recommended):
1. Open the new guide directory in your editor
2. Use "Find and Replace All" across all files
3. Replace each `{{PLACEHOLDER}}` systematically
4. Start with core identity placeholders first

### Using sed (command line):
```bash
# Example: Replace guide name across all files
find . -type f -name "*.md" -o -name "*.json" -o -name "Makefile" | \
  xargs sed -i '' 's/{{GUIDE_NAME}}/your-guide-name/g'
```

## 📝 Content Development Tips

### Main Presentation (`{{GUIDE_NAME}}.md`)
- Keep slides focused and visual
- Use consistent emoji themes
- Include practical code examples
- End with clear action items

### Speaker Notes (`speaker.md`)
- Add personal stories and examples
- Include timing guidance
- Note potential audience questions
- Add enthusiasm and energy cues

### Published Guide (`published.md`)
- Provide comprehensive explanations
- Include detailed background context
- Add troubleshooting information
- Link to additional resources

## ✅ Validation Checklist

After replacing placeholders:

- [ ] All `{{PLACEHOLDER}}` instances replaced
- [ ] File names updated (rename `{{GUIDE_NAME}}.md`)
- [ ] Code examples work and are tested
- [ ] Links are valid and accessible
- [ ] Slide counts match between main/speaker/published
- [ ] Make targets work correctly
- [ ] NPM scripts function properly

## 🚀 Testing Your New Guide

```bash
# Test the build system
make install
make build
make validate-slides

# Test development workflow
make dev
make dev-speaker
make dev-published

# Check statistics
make stats
```

## 🎨 Customization Options

### Themes
Modify the MARP theme in the frontmatter:
```yaml
theme: default  # or gaia, uncover, etc.
backgroundColor: #1e1e1e
color: #ffffff
```

### Slide Structure
Add more slides by:
1. Adding content to main presentation
2. Adding corresponding speaker notes
3. Adding detailed published content
4. Ensuring slide numbers align

### Build Targets
Extend the Makefile for custom formats or deployment targets.

---

**This template system ensures consistency across all presentation guides while providing flexibility for diverse content types.**

## 🎯 Build System

The template uses **Pandoc** for building presentations, which provides:

- **Base, speaker, and published versions** - Three different output formats
- **Custom HTML templates** - Responsive presentations with expandable notes
- **PPTX output** - PowerPoint files with presenter notes
- **GitHub Pages integration** - Automatic deployment support
- **Advanced features** - Better slide processing and note merging

### Key Features
- **Presenter Notes**: Speaker and published notes appear in PowerPoint's presenter notes section
- **Interactive HTML**: Slide navigation with expandable notes sections
- **Cross-Platform**: Works on macOS, Linux, and Windows
- **Automated Builds**: Single command builds all guides in all formats 