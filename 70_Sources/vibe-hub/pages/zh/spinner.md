---
type: web_source
source_url: "https://vibe-hub.org/spinner"
title: "旋转加载指示器 Spinner"
language: zh
category: "spinner"
fetched_at: 2026-07-27T10:03:57+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←结果页警告提示→

# 旋转加载指示器Spinner

你可能会说

加载慢的时候给个转圈的东西，不然用户以为坏了。

**旋转加载指示器是用持续旋转表示系统正在处理、但完成度未知的状态组件**·点击保存后短暂等待时，可在按钮旁显示旋转指示器并说明“正在保存”。等待过长时不能只让它旋转，应提供取消、重试或失败结果。

也常被叫作*加载圈**Loading Spinner*

**正在生成预览**通常需要几秒钟，请不要关闭此页面

容易混淆？这样区分

旋转加载指示器Spinner**≠**[进度条 **Progress**](/progress)

spinner 只说明系统仍在处理，不会显示完成了多少；[进度条 **Progress**](/progress) 用一条轨道展示任务的整体进展，能计算时还会显示比例。

旋转加载指示器Spinner**≠**[骨架屏 **Skeleton**](/skeleton)

spinner 适合短暂、局部的等待；[骨架屏 **Skeleton**](/skeleton) 会用内容轮廓提前占好整块页面的位置。

### 什么时候用

- **按钮提交后的短暂等待**：避免重复提交

  正在保存设置…
- **局部内容刷新**：不打断用户浏览页面
- **无法计算总量的处理**：同时说明当前任务

### 什么时候不用

- 已知文件大小或完成度：使用 [进度条 **Progress**](/progress)

  正在保存设置…
- 整页内容轮廓可预测：使用 [骨架屏 **Skeleton**](/skeleton)
- 长时间等待却没有取消、失败或重试入口

组成结构 · Anatomy

正在保存…

1旋转指示器Indicator持续运动，但不暗示不存在的完成比例

2状态文字Label说明系统正在处理的任务

常见变体 · Variants

按钮内In button

保存中

提交后暂时锁定当前操作

局部加载Inline

正在刷新

列表或区域更新时

居中等待Centered

加载中

弹窗或空白面板处理中

典型使用场景

保存按钮

保存中

局部列表刷新

**最近项目**

弹窗处理中

**正在导出报告**请不要关闭窗口

延伸阅读 · 权威出处

[进度指示器让慢系统没那么难熬NN/g ↗](https://www.nngroup.com/articles/progress-indicators/)
