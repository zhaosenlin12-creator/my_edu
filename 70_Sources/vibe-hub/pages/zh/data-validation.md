---
type: web_source
source_url: "https://vibe-hub.org/data-validation"
title: "数据校验 Validation"
language: zh
category: "data-validation"
fetched_at: 2026-07-27T10:04:23+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←CORSAPI→

# 数据校验Validation

你可能会说

用户乱填也能提交成功，怎么在保存之前先拦住？

**数据校验是在使用输入前检查其格式、范围和业务规则的步骤**·例如，必填项可在用户离开字段时提示，跨字段规则通常在提交时统一检查。前端提示帮助用户及时纠正，但可能被绕过；后端仍须重新校验并返回具体字段错误。

先知道

[路由与端点 **Route & Endpoint**](/route)[JSON](/json)

邮箱**oil@example.com***✓*
年龄**0***✕ 须为 1–120*
角色**user***✓*

后端规则**有一处不通过就不写入**

### 什么时候用

- 在后端检查**类型、必填、范围、长度和允许值**

  一眼看清字段规则

  email**必填 · 邮箱格式**price**数字 · 大于 0**role**user / admin**
- 返回字段级错误，让前端知道该在输入框旁提示什么

  错误要指向具体字段

  商品价格**-3**输入框下方**价格必须大于 0**
- 先校验，再执行业务和数据库写入

  校验通过才写数据库

  收到输入→规则检查→写入数据库
- 尽量使用框架的 schema 校验能力，规则集中在一处

  规则集中在一份 Schema

  email: string().email()price: number().positive()role: enum(["user", "admin"])

### 什么时候不用

- 只做前端校验：请求可以绕过页面直接发到接口

  页面检查可以被绕过

  跳过表单→直接请求 API→后端仍需校验
- 校验失败仍按成功结果返回：状态码和响应体应遵守 API 约定，前端也要解析业务结果

  状态码与结果互相矛盾

  HTTP**200 OK**响应内容**error: invalid email**

  前端很容易把失败当成功
- 把技术堆栈和数据库报错原样展示给用户

  不要把内部报错丢给用户

  **PrismaClientKnownRequestError**at node\_modules/runtime/library.js:129:42

  页面应该显示：暂时无法保存，请稍后重试
- 偷偷修正关键输入，例如把负价格自动变成正数

  不要偷偷改关键数据

  用户输入**价格 -99**
  *→*
  系统擅自改成**价格 99**

  应明确拒绝并让用户确认

组成结构 · Anatomy

原始输入*→*校验规则*→*通过或字段错误

1原始输入Raw Input来自表单、URL、请求头或第三方系统，都不能默认可信

2规则Schema定义字段类型、是否必填、范围、长度和允许值

3结果Result通过后只说明格式符合规则；仍要检查权限、业务条件和输出场景

典型使用场景

注册邮箱和密码

注册校验**在字段旁说明怎样修改**

邮箱**oil@**密码**••••**创建账号

邮箱格式不完整 · 密码至少 8 位

创建商品价格

商品价格**拒绝不合理数值**

售价**-19.90**

校验结果**价格必须大于 0**

文章标题长度

文章标题**输入时显示长度限制**

标题**这是一个超过允许长度的文章标题……**

当前**56 字**上限**40 字**

API 请求体 schema

请求体 Schema**集中检查 API 字段**

email**✓ string**age**✕ 应为 1–120**role**✓ user**

失败时按 API 约定返回 400 或 422 及字段级错误

延伸阅读 · 权威出处

[客户端表单验证MDN ↗](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)[帮助用户在表单中输入正确的数据web.dev ↗](https://web.dev/learn/forms/validation)
