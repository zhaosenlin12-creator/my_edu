---
type: web_source
source_url: "https://vibe-hub.org/en/sticky"
title: "Sticky"
language: en
category: "sticky"
fetched_at: 2026-07-27T10:05:15+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←Z-IndexPosition→

# Sticky

You might say

Keep the navigation pinned to the top while people scroll down.

**Keep an element visible after scrolling reaches it**·Sticky positioning lets a header, table heading, or section navigation follow the viewport within its container. It needs a defined offset and enough room to move. Test parent overflow and small screens, because both can change or block sticky behavior.

Know first

[Position](/en/position)

🔥 Popular components

Button

Text input

Card

🧭 Page navigation

Navigation menu

Pagination

Breadcrumbs

↕ Try scrolling: the group heading sticks to the top

### When to use it

- Keep table headers visible

  Task     StatusSign-in page redesign     In progressPayment flow     Complete
- Keep section navigation nearby

  AKaiBMs. Bai
- Hold important actions within a long panel

  Filter bar · sticky at top
- Pin a page header after it reaches the top

  position: sticky; top: 0;

### When NOT to use it

- Make several large regions sticky at once

  Ancestor: overflow: hiddenMay limit sticky’s scroll rangeCheck ancestor overflow, the scroll container, and the available scroll height.
- Cover the content people are trying to read

  Fixed barfixed removes the bar from document flow and covers the first line of content.
- Expect sticky to work through a clipping parent

  Sticky heading with a transparent background
- Use it on a small screen without checking remaining space

  Sticky navigationSticky filtersSticky table header

Anatomy

Group title · stickytop: 0Occupy space in the document flow without blocking others

1Scroll Containersticky relatively recent scrolling ancestor adsorption

2Sticky ElementThe element with position: sticky

3top / bottomWhen the scroll reaches a certain distance from the edge, it will be sucked. If you don’t write it, it will not take effect.

4In FlowAfter sucking, the original position is still retained, and the content is not blocked.

Variants

Sticky Top

top: 0

Scroll to the top of the header and navigation and click it.

Sticky Bottom

bottom: 0

Scroll the bottom operation bar all the way to stick it

Group Headers

AB

Address book letter, date group title

Typical use cases

Table header

TaskOwnerStatus

Login page revisionAlex ChenIn progress

Payment process reviewAkaiCompleted

Design specification v2 archiveTeacher BaiNot started

Documentation sidebar

A

![](/assets/avatar-fox.png)AkaiFront end

![](/assets/avatar-robot.png)A MayOperation

B

![](/assets/avatar-fox.png)Teacher BaiDesign

Page toolbar

Near subway
Can cook

![](/assets/cover-mountain.png)

**Mountain Guest House · Genting**

Dali · East Gate of the Ancient City · ¥688/night

![](/assets/slide-forest.png)

**Woodhouse · Valley**

Moganshan · Yu Village · ¥520/night

Section heading

![](/assets/slide-summer.png)

**Summer seaside postcard set ×1**

¥ 39.00

![](/assets/photo-cat.png)

**Cat photography album "Light on the Windowsill" ×1**

¥ 128.00

![](/assets/slide-city.png)

**City Walking Map · Guangzhou ×2**

¥ 58.00

Total **¥ 283.00**
Go to checkout (4)

Further reading

[positionMDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/position)[Sticky Headers: 5 Ways to Make Them BetterNN/g ↗](https://www.nngroup.com/articles/sticky-headers/)
