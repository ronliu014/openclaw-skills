#!/usr/bin/env python3
"""
Extract and clean content from browser snapshot data.
Helps parse the AI-format snapshot into structured content.
"""

import json
import re
import sys
from typing import Dict, List, Optional


def extract_text_from_snapshot(snapshot_text: str) -> Dict[str, any]:
    """
    Parse browser snapshot and extract structured content.
    
    Args:
        snapshot_text: Raw snapshot text from browser tool
        
    Returns:
        Dictionary with extracted content:
        - title: Page title
        - author: Author if found
        - date: Publication date if found
        - content: Main text content
        - links: List of important links
        - images: List of image references
    """
    result = {
        'title': '',
        'author': '',
        'date': '',
        'content': [],
        'links': [],
        'images': [],
        'metadata': {}
    }
    
    lines = snapshot_text.split('\n')
    
    # Extract title (usually first heading)
    for line in lines:
        if 'heading' in line and 'level=1' in line:
            # Extract text between quotes
            match = re.search(r'heading "([^"]+)"', line)
            if match:
                result['title'] = match.group(1)
                break
    
    # Extract author and date
    for line in lines:
        if 'author' in line.lower() or '作者' in line:
            match = re.search(r'"([^"]+)"', line)
            if match:
                result['author'] = match.group(1)
        
        if 'date' in line.lower() or '日期' in line or '时间' in line:
            match = re.search(r'"([^"]+)"', line)
            if match:
                result['date'] = match.group(1)
    
    # Extract paragraphs
    current_section = []
    for line in lines:
        if 'paragraph' in line:
            match = re.search(r'paragraph.*?: (.+)', line)
            if match:
                text = match.group(1).strip()
                # Clean up text
                text = text.replace('\\\"', '"')
                if text and text not in ['', '\\n']:
                    current_section.append(text)
        
        elif 'heading' in line and 'level=2' in line:
            if current_section:
                result['content'].append('\n'.join(current_section))
                current_section = []
            match = re.search(r'heading "([^"]+)"', line)
            if match:
                result['content'].append(f"\n## {match.group(1)}\n")
        
        elif 'heading' in line and 'level=3' in line:
            match = re.search(r'heading "([^"]+)"', line)
            if match:
                result['content'].append(f"\n### {match.group(1)}\n")
    
    if current_section:
        result['content'].append('\n'.join(current_section))
    
    # Extract links
    for line in lines:
        if 'link' in line and '/url:' in line:
            link_match = re.search(r'link "([^"]+)".*?/url: (.+)', line)
            if link_match:
                result['links'].append({
                    'text': link_match.group(1),
                    'url': link_match.group(2).strip()
                })
    
    # Extract images
    for line in lines:
        if 'img' in line:
            img_match = re.search(r'img "([^"]+)"', line)
            if img_match:
                result['images'].append(img_match.group(1))
    
    return result


def format_output(data: Dict[str, any], url: str = '') -> str:
    """
    Format extracted data into readable markdown.
    
    Args:
        data: Extracted content dictionary
        url: Original URL
        
    Returns:
        Formatted markdown string
    """
    output = []
    
    # Title
    if data['title']:
        output.append(f"# {data['title']}\n")
    
    # Metadata
    output.append("**元信息**:")
    if url:
        output.append(f"- **链接**: {url}")
    if data['author']:
        output.append(f"- **作者**: {data['author']}")
    if data['date']:
        output.append(f"- **日期**: {data['date']}")
    output.append("")
    
    # Main content
    if data['content']:
        output.append("## 主要内容\n")
        output.extend(data['content'])
        output.append("")
    
    # Links
    if data['links']:
        output.append("## 相关链接\n")
        for link in data['links'][:10]:  # Limit to first 10 links
            output.append(f"- [{link['text']}]({link['url']})")
        output.append("")
    
    # Images
    if data['images']:
        output.append(f"## 图片信息\n")
        output.append(f"页面包含 {len(data['images'])} 张图片")
        output.append("")
    
    return '\n'.join(output)


def main():
    """CLI entry point."""
    if len(sys.argv) < 2:
        print("Usage: python extract_content.py <snapshot_file>")
        print("   or: python extract_content.py <snapshot_file> <url>")
        sys.exit(1)
    
    snapshot_file = sys.argv[1]
    url = sys.argv[2] if len(sys.argv) > 2 else ''
    
    try:
        with open(snapshot_file, 'r', encoding='utf-8') as f:
            snapshot_text = f.read()
        
        data = extract_text_from_snapshot(snapshot_text)
        output = format_output(data, url)
        
        print(output)
        
    except FileNotFoundError:
        print(f"Error: File '{snapshot_file}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
