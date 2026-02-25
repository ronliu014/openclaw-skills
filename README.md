# OpenClaw Skills Collection

刘金龙的 OpenClaw 自定义技能集合。

## 📦 Skills 列表

### web-analyzer
深度网页分析和内容提取技能。

**功能：**
- 打开和分析任何网页（包括微信公众号文章）
- 提取标题、作者、日期、正文内容
- 识别页面结构和类型
- 提取图片和链接信息
- 生成智能摘要
- 支持截图保存

**使用：**
```
"小贾，帮我分析这个网页：[URL]"
"小贾，读取这篇文章的内容"
```

**状态：** ✅ 已测试，可用

---

## 🚀 安装方法

### 方法 1：直接复制
```bash
# 复制到 OpenClaw skills 目录
cp -r web-analyzer ~/path/to/openclaw/skills/
```

### 方法 2：Git Clone
```bash
git clone https://github.com/ronliu014/openclaw-skills.git
cd openclaw-skills
cp -r web-analyzer ~/path/to/openclaw/skills/
```

## 📝 开发规范

所有 skills 遵循 OpenClaw 标准结构：

```
skill-name/
├── SKILL.md          # 必需：技能文档
├── README.md         # 可选：使用说明
├── scripts/          # 可选：辅助脚本
├── references/       # 可选：参考文档
└── assets/           # 可选：资源文件
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可

MIT License

## 👤 作者

刘金龙 (ronliu014)
- GitHub: [@ronliu014](https://github.com/ronliu014)
- Email: 66141975@qq.com

## 🙏 致谢

感谢 OpenClaw 项目提供的强大平台。
