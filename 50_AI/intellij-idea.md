---
type: development_tool
status: active
domain: development,ide,build
audience: self
repo:
url: https://www.jetbrains.com/idea/
summary: 主力工程 IDE，用于项目打开、编译、运行、测试和调试
next_action: 按具体项目确认 JDK、Maven 或 Gradle 配置
updated_at: 2026-07-27
tags: intellij,ide,build,debug
---

# IntelliJ IDEA 2026.1

> IntelliJ 是工程 IDE，不是单独的编译器。它负责组织并调用项目的 JDK、Maven、Gradle、Node.js 等真实工具链。

## 已确认安装
- 版本：IntelliJ IDEA 2026.1 Ultimate
- Build：261.22158.277
- 程序：`C:\Users\Administrator\AppData\Local\JetBrains\IntelliJ IDEA 2026.1\bin\idea64.exe`
- 快捷方式：`C:\Users\Public\Desktop\IntelliJ IDEA 2026.1.lnk`

## 在我的工具链中的职责
- 打开和理解大型工程
- Java / Kotlin 项目调用 JDK、Maven 或 Gradle 编译
- 运行单元测试、断点调试和查看日志
- 管理 Git 分支、提交与差异
- Web 项目通过内置终端调用 `npm`、`pnpm` 或项目脚本

## 与 Codex 的分工
- Codex：读仓库、分析需求、修改代码、执行自动化验证
- IntelliJ：人工浏览、工程配置、编译运行、调试与最后确认
- 编译成功不等于功能正确；仍要运行测试和真实业务流程

## 为什么不需要 Trae
- Trae 的核心价值是 AI 编辑器与对话式编码
- 当前已有 Codex 负责 AI 协作，IntelliJ 负责成熟 IDE 和工程验证
- Trae 没有形成不可替代的真实任务证据，因此移入 `90_Archive`

## 使用检查
- [ ] 项目使用的 JDK / Node / Python 版本正确
- [ ] Maven / Gradle / pnpm 依赖完成同步
- [ ] 编译与测试命令来自仓库说明，而不是凭经验猜
- [ ] 运行配置没有包含 Token 或生产密钥

## 关联
- [[50_AI/codex]]
- [[20_Projects/index]]
- [[90_Archive/trea-cn]]
