---
type: ai_tool
status: active
domain: ai,api,education
audience: self
repo:
url: https://platform.deepseek.com/
summary: 已用于 Python 冒险岛等项目的模型 API，承担结构化出题与后端能力
next_action: 建立成本、稳定性、降级和内容安全基线
updated_at: 2026-07-27
tags: ai,deepseek,api,education
---

# DeepSeek API

> 已进入真实项目的模型 API，不只是聊天工具；因此必须按生产依赖来管理。

## 已验证场景
- Python 冒险岛中的 AI 智能出题
- 按科目、年级和模板生成结构化内容
- 作为后端能力被 Web 应用调用

## 工程检查清单
- [ ] API Key 仅存在环境变量，不进入 Git
- [ ] 请求设置超时、重试和错误提示
- [ ] 输出经过 JSON Schema 或业务校验
- [ ] 学生可见内容经过安全过滤
- [ ] 记录单次请求成本与月度预算
- [ ] 供应商不可用时有静态题库降级

## 教学使用边界
- AI 出题只能作为题库草稿，教师对知识点和答案负责
- 不把学生姓名、联系方式和学习档案直接发给模型
- 课堂中明确哪些内容由 AI 生成

## 下一步
- [ ] 从 python-adventure 提炼可复用 API 封装
- [ ] 补一份故障降级演练记录
- [ ] 建立模型切换对照表

## 关联
- [[20_Projects/python-adventure]]
- [[50_AI/codex]]
- [[00_Home/MOCs/ai_tools]]
