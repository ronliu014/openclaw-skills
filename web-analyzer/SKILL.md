---
name: web-analyzer
description: Analyze web pages with deep content extraction and structure analysis. Use when user asks to read, analyze, or extract information from web pages (especially complex pages like WeChat articles, news sites, blogs). Supports text extraction, image detection, structure analysis, and intelligent summarization. Ideal for pages that web_fetch cannot fully extract.
---

# Web Analyzer

Deep web page analysis and content extraction using browser automation.

## When to Use

Use this skill when:
- User asks to read or analyze a web page
- `web_fetch` fails to extract complete content
- Need to analyze page structure or layout
- Working with dynamic content (JavaScript-rendered pages)
- Extracting from complex pages (WeChat articles, Medium, Substack, etc.)
- Need screenshots or visual analysis

## Quick Start

Basic usage:
```
"小贾，帮我分析这个网页：[URL]"
"小贾，读取这篇文章的内容：[URL]"
"小贾，提取这个页面的关键信息：[URL]"
```

## Workflow

### 1. Open the Page

Use browser tool to open the target URL:

```javascript
browser(action="open", profile="openclaw", targetUrl="<URL>")
```

Wait for page to fully load (3-5 seconds for complex pages).

### 2. Capture Page Snapshot

Get page structure and content:

```javascript
browser(action="snapshot", targetId="<tab-id>", snapshotFormat="ai")
```

The snapshot includes:
- Page title and metadata
- Text content hierarchy
- Interactive elements
- Links and images

### 3. Extract Content

Parse the snapshot to extract:
- **Title**: Main heading or page title
- **Author**: If available (common in articles)
- **Date**: Publication or update date
- **Main Content**: Article body, removing navigation/ads
- **Images**: URLs and alt text
- **Links**: Important hyperlinks

### 4. Analyze Structure

Identify page type and structure:
- Article/Blog post
- Product page
- Documentation
- Social media post
- News article
- Landing page

### 5. Generate Summary

Create a structured summary:
- Key points (3-5 bullet points)
- Main topic/theme
- Important details
- Actionable information

## Advanced Features

### Screenshot Capture

For visual reference:

```javascript
browser(action="screenshot", targetId="<tab-id>", fullPage=true)
```

### Scroll and Load More

For infinite scroll pages:

```javascript
browser(action="act", request={
  kind: "evaluate",
  fn: "window.scrollTo(0, document.body.scrollHeight)"
})
```

Wait and snapshot again to capture loaded content.

### Handle Paywalls/Login

If content is blocked:
1. Inform user about the restriction
2. Suggest alternatives (archive.is, web.archive.org)
3. Ask if they have access credentials

## Output Format

Present extracted information in a clear structure:

```markdown
# [Page Title]

**来源**: [Domain/Site Name]
**作者**: [Author if available]
**日期**: [Date if available]
**链接**: [URL]

## 摘要

[3-5 key points in bullet format]

## 主要内容

[Extracted main content, cleaned and formatted]

## 关键信息

- **类型**: [Article/Product/Documentation/etc.]
- **字数**: [Approximate word count]
- **图片**: [Number of images]
- **链接**: [Number of external links]

## 相关链接

[Important links mentioned in the content]
```

## Tips

- **Wait for load**: Complex pages need 3-5 seconds to fully render
- **Check for popups**: Dismiss cookie notices or overlays if they block content
- **Multiple snapshots**: For long pages, may need to scroll and snapshot multiple times
- **Fallback to web_fetch**: If browser is unavailable, try web_fetch first
- **Cache results**: For repeated analysis, save extracted content to avoid re-fetching

## Error Handling

**Browser unavailable**:
- Try `web_fetch` as fallback
- Inform user browser service is down
- Suggest restarting OpenClaw gateway

**Page load timeout**:
- Increase wait time
- Check if URL is accessible
- Try alternative URL (archive, cached version)

**Content blocked**:
- Check for paywalls or login requirements
- Look for "reader mode" or simplified version
- Suggest user provides access or alternative source

## Examples

### Example 1: WeChat Article

```
User: "小贾，帮我读这篇文章：https://mp.weixin.qq.com/s/xxxxx"

Steps:
1. Open URL in browser
2. Wait 5 seconds (WeChat articles load slowly)
3. Snapshot page
4. Extract title, author, content
5. Present formatted summary
```

### Example 2: Technical Blog

```
User: "分析这个技术博客的内容"

Steps:
1. Open URL
2. Snapshot
3. Identify code blocks and technical terms
4. Extract main concepts
5. Summarize with technical focus
```

### Example 3: Product Page

```
User: "这个产品页面有什么信息？"

Steps:
1. Open URL
2. Snapshot
3. Extract product name, price, features
4. Identify key selling points
5. Present structured product info
```

## Integration with Other Skills

- **summarize**: Use for deeper content analysis
- **obsidian**: Save extracted content to knowledge base
- **github**: Extract code snippets from documentation

## Notes

- Browser profile "openclaw" is isolated; "chrome" uses your actual Chrome
- Snapshots are text-based; use screenshot for visual capture
- Large pages may need multiple snapshots
- Respect robots.txt and rate limits
