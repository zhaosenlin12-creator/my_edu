---
type: web_source
source_url: "https://vibe-hub.org/en/flex"
title: "Flex"
language: en
category: "flex"
fetched_at: 2026-07-27T10:05:06+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←PaddingGrid→

# Flex

You might say

Put these buttons in one row with even spacing and center them vertically.

**Arrange items along one row or one column**·Flexbox lays items out on a single main axis and handles alignment, spacing, wrapping, and flexible size. It is a good fit for toolbars, form rows, and card content. Use grid when both rows and columns need a planned structure.

Know first

[Space](/en/space)

### When to use it

- Align items in a row

  HomeComponentsTerm
- Build a vertical stack

  NameEmailflex-direction: column changes the layout to vertical.
- Distribute space between controls

  Sign inSet both the main and cross axes to center.
- Let items wrap when room runs out

  Project newsView all

### When NOT to use it

- Use many nested flex containers for a simple grid

  float leftfloat rightUsing floats for ordinary layout also requires clearing them.
- Set fixed widths that fight the flexible layout

  Grid is usually more direct when you need to control rows and columns together.
- Forget how the order changes on small screens

  When the width is fixed and line wrapping is prohibited, child elements may overflow the container.
- Use visual order that differs from keyboard and reading order

  Label oneLabel twoLabel threeTag fourTag fiveTag six

Anatomy

itemMain axis →Cross axis ↓

1ContainerThe parent element with display: flex written on it

2Itemdirect child elements in the container

3Main AxisThe arrangement direction of items, justify-content takes care of it

4Cross AxisPerpendicular to the main axis, align-items doesn't care

Variants

Row

The default main axis is horizontal; select it when the content needs to flow along the same line.

Column

The main axis is changed to vertical direction; select when the content order should be from top to bottom.

Center

When the container size is clear, allocate the remaining space on both axes to both sides of the content

SpaceBetween

Place the remaining space on the main axis between items; suitable for arrangements that require welting at both ends

Typical use cases

Toolbar

display: flex · horizontal row

![](/assets/logo.svg)**VibeHub**
Components
Terms
Examples

![](/assets/avatar-robot.png)

Flex keeps the logo, links, and avatar aligned in one row

Navigation row

flex-direction: column

Nickname
Email
Save data

Form actions

justify-content: space-between

**Project News**
View all →

![](/assets/avatar-fox.png)Little Fox has updated the "Home Page Revision"
10:24

Card header

align-items + justify-content: center

![](/assets/empty-box.png)

No news yet, the content is centered on both axes

Further reading

[FlexboxMDN ↗](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Flexbox)[A Complete Guide to CSS FlexboxCSS-Tricks ↗](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
