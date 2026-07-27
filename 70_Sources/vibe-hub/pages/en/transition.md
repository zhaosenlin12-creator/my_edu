---
type: web_source
source_url: "https://vibe-hub.org/en/transition"
title: "Transition"
language: en
category: "transition"
fetched_at: 2026-07-27T10:05:13+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←Fade In / OutAnimation→

# Transition

You might say

The button color changes too abruptly. Can it ease into the new color?

**Smooth the change between two visual states**·A transition animates a CSS property when its value changes, such as color on hover or a panel opening. Use it to clarify cause and effect, keep the duration short, and respect reduced-motion preferences. Not every property animates smoothly or cheaply.

Know first

[Hover](/en/hover)[Active](/en/active)

Hover me← it really animates (transition)

Frame by frame: the color eases over instead of snapping

### When to use it

- Hover and focus feedback

  Save→Save
- Open or close a small panel

  transition-property: backgroundtransition-duration: .25stransition-timing-function: ease-out
- Change color, opacity, or transform

  Brief feedbackTest by distanceLarger movement
- Help people follow a state change

### When NOT to use it

- Animate every property with one broad rule

  transition: allEven unintended width and padding changes are animated.
- Use a long transition for frequent controls

  hover

  An overly long color transition makes feedback feel slow.
- Animate layout-heavy properties without checking performance

  ⚡
- Ignore reduced-motion settings

  →

  Transitioning width or height triggers reflow and can be janky.

Anatomy

*Default**→**Hover*transition-property: backgroundtransition-duration: .25stransition-timing-function: ease-out

1TriggerA state change like hover or selection — the starting point of every transition

2PropertyList the properties that should transition; avoid all when unrelated changes may be animated

3DurationHow long it takes; test against distance, task, and motion preferences

4EasingThe speed curve that gives the motion its character

Variants

Color

→

Hover color shifts and selected states

Transform

Lift

Lifts and slide-ins via transform — best performance

Opacity

Fade-in entrances and fade-out exits

Typical use cases

Button hover

Write your thoughts…

Cancel

Publish
🖱️

→

`transition: background .25s ease`

Dropdown opening

New message alerts

Weekly digest email

Dark mode

The knob uses a transform transition; the ghost on the left shows its path

Accordion

![](/assets/cover-workspace.png)

Website Redesign

Updated yesterday

![](/assets/cover-mountain.png)

Hiking Album

2 hours ago

🖱️

![](/assets/slide-forest.png)

Team Offsite RSVP

3 days ago

Transform and shadow provide the hover feedback, then settle smoothly on exit

Theme change

Log out?

Unsaved drafts are kept automatically.

CancelLog out

Modal and mask opacity

ease with opacity

Further reading

[transitionMDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/transition)
