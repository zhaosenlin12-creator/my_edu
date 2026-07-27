---
type: web_source
source_url: "https://vibe-hub.org/en/border-radius"
title: "BorderRadius"
language: en
category: "border-radius"
fetched_at: 2026-07-27T10:05:05+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←DividerShadow→

# BorderRadius

You might say

Round the sharp corners on these cards a bit so they feel softer.

**Round the corners of a box**·Border radius changes sharp corners into rounded ones and helps set the visual tone of controls, cards, and images. Define a small set of radius values and use them consistently. A pill shape works only when the height and content support it.

### When to use it

- Soften controls and cards

  Input control: control tokenContent container: surface token
- Create circular avatars

  LSquare + 50% = perfect circle avatar
- Build pills or tags

  Pill labelPill button
- Keep a product's corner language consistent

  SmallMid-rangeLarge

### When NOT to use it

- Choose a different radius for every component
- Round nested boxes so much that their edges clash

  A rectangle + 50% = an oval, not a pill.
- Use a pill shape for long, multiline content
- Assume more rounding always feels friendlier

Anatomy

Content

1RadiusThe arc size of the corners, the four corners can be set separately

2BorderThe rounded corners follow the arc of the border

3ContentNot clipped by rounded corners by default unless overflow: hidden

Variants

Small

When you want to retain a clearer edge; select according to component size

Medium

When a balance between edge and soft contours is required

Large

When you need a more obvious arc; first check the content space and nesting relationship

Circle

Square avatar, status point or round icon container

Pill

When long labels or buttons require complete arcs at both ends

Typical use cases

Button corners

border-radius: 12px

**Message notification**

**Dark mode**

Card surface

![](/assets/avatar-fox.png)50% perfect circle

**Little Fox** · 2 hours ago

This rounded corner tutorial is so easy to understand, I have saved it!

Avatar

![](/assets/photo-cat.png)

**Front-end entry training camp**

Hot Sale
New

+ Follow

**border-radius: 999px** is the CSS writing method that allows this example to achieve a capsule outline, and is not a fixed value for all components

Tag

Controls with the same visual role use the same radius token

Search

border-radius
box-shadow
flex layout

Further reading

[border-radiusMDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/border-radius)
