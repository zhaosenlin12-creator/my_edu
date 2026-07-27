---
type: ai_tool
status: evaluate
domain: ai,automation,windows
audience: self,apprentice
repo:
url:
summary: 用于操作 Windows 桌面应用和验证真实界面的能力层
next_action: 固化 Obsidian、浏览器和教学软件三个低风险流程
updated_at: 2026-07-27
tags: ai,computer-use,windows,automation
---

# Codex Computer Use

> 让 AI 能操作真实桌面，但权限越接近人，验收和风险控制就越重要。

## 已验证场景
- 启动并打开本地 Obsidian Vault
- 检查应用窗口、页面状态和实际交互
- 辅助重复性的桌面流程

## 风险分级
| 级别 | 示例 | 规则 |
|---|---|---|
| 低 | 打开文件、截图、读取界面 | 可自动执行 |
| 中 | 修改设置、填写表单、批量移动 | 执行前确认范围 |
| 高 | 发布、付款、删除、发送消息 | 必须人工最终确认 |

## 标准流程
1. 明确目标窗口和要操作的对象。
2. 操作前记录当前状态。
3. 每个关键步骤后截图或读取状态。
4. 出现弹窗、账号切换或未知页面立即停下。
5. 完成后回到文件或系统状态验证结果。

## 下一步
- [ ] Obsidian 新人开库流程
- [ ] 教学软件课前检查流程
- [ ] 个人站发布后桌面与移动端验收流程

## 关联
- [[50_AI/codex]]
- [[50_AI/codex-browser]]
- [[00_Home/MOCs/ai_tools]]
