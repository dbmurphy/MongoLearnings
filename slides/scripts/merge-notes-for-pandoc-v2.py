#!/usr/bin/env python3
"""
Script to merge speaker or published notes into slides for Pandoc compatibility.
This creates clean markdown with expandable notes for HTML and proper presenter notes for PPTX.
"""

import re
import sys
import argparse
from pathlib import Path

def extract_slides(content):
    """Extract individual slides from markdown content."""
    # Remove frontmatter first
    content_without_frontmatter = re.sub(r'^---\n.*?---\n', '', content, flags=re.DOTALL)
    
    # Split by slide separators (---)
    slides = re.split(r'\n---\n', content_without_frontmatter)
    
    # Filter out empty slides
    filtered_slides = []
    for slide in slides:
        slide = slide.strip()
        if slide:
            filtered_slides.append(slide)
    
    return filtered_slides

def merge_notes_for_pandoc(main_content, notes_content, output_file, notes_type="Speaker"):
    """Merge speaker/published notes into slides for Pandoc format."""
    print(f"Merging {notes_type.lower()} notes for Pandoc...")
    
    # Extract slides from both files
    main_slides = extract_slides(main_content)
    notes_slides = extract_slides(notes_content)
    
    print(f"Found {len(main_slides)} main slides")
    print(f"Found {len(notes_slides)} notes slides")
    
    # Merge slides
    merged_slides = []
    
    for i, main_slide in enumerate(main_slides):
        # Get corresponding notes (if available)
        notes_content_clean = ""
        if i < len(notes_slides):
            notes_content_clean = notes_slides[i].strip()
        
        # Create slide with notes
        if notes_content_clean:
            # Clean up notes content for PPTX compatibility
            # Remove HTML comments
            notes_content_clean = re.sub(r'<!--.*?-->', '', notes_content_clean, flags=re.DOTALL)
            # Convert # headers to ## in notes to avoid slide separation conflicts
            notes_content_fixed = re.sub(r'^# ', '## ', notes_content_clean, flags=re.MULTILINE)
            # Remove extra whitespace and clean up
            notes_content_fixed = re.sub(r'\n\s*\n\s*\n', '\n\n', notes_content_fixed)
            notes_content_fixed = notes_content_fixed.strip()
            
            # For PPTX: Add presenter notes comment
            # For HTML: Add notes section that will be styled by CSS
            merged_slide = f"{main_slide}\n\n::: notes\n{notes_content_fixed}\n:::"
        else:
            merged_slide = main_slide
        
        merged_slides.append(merged_slide)
    
    # Reconstruct the full document with proper slide separators
    frontmatter = re.match(r'^---\n.*?---\n', main_content, re.DOTALL)
    if frontmatter:
        result = frontmatter.group(0) + '\n\n---SLIDE---\n\n'.join(merged_slides)
    else:
        result = '\n\n---SLIDE---\n\n'.join(merged_slides)
    
    # Write the merged result
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)
    
    print(f"✅ Pandoc-compatible slides saved to {output_file}")

def main():
    """Main function to merge notes for Pandoc format."""
    parser = argparse.ArgumentParser(description='Merge speaker or published notes for Pandoc format')
    parser.add_argument('main_file', help='Main markdown file')
    parser.add_argument('notes_file', help='Notes file (speaker.md or published.md)')
    parser.add_argument('output_file', help='Output file')
    parser.add_argument('--notes-type', default='Speaker', choices=['Speaker', 'Published'], 
                       help='Type of notes (Speaker or Published)')
    
    args = parser.parse_args()
    
    # Check if files exist
    if not Path(args.main_file).exists():
        print(f"❌ Main file {args.main_file} not found!")
        sys.exit(1)
    
    if not Path(args.notes_file).exists():
        print(f"❌ Notes file {args.notes_file} not found!")
        sys.exit(1)
    
    # Read files
    with open(args.main_file, 'r', encoding='utf-8') as f:
        main_content = f.read()
    
    with open(args.notes_file, 'r', encoding='utf-8') as f:
        notes_content = f.read()
    
    print(f"📝 Using notes file: {args.notes_file}")
    
    # Merge notes into slides
    merge_notes_for_pandoc(main_content, notes_content, args.output_file, args.notes_type)
    
    print(f"🎉 Successfully merged {args.notes_file} into slides!")
    print(f"📄 Output: {args.output_file}")

if __name__ == "__main__":
    main()
