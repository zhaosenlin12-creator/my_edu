---
type: web_source
source_url: "https://vibe-hub.org/authorization"
title: "权限控制 Authorization"
language: zh
category: "authorization"
fetched_at: 2026-07-27T10:04:23+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←身份认证身份认证→

# 权限控制Authorization

你可能会说

登录之后还要分谁能看谁不能看，管理员和普通用户不一样。

**权限控制是在确认身份后判断用户能访问或操作哪些资源的机制**·例如，普通用户只能修改自己的资料，管理员可管理成员。敏感操作必须在服务端逐次检查；隐藏按钮只改善界面，不能代替权限判断。

先知道

[身份认证 **Authentication**](/authentication)[数据库 **Database**](/database)

当前用户**成员 · 小林**

查看项目*允许*

编辑自己的任务*允许*

删除他人任务*拒绝*

管理全部账号*拒绝*

### 什么时候用

- 每次读取或修改敏感资源，都在服务端检查当前用户

  每次敏感操作都经过权限判断

  当前用户→权限规则→允许 / 拒绝
- 同时检查角色和资源归属：是不是本人、是不是项目成员

  角色之外，还要看资源关系

  当前用户**u\_23**文章作者**u\_23**结果**允许编辑**
- 默认拒绝，只明确开放真正需要的能力

  默认拒绝，按需开放

  默认**DENY**明确开放**viewer → read**
- 为管理操作保留审计记录：谁在什么时候改了什么

  管理操作留下记录

  16:42 · admin\_u7disabled user\_u23reason: repeated abuse

### 什么时候不用

- 只把删除按钮隐藏：用户仍可以直接请求删除接口

  隐藏按钮不等于接口安全

  页面**没有删除按钮**
  *→*
  直接请求**DELETE /users/42 → 204**
- 相信前端传来的 userId 或 role=admin

  前端声明的身份可以伪造

  POST /api/admin/delete{ "userId": "u\_23", **"role": "admin"** }
- 登录后默认允许访问所有数据：认证不等于授权

  登录不代表能看所有数据

  已登录→访问他人账单→应该 403
- 权限规则散落在几十个文件里，改一处漏三处

  同一规则散落多处

  users.ts**检查 admin**orders.ts**忘了检查**reports.ts**规则不同**

组成结构 · Anatomy

谁能否做什么作用于哪个资源

1主体Subject当前已通过认证的用户，以及可信来源中的角色和成员关系

2动作Action读取、编辑、删除、审批等需要逐项判断的能力

3资源Resource目标记录、项目或文件；还要检查它归谁所有、属于哪个组织

常见变体 · Variants

按角色Role-based

viewer · editor · admin

规则简单、角色边界清晰

按资源归属Ownership

post.userId === me.id

用户只能操作自己的数据

按成员关系Membership

project\_members

团队与多人协作产品

典型使用场景

只能编辑自己的资料

个人资料**按资源归属判断编辑权限**

当前用户**u\_23**资料所有者**u\_23**结果**允许编辑**

项目成员可查看

项目成员**成员关系决定查看权限**

项目**VibeHub**用户角色**viewer**权限**可查看 · 不可删除**

管理员可以封禁账号

管理员操作**封禁账号并留下审计记录**

目标账号**user\_42**原因**重复滥用**

确认封禁

记录 admin\_u7 · 16:42 · disable user\_42

付费用户访问高级功能

付费功能**订阅状态由服务端确认**

当前方案**Free**
*→*
导出高清文件**需要 Pro**

隐藏入口之外，接口仍要检查订阅权限

延伸阅读 · 权威出处

[权限控制安全清单OWASP ↗](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
