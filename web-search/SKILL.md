---
name: web-search
description: Search the web using browser automation. Use when user asks to search for information, find websites, or look up current events. Supports Google search with intelligent result extraction. Alternative to web_search tool that doesn't require API keys.
---

# Web Search Skill

Browser-based web search without API dependencies.

## When to Use

Use this skill when:
- User asks to search for information online
- Need current/recent information
- Looking for specific websites or resources  
- web_search tool is unavailable or failing
- Want to avoid API costs

## Quick Start

```
"小贾，搜索一下 FastAPI 教程"
"小贾，帮我查一下最新的 AI 新闻"
"小贾，在网上找找 Python 异步编程的资料"
```

## Complete Workflow (with Cleanup)

### Step 1: Build Search URL

```javascript
// Google search with Chinese language
const query = "FastAPI 教程";
const encodedQuery = encodeURIComponent(query);
const searchUrl = `https://www.google.com/search?q=${encodedQuery}&hl=zh-CN`;
```

### Step 2: Open in Browser

```javascript
const result = browser(action="open", profile="openclaw", targetUrl=searchUrl);
const targetId = result.targetId;  // ⚠️ Save this for cleanup!
```

**Why openclaw profile?**
- Persistent user data (saves cookies)
- Reduces CAPTCHA triggers
- Faster subsequent searches

### Step 3: Capture Page Snapshot

```javascript
browser(action="snapshot", 
        targetId=targetId,  // Use saved targetId
        snapshotFormat="ai",
        maxChars=15000)
```

### Step 4: Extract Search Results

Parse the snapshot to extract:
- Result titles
- URLs
- Snippets/descriptions
- Dates (if available)

### Step 5: Format Output

Present results in clean, readable format.

### Step 6: Clean Up (Important!) ✨

**Always close the tab after use**:

```javascript
browser(action="close", targetId=targetId);
```

**Why this matters**:
- ✅ Frees system resources
- ✅ Prevents tab accumulation
- ✅ Better user experience (no leftover tabs)
- ✅ Complete workflow closure

**Best practice**: Use try-finally pattern to ensure cleanup even if errors occur.

## Complete Example (Pseudocode)

```javascript
function webSearch(query) {
    let targetId = null;
    
    try {
        // 1. Build URL
        const searchUrl = `https://www.google.com/search?q=${encodeURIComponent(query)}&hl=zh-CN`;
        
        // 2. Open browser
        const result = browser(action="open", profile="openclaw", targetUrl=searchUrl);
        targetId = result.targetId;
        
        // 3. Capture results
        const snapshot = browser(action="snapshot", targetId=targetId, maxChars=15000);
        
        // 4. Extract results
        const results = extractSearchResults(snapshot);
        
        // 5. Format output
        return formatResults(results);
        
    } finally {
        // 6. Cleanup: Always close the tab
        if (targetId) {
            browser(action="close", targetId=targetId);
        }
    }
}
```

## Advanced Features

### Site-Specific Search

```javascript
// Search within specific domain
const query = "site:github.com FastAPI";
```

### Recent Results Filter

```javascript
// Add time filter to URL
const searchUrl = `https://www.google.com/search?q=${query}&hl=zh-CN&tbs=qdr:w`;
// qdr:d = past day
// qdr:w = past week  
// qdr:m = past month
// qdr:y = past year
```

### News Search

```javascript
const searchUrl = `https://www.google.com/search?q=${query}&hl=zh-CN&tbm=nws`;
```

## Result Extraction Patterns

### Google Search Results

From snapshot, look for these patterns:

**Title pattern**:
```
- link "[Title Text]" [ref=eXXX] [cursor=pointer]:
  - heading "[Title]" [level=3]
```

**URL pattern**:
```
- /url: https://actual-url.com/path
```

**Snippet pattern**:
```
- generic [ref=eXXX]:
  - text: "Description text..."
  - emphasis: "Highlighted keywords"
```

**Ad detection**:
```
- region "广告" [ref=eXXX]
- heading "赞助商搜索结果"
```

## Output Format

```markdown
# 搜索结果：[Query]

**搜索引擎**: Google
**结果数量**: [Count]

---

## 1. [Title]
**链接**: [URL]

[Snippet/Description]

---

## 2. [Title]
**链接**: [URL]

[Snippet/Description]

---

💡 提示: 让我帮你分析特定页面的详细内容
```

## Error Handling

### CAPTCHA Detection

Check snapshot for CAPTCHA indicators:
```
- heading "请完成安全验证"
- text: "请点击下方按钮完成验证"
```

**Response**:
```
⚠️ 检测到验证码，请稍后重试或使用 web_fetch 工具
```

**Cleanup**: Still close the tab even if CAPTCHA detected.

### No Results

Check for:
```
- text: "找不到和您查询的"
- text: "没有找到相关结果"
```

**Response**: Suggest refining search query.

**Cleanup**: Close the tab.

### Page Load Timeout

If snapshot fails or returns empty:

**Response**:
1. Retry with longer wait time
2. Check internet connection
3. Try alternative search engine

**Cleanup**: Always close the tab, even on error.

## Resource Management Best Practices

### 1. Always Save targetId

```javascript
// ✅ Good
const result = browser(action="open", ...);
const targetId = result.targetId;

// ❌ Bad - can't close later
browser(action="open", ...);
```

### 2. Use try-finally

```javascript
// ✅ Good - guaranteed cleanup
try {
    // ... work ...
} finally {
    browser(action="close", targetId=targetId);
}

// ❌ Bad - might not close on error
// ... work ...
browser(action="close", targetId=targetId);
```

### 3. Handle Cleanup Errors

```javascript
// ✅ Good - silent cleanup errors
finally {
    if (targetId) {
        try {
            browser(action="close", targetId=targetId);
        } catch (e) {
            // Log but don't throw
        }
    }
}
```

### 4. Batch Operations

For multiple searches:

```javascript
// Option A: Close after each (recommended)
for (const query of queries) {
    let targetId = null;
    try {
        targetId = openAndSearch(query);
    } finally {
        if (targetId) close(targetId);
    }
}

// Option B: Reuse tab (advanced)
let targetId = null;
try {
    targetId = openBrowser();
    for (const query of queries) {
        navigateAndSearch(targetId, query);
    }
} finally {
    if (targetId) close(targetId);
}
```

## Integration with Other Skills

- **web-analyzer**: Deep analysis of specific search results
- **summarize**: Summarize content from result pages
- **obsidian**: Save search results to knowledge base

## Comparison: Skill vs Tool

| Feature | web-search skill | web_search tool |
|---------|------------------|-----------------|
| **API Required** | ❌ No | ✅ Yes (Gemini) |
| **Cost** | Free | API charges |
| **Speed** | 3-5 seconds | <1 second |
| **Resource Cleanup** | ✅ Automatic | N/A |
| **Customization** | High | Limited |

## Notes

- Always close tabs after use
- Use openclaw profile for persistence
- Handle errors gracefully
- Respect rate limits

---

**Remember**: A complete workflow includes cleanup! 🧹
