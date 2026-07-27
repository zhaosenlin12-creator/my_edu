---
type: web_source
source_url: "https://vibe-hub.org/en/position"
title: "Position"
language: en
category: "position"
fetched_at: 2026-07-27T10:05:18+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←StickyCentering→

# Position

You might say

Pin this little icon to the top-right corner of the card so the rest of the layout doesn't affect it.

**Place an element in normal flow, against a parent, or against the viewport**·CSS position decides how an element is placed and whether offsets such as top and left apply. Relative often creates a reference for an absolutely positioned child; fixed follows the viewport; sticky moves only within its scrolling context. Choose the mode from the relationship you need.

NEW
✓ Card has relative — badge sticks to the card's corner

NEW
✕ No relative on the card — badge flies to the container's corner →

### When to use it

- Anchor a badge to an icon

  3
- Fix a floating control to the viewport

  ＋
- Create a reference for an overlay inside a component

  Filter bar · sticky at top
- Keep normal content in document flow by default

  All statesAll statesIn progress

### When NOT to use it

- Absolutely position the main page layout

  Badge flies into the cornerWithout relative on the card, absolute positioning is relative to the body.
- Use fixed coordinates that only fit one screen

  z-index: 99, but no position is set
- Remove content from flow without reserving its space

  Fixed barfixed removes the bar from document flow and covers the first line of content.
- Choose a position mode before identifying its reference box

  top:6 left:8top:18 left:62top:42 left:28Hard-coded coordinates break as soon as content gets longer.

Anatomy

anchortop: 0 · right: 0z-index: 1 · May cover other content

1Containing BlockAbsolute often determines the containing block from the nearest positioning ancestor; transform, contain, etc. may also create a containing block. If it cannot be found, refer to the initial containing block. Do not call it body in general.

2Positioned ElementOnly if the position is not static can you use offset

3Offsetstop / right / bottom / left, determine how far away from each side of the reference object

4Stackingz-index can be used to position elements and flex/grid children; compare the stacking context first, and then compare the values

Variants

Static

static

This is it by default, queuing with the document flow

Relative

relative

Fine-tune the position, or use anchor points for child elements

Absolute

3

Corner floating layer, relatively recent positioning ancestor

Fixed

＋

Floating button and pin operation, scrolling does not follow

Sticky

top: 0

The meter header and navigation scroll to the set position and then snap.

Typical use cases

Badge on avatar

![](/assets/avatar-fox.png)

Design Crew

New homepage draft just dropped

10:24
3

![](/assets/avatar-robot.png)

Vibe Assistant

Your page is live now

09:50

Floating button

＋

Popover anchor

**Vibe Guide**
Components
Concepts
Practice

Sticky toolbar

**Members**
Role: All ▾

![](/assets/avatar-fox.png)MayaAdmin

![](/assets/avatar-robot.png)AlexGuest

All roles ✓

Admin

Editor

Further reading

[positionMDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/position)
