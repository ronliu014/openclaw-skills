# Web Analyzer Skill

深度网页分析和内容提取技能，使用浏览器自动化技术。

## 功能特性

- ✅ 打开和分析任何网页（包括微信公众号文章）
- ✅ 提取标题、作者、日期、正文内容
- ✅ 识别页面结构和类型
- ✅ 提取图片和链接信息
- ✅ 生成智能摘要
- ✅ 支持截图保存
- ✅ 处理动态加载内容

## 使用方法

### 基础用法

直接告诉小贾分析网页：

```
"小贾，帮我分析这个网页：https://example.com"
"小贾，读取这篇文章的内容：https://mp.weixin.qq.com/s/xxxxx"
"小贾，提取这个页面的关键信息"
```

### 高级用法

**保存到 Obsidian：**
```
"小贾，分析这个网页并保存到 Obsidian"
```

**截图保存：**
```
"小贾，分析这个网页并截图"
```

**深度分析：**
```
"小贾，详细分析这篇技术文章，提取所有代码示例"
```

## 工作流程

1. **启动浏览器** - 自动启动 OpenClaw 浏览器实例
2. **打开页面** - 加载目标 URL
3. **等待渲染** - 等待页面完全加载（3-5秒）
4. **捕获快照** - 获取页面结构和内容
5. **提取信息** - 解析标题、作者、正文等
6. **生成摘要** - 创建结构化输出

## 输出格式

```markdown
# [页面标题]

**元信息**:
- **链接**: [URL]
- **作者**: [作者名]
- **日期**: [发布日期]

## 摘要

- 关键点 1
- 关键点 2
- 关键点 3

## 主要内容

[提取的正文内容，保持原有结构]

## 相关链接

- [链接1](url1)
- [链接2](url2)

## 图片信息

页面包含 X 张图片
```

## 适用场景

### ✅ 适合使用的场景

- 微信公众号文章
- 技术博客和文档
- 新闻网站
- 产品页面
- 社交媒体帖子
- 需要截图的页面
- JavaScript 渲染的动态内容

### ⚠️ 不适合的场景

- 需要登录的页面（除非提供凭证）
- 付费墙内容
- 需要人机验证的页面
- 实时更新的数据（如股票行情）

## 辅助脚本

### extract_content.py

用于从浏览器快照中提取和清理内容。

**用法：**
```bash
python scripts/extract_content.py snapshot.txt
python scripts/extract_content.py snapshot.txt https://example.com
```

## 故障排除

### 浏览器无法启动

```bash
# 检查浏览器状态
openclaw gateway status

# 重启 gateway
openclaw gateway restart

# 手动启动浏览器
browser(action="start", profile="openclaw")
```

### 页面加载超时

- 增加等待时间（5-10秒）
- 检查网络连接
- 尝试使用 web_fetch 作为备选

### 内容提取不完整

- 页面可能需要滚动加载
- 尝试多次快照
- 检查是否有弹窗遮挡

## 与其他 Skills 集成

- **summarize**: 深度内容分析
- **obsidian**: 保存到知识库
- **github**: 提取代码片段

## 技术细节

- 使用 OpenClaw 内置 browser 工具
- 基于 Playwright 引擎
- 支持 Chrome/Edge 浏览器
- 快照格式：AI-optimized text format
- 隔离的浏览器环境（openclaw profile）

## 更新日志

### v1.0.0 (2026-02-25)
- ✅ 初始版本
- ✅ 基础网页分析功能
- ✅ 内容提取脚本
- ✅ 微信公众号文章支持

## 作者

小贾 (OpenClaw Assistant)

## 许可

MIT License
