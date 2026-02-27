# Web Search Skill

基于浏览器自动化的网页搜索功能，无需 API Key。

## 特点

- ✅ **无需 API**: 不需要 Google/Gemini API Key
- ✅ **多引擎支持**: Google、Bing、DuckDuckGo、Baidu
- ✅ **零成本**: 无 API 调用费用和速率限制
- ✅ **利用现有会话**: 使用你的 Chrome cookies 和登录状态
- ✅ **灵活定制**: 支持日期过滤、站点搜索等高级功能

## 使用方法

### 基本搜索

```
"小贾，搜索一下 FastAPI 教程"
"小贾，帮我查一下最新的 AI 新闻"
"小贾，在网上找找 Python 异步编程的资料"
```

### 指定搜索引擎

```
"用 Bing 搜索一下..."
"用百度搜索..."
"用 DuckDuckGo 搜索..."
```

### 高级搜索

```
"在 GitHub 上搜索 FastAPI 项目"  # site:github.com
"搜索最近一周的 AI 新闻"         # 日期过滤
```

## 工作原理

1. **构建搜索 URL**: 根据查询和搜索引擎生成 URL
2. **打开浏览器**: 使用 browser 工具打开搜索页面
3. **捕获结果**: 获取页面快照
4. **解析提取**: 从快照中提取标题、链接、摘要
5. **格式化输出**: 以结构化格式展示结果

## 优势

| 特性 | web-search skill | web_search tool |
|------|------------------|-----------------|
| API 需求 | ❌ 不需要 | ✅ 需要 Gemini API |
| 成本 | 免费 | API 调用费用 |
| 搜索引擎 | 多个 | 仅 Google |
| 速度 | 较慢 (3-5秒) | 快 (<1秒) |
| 隐私 | 使用你的浏览器 | API 追踪 |
| 定制性 | 高 | 有限 |

## 技术实现

### 搜索引擎 URL 模板

```javascript
// Google
https://www.google.com/search?q=${query}&hl=zh-CN

// Bing
https://www.bing.com/search?q=${query}

// DuckDuckGo
https://duckduckgo.com/?q=${query}

// Baidu
https://www.baidu.com/s?wd=${query}
```

### Browser 工具调用

```javascript
// 1. 打开搜索页面
browser(action="open", profile="chrome", targetUrl=searchUrl)

// 2. 捕获页面快照
browser(action="snapshot", targetId="<tab-id>", snapshotFormat="ai")

// 3. 解析结果并格式化输出
```

## 注意事项

- 需要浏览器服务运行
- 速度比 API 调用慢（3-5秒 vs <1秒）
- 频繁使用可能触发验证码
- 依赖浏览器的可用性

## 与其他 Skills 集成

- **web-analyzer**: 深度分析搜索结果页面
- **summarize**: 总结搜索结果内容
- **obsidian**: 保存搜索结果到知识库

## 开发状态

- [x] 基本搜索功能设计
- [x] 多搜索引擎支持
- [x] SKILL.md 文档
- [ ] 实际测试和优化
- [ ] 结果解析逻辑完善
- [ ] 错误处理增强

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License
