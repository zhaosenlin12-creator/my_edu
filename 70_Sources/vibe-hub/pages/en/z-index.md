---
type: web_source
source_url: "https://vibe-hub.org/en/z-index"
title: "Z-Index"
language: en
category: "z-index"
fetched_at: 2026-07-27T10:05:07+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←GridSticky→

# Z-Index

You might say

This dialog is getting covered by other content. Make sure it stays on top.

**Control which overlapping layer appears on top**·Z-index affects the stacking order of positioned elements inside a stacking context. A larger number does not always escape its parent. Define a short layer scale for content, sticky UI, menus, overlays, and dialogs instead of solving each overlap with a larger random number.

Know first

[Position](/en/position)

z: 1
z: 2
z: 3

### When to use it

- Keep a dropdown above nearby content

  Delete this project?

  CancelDelete
- Place a dialog above its backdrop

  Navigation · z-index: 100
- Order sticky and floating elements

  All statesAll statesIn progress
- Create a shared layer scale

  Content 1Sticky header 100Overlay 1000Dialog 10000

### When NOT to use it

- Keep increasing the number without checking the stacking context

  z-index: 99, but no position is set
- Give every component its own arbitrary z-index

  z-index: 9999z-index: 99999z-index: 999999
- Place ordinary content above a modal

  Parent z-index: 1Child 9999z-index: 2
- Use layering to hide a layout or clipping problem

  Content that appears earlier in the codeUse z-index to force a different stacking orderIf the visual order should match the document order, adjust the DOM structure first.

Anatomy

z-index: 1z-index: 2The big one is on top

1BottomThe z-index is small and is suppressed below.

2TopThe z-index is larger and covers it.

3Z-IndexThe stacking value used to position elements and flex/grid items; it also depends on the stacking context in which it is located.

Variants

1 ~ 10

12

The card corner mark and avatar are slightly overlaid.

100

100

Fixed bar suppresses scrolling content

1000

Page1000

Drop-down, bubble, text prompt

10000

10000

Example gear: Make the modal layer higher than the ordinary page floating layer

Typical use cases

Dropdown layer

Page z-index: 1

Mask z-index: 1000

Pop-up z-index: 1001
**Confirm to log out?** 

CancelExit

Sticky header

**Document Center**
Guidelines
API
z-index: 100

In the same cascading rule, the navigation level is higher than the scrolling content

Modal

**Task list**
In progress ▾

z-index: 1000

All

In progress ✓

Completed

The drop-down floats on top of the card and is neither covered nor cut

Tooltip

＋
z-index: 10

Further reading

[z-indexMDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/z-index)[Stacking contextMDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_positioned_layout/Stacking_context)
