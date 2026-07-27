---
type: web_source
source_url: "https://vibe-hub.org/en/grid"
title: "Grid"
language: en
category: "grid"
fetched_at: 2026-07-27T10:05:06+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←FlexZ-Index→

# Grid

You might say

Arrange these cards in a clean grid that switches to two columns on narrower screens.

**Plan rows and columns as one layout system**·CSS Grid controls two-dimensional layouts where rows and columns work together. It suits galleries, dashboards, and page regions. Let columns adapt to available space instead of copying one fixed desktop grid onto every screen.

Know first

[Space](/en/space)

### When to use it

- Responsive card gallery
- Dashboard panels
- Page regions with aligned rows and columns
- Layouts with intentional spanning

### When NOT to use it

- Use grid for a simple one-dimensional row

  Grid is usually more direct when you need to control rows and columns together.
- Hard-code many columns on small screens

  33.33%33.33%33.33%

  A hand-written percentage grid needs extra calculations whenever spacing changes.
- Reorder content visually in a way that breaks reading order

  Fixed column counts and widths can overflow on narrow screens.
- Create empty tracks only to imitate spacing

Anatomy

Grid

1ContainerWrite display: grid on the parent element

2TrackEach defined row or column track

3CellThe grid formed by the intersection of rows and columns

4GapThe gaps between grid items, declared once for the whole grid

Variants

Repeat

Each column of the card wall is the same width

AutoFill

When the width changes, the number of columns automatically increases or decreases.

Gap

Use gap to uniformly manage row and column spacing

TwoColumns

Overall framework like sidebar + content

Typical use cases

Card gallery

repeat(3, 1fr) three equal columns

![](/assets/cover-mountain.png)

**Mountain Hiking**

1.2k Collection

![](/assets/cover-workspace.png)

**Desktop aesthetics**

856 Collection

![](/assets/photo-cat.png)

**Cat daily life**

2.4k collection

Dashboard

auto-fill + minmax, adjust the number of columns according to the available width

![](/assets/slide-summer.png)

**Summer canvas bag**

¥ 89

![](/assets/slide-city.png)

**City postcard**

¥ 19

![](/assets/slide-forest.png)

**Forest Aromatherapy**

¥ 129

Media grid

grid-template-columns: 2fr 1fr

**Visit trends**

Registered user

**8,921**

Conversion rate

**4.6%**

Page shell

grid-template-columns: 120px 1fr

**Console**

Overview

item

Settings

**Project Overview**

Further reading

[CSS grid layoutMDN ↗](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Grids)[A Complete Guide to CSS Grid LayoutCSS-Tricks ↗](https://css-tricks.com/snippets/css/complete-guide-grid/)
