---
type: web_source
source_url: "https://vibe-hub.org/en/fade"
title: "Fade In / Out"
language: en
category: "fade"
fetched_at: 2026-07-27T10:05:14+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←SpringTransition→

# Fade In / Out

You might say

When the content changes, fade the old content out and the new content in.

**Reveal or hide an element by changing its opacity**·A fade is a simple transition between transparent and visible states. It works for overlays, messages, and content replacement, but opacity alone does not explain where an element came from. Combine it with small spatial motion only when that adds useful context.

Know first

[Opacity](/en/opacity)[Transition](/en/transition)

Frame indication: opacity 0 → 1, while gently moving up

### When to use it

- Show or hide an overlay
- Replace a small piece of content

  Slow entranceQuick exit
- Introduce a toast or status message

  The old fades out; the new fades in.
- Soften a non-spatial state change

  opacitytransform

### When NOT to use it

- Fade critical content so slowly that work is delayed

  All statesAll statesIn progressThe menu only fades in place, with no origin or directional cue.
- Use opacity to hide an element that remains unexpectedly interactive

  fadeDuration too long

  A fade-in that is too slow delays the sense that content is ready.
- Combine large movement with every fade

  At opacity: 0 it still takes up space and blocks clicks underneath.
- Use repeated fades around text people are reading

  Dialog fadeScale fadeSlide fade

  Using only fades for every change weakens hierarchy and directional cues.

Anatomy

transform: translateY(8px)animation-duration: .2s

1OpacityOpacity changes from 0 to 1, taking the element from transparent to visible

2OffsetA small translate offset gives the entering element a more natural motion

3DurationThere is no universal duration; choose one based on travel distance, task urgency, and reduced-motion preferences.

Variants

Pure Fade

For overlay or placeholder content that should appear without drawing attention

Fade In Up

For a card or modal entering the page

Cross Fade

For switching carousel or tab content

Typical use cases

Overlay

New project

CancelCreate

The mask fades in synchronously with the pop-up window, and uses slight displacement to express the entry direction

Toast

✓ Saved
Entry fade-in, the duration is adjusted according to the task

✓ Saved
Exit fade-out, you can use a faster pace

Image loading

Introduction
Comments 12
Related articles

![](/assets/avatar-fox.png)**New News**: A new item has been added to the short entry animation prompt list

Old content (afterimage) fades out, new content fades in, and cross-fade does not interrupt the line of sight

Content swap

fade-in  
300ms  
→

![](/assets/cover-mountain.png)

Weekend hiking route

Read about 4 minutes

The first screen content fades in as a whole + moves up slightly, without flashing or jumping

Further reading

[opacityMDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/opacity)
