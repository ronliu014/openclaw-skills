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

**Why openclaw profile?**
- Persistent user data (saves cookies and login state)
- Isolated from your personal Chrome
- Reduces CAPTCHA triggers
- Faster for repeated visits

**Wait time**: 3-5 seconds for complex pages (automatic).

### 2. Capture Page Snapshot

Get page structure and content:

```javascript
browser(action="snapshot", 
        targetId="<tab-id>", 
        snapshotFormat="ai",
        maxChars=20000)
```

**Snapshot format**: Use `ai` format for structured, readable content.

**What's included**:
- Page title and metadata
- Text content hierarchy
- Interactive elements (buttons, links)
- Images with alt text
- Headings and structure

### 3. Extract Content

Parse the snapshot to extract:

**Core elements**:
- **Title**: Main heading (look for `heading [level=1]` or page title)
- **Author**: Often in metadata or byline
- **Date**: Publication or update date
- **Main Content**: Article body (filter out navigation/ads)
- **Images**: URLs and descriptions
- **Links**: Important hyperlinks

**Extraction strategy**:
1. Identify content region (usually `article`, `main`, or specific `generic` blocks)
2. Extract headings in order (h1 → h2 → h3)
3. Collect text content under each heading
4. Filter out navigation, ads, footers
5. Preserve formatting (bold, italic, lists)

### 4. Analyze Structure

Identify page type and structure:

**Common types**:
- **Article/Blog**: Has title, author, date, body text
- **Product Page**: Has price, features, buy button
- **Documentation**: Has navigation, code blocks, examples
- **Social Media**: Has author, timestamp, engagement metrics
- **News Article**: Has headline, byline, publication date
- **Landing Page**: Has hero section, CTA buttons

**Structure indicators**:
```
Article:
- heading [level=1] → Title
- generic → Author/Date
- article/main → Content body

Product:
- heading → Product name
- text → Price
- list → Features
- button → "Add to cart"

Documentation:
- navigation → Sidebar/TOC
- article → Main content
- code blocks → Examples
```

### 5. Generate Summary

Create a structured summary:

**Summary components**:
- **Key points**: 3-5 bullet points (most important info)
- **Main topic**: One-sentence theme
- **Important details**: Dates, numbers, names
- **Actionable information**: What user can do with this info

**Summary strategy**:
1. Extract first paragraph (often contains overview)
2. Identify key sentences (with important keywords)
3. Look for lists or numbered points
4. Extract conclusions or final paragraphs
5. Combine into coherent summary

## Advanced Features

### Screenshot Capture

For visual reference or UI analysis:

```javascript
browser(action="screenshot", 
        targetId="<tab-id>", 
        fullPage=true,
        type="png")
```

**Use cases**:
- Visual design analysis
- UI/UX review
- Capture charts/graphs
- Evidence/documentation

### Scroll and Load More

For infinite scroll or lazy-loaded content:

```javascript
// Scroll to bottom
browser(action="act", 
        targetId="<tab-id>",
        request={
          kind: "evaluate",
          fn: "window.scrollTo(0, document.body.scrollHeight)"
        })

// Wait for content to load
// (add 2-3 second delay)

// Capture new snapshot
browser(action="snapshot", targetId="<tab-id>")
```

### Handle Dynamic Content

For pages with AJAX/dynamic loading:

```javascript
// Wait for specific element
browser(action="act",
        targetId="<tab-id>",
        request={
          kind: "wait",
          text: "Expected content text"
        })
```

### Handle Paywalls/Login

If content is blocked:

**Detection**:
- Look for "Subscribe", "Sign in", "Premium" in snapshot
- Check for overlay/modal elements
- Limited content visible

**Response**:
1. Inform user about the restriction
2. Suggest alternatives:
   - archive.is
   - web.archive.org
   - Reader mode
3. Ask if they have access credentials
4. Offer to try web_fetch (sometimes bypasses)

### Extract Specific Elements

**Code blocks**:
```
Look for: code [ref=eXXX]
Extract: text content
Preserve: formatting and indentation
```

**Tables**:
```
Look for: table [ref=eXXX]
Extract: rows and cells
Format: markdown table
```

**Lists**:
```
Look for: list [ref=eXXX] → listitem
Extract: each item
Format: bullet or numbered list
```

## Output Format

Present extracted information in a clear structure:

```markdown
# [Page Title]

**来源**: [Domain/Site Name]
**作者**: [Author if available]
**日期**: [Date if available]
**类型**: [Article/Product/Documentation/etc.]
**链接**: [URL]

---

## 📝 摘要

- [Key point 1]
- [Key point 2]
- [Key point 3]

---

## 📄 主要内容

### [Section 1 Heading]

[Content paragraph 1]

[Content paragraph 2]

### [Section 2 Heading]

[Content continues...]

---

## 🔗 相关链接

- [Link 1 title]: [URL]
- [Link 2 title]: [URL]

---

## 📊 页面信息

- **字数**: 约 [X] 字
- **图片**: [N] 张
- **外部链接**: [N] 个
- **代码块**: [N] 个（如果有）

---

💡 **提示**: 需要更详细的分析或保存到知识库吗？
```

## Tips & Best Practices

### Performance

- ✅ **Use openclaw profile**: Persistent cookies, faster loading
- ✅ **Reuse tabs**: Don't close tab between analyses
- ✅ **Cache snapshots**: Save for repeated access
- ✅ **Limit maxChars**: Use 15000-20000 for balance

### Reliability

- ✅ **Wait for load**: Complex pages need 3-5 seconds
- ✅ **Check for overlays**: Dismiss cookie notices/popups
- ✅ **Handle errors gracefully**: Fallback to web_fetch
- ✅ **Respect rate limits**: Don't hammer same site

### Quality

- ✅ **Filter noise**: Remove ads, navigation, footers
- ✅ **Preserve structure**: Keep headings and hierarchy
- ✅ **Extract metadata**: Author, date, source
- ✅ **Validate content**: Check if extraction makes sense

### From allwin-video-toolkit Learning

**Persistent user data**:
- openclaw profile saves cookies automatically
- Login state persists across sessions
- Reduces CAPTCHA triggers

**Better waiting**:
- Wait for specific elements, not just time
- Check page load events
- Verify content is actually loaded

**Error handling**:
- Always use try-finally for cleanup
- Close tabs properly
- Handle network timeouts

## Error Handling

### Browser Unavailable

```
❌ 浏览器服务不可用

建议:
1. 尝试使用 web_fetch 工具
2. 重启 OpenClaw gateway
3. 检查浏览器进程
```

### Page Load Timeout

```
⏱️ 页面加载超时

建议:
1. 增加等待时间
2. 检查 URL 是否可访问
3. 尝试存档版本 (archive.is)
```

### Content Blocked

```
🔒 内容被限制访问

检测到: [Paywall/Login/Premium]

建议:
1. 使用 web.archive.org
2. 尝试 Reader 模式
3. 提供登录凭证
```

### Extraction Failed

```
⚠️ 内容提取失败

可能原因:
- 页面结构特殊
- 动态加载未完成
- 反爬虫机制

建议:
1. 尝试 web_fetch
2. 增加等待时间
3. 使用截图查看实际内容
```

## Integration with Other Skills

### web-search
```
搜索 → 选择结果 → web-analyzer 深度分析
```

### summarize
```
web-analyzer 提取 → summarize 深度总结
```

### obsidian
```
web-analyzer 提取 → 保存到知识库
```

### github
```
文档页面 → 提取代码示例 → 保存到项目
```

## Comparison: web-analyzer vs web_fetch

| Feature | web-analyzer | web_fetch |
|---------|--------------|-----------|
| **Method** | Browser automation | HTTP request |
| **JavaScript** | ✅ Executes | ❌ No |
| **Dynamic content** | ✅ Full support | ❌ Limited |
| **Complex pages** | ✅ Excellent | ⚠️ May fail |
| **Speed** | 3-5 seconds | <1 second |
| **Cookies/Login** | ✅ Supported | ❌ No |
| **Screenshots** | ✅ Yes | ❌ No |
| **Resource usage** | Higher | Lower |

**When to use each**:
- **web-analyzer**: Complex pages, dynamic content, need screenshots
- **web_fetch**: Simple pages, fast extraction, no JavaScript needed

## Examples

### Example 1: WeChat Article

```
User: "小贾，帮我读这篇微信文章"

Steps:
1. browser(action="open", profile="openclaw", targetUrl="...")
2. Wait 5 seconds (WeChat loads slowly)
3. browser(action="snapshot", maxChars=20000)
4. Extract: title, author, publish date, content
5. Filter: Remove WeChat UI elements
6. Format: Clean markdown output
```

### Example 2: Technical Documentation

```
User: "分析 FastAPI 文档的这一页"

Steps:
1. Open URL
2. Snapshot with maxChars=25000 (docs are long)
3. Extract: headings, code blocks, examples
4. Identify: API references, parameters
5. Format: Preserve code formatting
```

### Example 3: News Article

```
User: "这篇新闻讲了什么？"

Steps:
1. Open URL
2. Snapshot
3. Extract: headline, byline, date, body
4. Filter: Remove ads, related articles
5. Summarize: Key points in 3-5 bullets
```

### Example 4: Product Page

```
User: "这个产品怎么样？"

Steps:
1. Open URL
2. Snapshot
3. Extract: name, price, features, reviews
4. Analyze: Key selling points
5. Format: Structured product info
```

## Notes

- **Profile choice**: `openclaw` (isolated) vs `chrome` (your browser)
- **Snapshot size**: Balance between completeness and token usage
- **Multiple snapshots**: For very long pages, scroll and capture multiple times
- **Respect robots.txt**: Check if scraping is allowed
- **Rate limiting**: Don't overwhelm servers

## Future Improvements

- [ ] Auto-detect page type
- [ ] Smart content extraction (ML-based)
- [ ] Multi-language support
- [ ] PDF export
- [ ] Batch processing
- [ ] Content comparison (before/after)

---

**Last updated**: 2026-02-27  
**Optimized based on**: allwin-video-toolkit Chrome CDP patterns
