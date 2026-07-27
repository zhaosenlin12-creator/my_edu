---
type: web_source
source_url: "https://vibe-hub.org/en/opacity"
title: "Opacity"
language: en
category: "opacity"
fetched_at: 2026-07-27T10:05:07+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←ShadowGradient→

# Opacity

You might say

This image is stealing too much attention. Make it a little transparent.

**Make an element and its contents more transparent**·Opacity changes the transparency of an entire element, including its children. It can soften secondary or disabled content, but low opacity also reduces text contrast. Use a transparent color when only the background should fade.

100%50%15%

### When to use it

- Soften a disabled visual state

  AvailableDisabled
- Fade an element during a transition

  ✎→✎
- Create a subtle overlay

  Dialog
- Reduce the emphasis of decorative content

### When NOT to use it

- Lower body-text contrast until it is hard to read

  opacity .4rgba .4
- Use opacity when only the background should change

  Body text is too transparent, so its contrast is too low.
- Hide content visually while leaving an unexpected click target

  This opacity: 0 button is still clickable.
- Use transparency as the only sign that a control is disabled

  Opacity compounds across layers, making the resulting color harder to predict.

Anatomy

opacity: 0.45Background shines through

1Backdropsomething seen through

2ElementIf opacity is less than 1, the overall color becomes lighter.

3See-throughThe lower the transparency, the more the background shows through

Variants

0.4

Disable

Unclickable buttons and input boxes

0.8

hover

Secondary icons are usually lighter

0.5

Mask

Darken the page behind the pop-up window

0

0

Use placeholder when doing fade-in animation

Typical use cases

Disabled state

opacity: 0.4 = disabled
Email

Cancel
Submit

Fade transition

**Design specification.md**
✎
⧉
★

The secondary icon usually has an opacity of 0.45, and the hovered one returns to 1

Overlay

Mask rgba(.32), the background is vaguely visible

✓ Saved

Decorative image

Copied link
→
Copied link
→
Copied link
transition: opacity .2s, fade in

Further reading

[opacityMDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/opacity)
