---
type: template
status: active
domain: project,code-review
audience: self
updated_at: 2026-07-27
tags: code-review,checklist
---

# 代码审查清单

## 提交前自检
- [ ] diff 只处理一个主题
- [ ] 提交信息说清楚为什么改
- [ ] 没有把密钥、Token、.env 写进代码
- [ ] 没有把课程数据、学生信息硬编码
- [ ] 单元测试或手动验证已运行
- [ ] README、注释、properties 同步更新

## 让 AI 改代码时
- [ ] Codex 先读仓库再修改
- [ ] 让 Codex 列出 diff 摘要
- [ ] 至少人工 review 一次 diff
- [ ] 在 IntelliJ 中编译并运行测试
- [ ] 必要时打开 VibeHub 相关术语页对照术语是否准确

## 教学项目额外项
- [ ] 学员可读代码（变量名 / 函数名 / 注释）
- [ ] 提供运行截图或录屏
- [ ] 难度与学生年级匹配

