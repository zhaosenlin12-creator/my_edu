---
type: web_source
source_url: "https://vibe-hub.org/en/easing"
title: "Easing"
language: en
category: "easing"
fetched_at: 2026-07-27T10:05:14+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←AnimationSpring→

# Easing

You might say

This animation feels choppy. Can it speed up and slow down more naturally?

**Control how motion speeds up and slows down**·Easing changes the pace of a transition or animation over time. Ease-out often feels responsive for an element entering, while ease-in can suit an element leaving. Choose a small motion set and judge it in the real interaction, not from curve names alone.

Know first

[Transition](/en/transition)

ease-out entryease-in exitlinear machinery

### When to use it

- Make entering motion settle naturally

  ease-out: starts fast, then slows to a stop.
- Let an exiting element accelerate away

  ease-in: starts slowly, then accelerates away.
- Give repeated interactions a consistent rhythm

  Four cubic-bezier values can shape any curve.
- Tune a transition without changing its path

  --easeButtonCardDialog

  Reuse a small set of curves by motion type to balance consistency with context.

### When NOT to use it

- Choose a curve only because its name sounds right

  linear keeps a constant speed and does not suit every entrance movement.
- Use dramatic bounce for routine controls

  Using ease-in for entrance can make the initial feedback feel sluggish.
- Mix many easing curves in one flow
- Make the beginning so slow that input feels delayed

  Both ends overshoot and rebound out of control; use a spring when you need elasticity.

Anatomy

Horizontal axis: time →Vertical axis: progress ↑

1CurveThe curve maps time to progress. Its slope is the animation’s instantaneous speed: a steeper slope moves faster, while a flatter slope moves slower.

2TimeThe horizontal axis represents time from the start to the end of the animation

3ProgressThe vertical axis represents the fraction of the property change that has completed

Variants

ease-out

Entering and appearing, first quickly and then steadily.

ease-in

Exit and disappear, speed up and leave

ease-in-out

Switch to the original state, both ends are soft

cubic-bezier

Fine-tuning for a unique brand feel

Typical use cases

Panel opening

B
I
🔗

Publish
🖱️

ease-out: The color changes first quickly and then slowly, and the fingers can feel "following the hand"

Menu closing

New version v2.4 is ready

Restart the application to complete the update.

LaterUpdate now

ease-out entry: rush in quickly and "brake" to a stop before reaching the point

Card movement

✓ Saved

✓ Saved

↑

ease-in: start slowly, then accelerate away

Page transition

Design specifications · Animation Tokens

`--ease-standard`
cubic-bezier(.2,.8,.2,1)

Button hover
Pop-up admission
Card floats
Use this one all

Further reading

[<easing-function>MDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/easing-function)
