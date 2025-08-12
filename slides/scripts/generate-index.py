#!/usr/bin/env python3
"""
Script to generate index.html for GitHub Pages based on available guides.
This creates a dynamic landing page that automatically includes all built guides.
"""

import os
import re
import sys
from pathlib import Path

def extract_guide_info(guide_dir):
    """Extract guide information from README.md and guide files."""
    guide_name = guide_dir.name
    guide_path = guide_dir
    
    # Default values
    info = {
        'name': guide_name.replace('-', ' ').title(),
        'duration': 'Duration: TBD',
        'description': 'Technical guide covering MongoDB performance optimization.',
        'has_base': False,
        'has_speaker': False,
        'has_published': False
    }
    
    # Try to read README.md for guide info
    readme_path = guide_path / 'README.md'
    if readme_path.exists():
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Extract duration
            duration_match = re.search(r'Duration:\s*(~?\d+-\d+\s*minutes?.*?)(?:\n|$)', content, re.IGNORECASE)
            if duration_match:
                info['duration'] = duration_match.group(1).strip()
            
            # Extract description (look for coverage section)
            coverage_match = re.search(r'Coverage:.*?\n(.*?)(?:\n\n|\n##|\n###|$)', content, re.DOTALL | re.IGNORECASE)
            if coverage_match:
                description = coverage_match.group(1).strip()
                # Clean up the description
                description = re.sub(r'^\s*[-•*]\s*', '', description, flags=re.MULTILINE)
                description = re.sub(r'\n\s*[-•*]\s*', ' ', description)
                description = re.sub(r'\s+', ' ', description).strip()
                if description and len(description) > 50:
                    info['description'] = description[:200] + '...' if len(description) > 200 else description
    
    # Check which HTML files exist in build directory
    build_path = Path('build') / guide_name
    if build_path.exists():
        html_files = list(build_path.glob('*.html'))
        for html_file in html_files:
            filename = html_file.name
            if '-speaker.' in filename:
                info['has_speaker'] = True
            elif '-published.' in filename:
                info['has_published'] = True
            else:
                info['has_base'] = True
    
    return info

def generate_index_html(guides_info):
    """Generate the index.html content using template."""
    
    # Create guide cards HTML
    guide_cards = []
    for guide_name, info in guides_info.items():
        card_html = f'''
        <div class="guide-card">
            <div class="guide-title">📖 {info['name']}</div>
            <div class="guide-duration">{info['duration']}</div>
            <div class="guide-description">
                {info['description']}
            </div>
            <div class="guide-links">'''
        
        # Add links for available versions
        if info['has_base']:
            card_html += f'''
                <a href="./{guide_name}/{guide_name}.html" class="btn btn-primary">View Base Version</a>'''
        
        if info['has_speaker']:
            card_html += f'''
                <a href="./{guide_name}/{guide_name}-speaker.html" class="btn btn-secondary">Speaker Notes</a>'''
        
        if info['has_published']:
            card_html += f'''
                <a href="./{guide_name}/{guide_name}-published.html" class="btn btn-secondary">Published Notes</a>'''
        
        card_html += '''
            </div>
        </div>'''
        
        guide_cards.append(card_html)
    
    # Read template
    template_path = Path('template/index-template.html')
    if template_path.exists():
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()
    else:
        # Fallback template if template file doesn't exist
        template_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{SITE_TITLE}}</title>
    <style>
        body { font-family: -apple-system, sans-serif; max-width: 1200px; margin: 0 auto; padding: 2rem; }
        .header { text-align: center; margin-bottom: 3rem; }
        .guides-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 2rem; }
        .guide-card { background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .btn { padding: 0.5rem 1rem; border-radius: 6px; text-decoration: none; margin: 0.25rem; }
        .btn-primary { background: #3498db; color: white; }
        .btn-secondary { background: #ecf0f1; color: #2c3e50; }
    </style>
</head>
<body>
    <div class="header">
        <h1>{{HEADER_TITLE}}</h1>
        <p>{{HEADER_DESCRIPTION}}</p>
    </div>
    <div class="guides-grid">{{GUIDE_CARDS}}</div>
    <div style="text-align: center; margin-top: 3rem;">
        <p>{{FOOTER_TEXT}}</p>
        <p><a href="{{GITHUB_URL}}">View on GitHub</a></p>
    </div>
</body>
</html>'''
    
    # Replace template variables
    html_content = template_content.replace('{{SITE_TITLE}}', 'MongoDB Performance Guides')
    html_content = html_content.replace('{{SITE_DESCRIPTION}}', 'A comprehensive collection of in-depth field guides covering MongoDB performance optimization for Node.js/Mongoose developers.')
    html_content = html_content.replace('{{SITE_URL}}', 'https://yourusername.github.io/MongoLearnings/')
    html_content = html_content.replace('{{HEADER_TITLE}}', '📚 MongoDB Performance Guides')
    html_content = html_content.replace('{{HEADER_DESCRIPTION}}', 'A comprehensive collection of in-depth field guides covering MongoDB performance optimization for Node.js/Mongoose developers.')
    html_content = html_content.replace('{{GUIDE_CARDS}}', ''.join(guide_cards))
    html_content = html_content.replace('{{FOOTER_TEXT}}', 'Built with ❤️ using Pandoc and custom HTML templates')
    html_content = html_content.replace('{{GITHUB_URL}}', 'https://github.com/yourusername/MongoLearnings')
    
    return html_content

def main():
    """Main function to generate index.html."""
    # Find all guide directories
    guide_dirs = []
    for item in Path('.').iterdir():
        if item.is_dir() and item.name.endswith('-guide'):
            guide_dirs.append(item)
    
    if not guide_dirs:
        print("❌ No guide directories found!")
        sys.exit(1)
    
    print(f"📚 Found {len(guide_dirs)} guide directories")
    
    # Extract information from each guide
    guides_info = {}
    for guide_dir in guide_dirs:
        print(f"🔍 Processing {guide_dir.name}...")
        guides_info[guide_dir.name] = extract_guide_info(guide_dir)
    
    # Generate the index.html content
    print("📝 Generating index.html...")
    index_content = generate_index_html(guides_info)
    
    # Write to docs/index.html
    docs_dir = Path('docs')
    docs_dir.mkdir(exist_ok=True)
    
    index_path = docs_dir / 'index.html'
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print(f"✅ Generated index.html with {len(guides_info)} guides")
    print(f"📁 Saved to {index_path}")
    
    # Print summary
    for guide_name, info in guides_info.items():
        versions = []
        if info['has_base']:
            versions.append('base')
        if info['has_speaker']:
            versions.append('speaker')
        if info['has_published']:
            versions.append('published')
        
        print(f"  📖 {guide_name}: {', '.join(versions) if versions else 'no HTML files'}")

if __name__ == '__main__':
    main()
