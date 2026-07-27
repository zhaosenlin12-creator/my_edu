---
type: web_source
source_url: "https://vibe-hub.org/en/spring"
title: "Spring"
language: en
category: "spring"
fetched_at: 2026-07-27T10:05:14+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←EasingFade In / Out→

# Spring

You might say

Give the dialog a small springy bounce when it appears.

**Create motion that settles with weight and elasticity**·Spring motion is defined by physical-style values such as stiffness and damping rather than only a fixed curve. It suits direct manipulation and elements that need to settle into place. Too much bounce makes routine actions feel slow and unstable.

Know first

[Animation](/en/animation)[Easing](/en/easing)

First cross the target value and then return to the stable position: overshoot (overshoot) and rebound

### When to use it

- Drag-and-drop settling

  👆Release ↩

  Release after dragging and it springs back into place.
- Interactive sheet or drawer

  A slight overshoot can add energy to low-risk entrances.
- Reordering items

  Stiffness

  Damping

  Stiffness affects response speed; damping affects how oscillation decays.
- A playful control with direct manipulation

  type: "spring"This configuration enables Framer Motion’s spring model.

### When NOT to use it

- Add bounce to every button

  Repeated rebounds delay the stable state and distract attention.
- Let overshoot cover nearby content

  Confirm transfer of ¥50,000?

  CancelConfirm
- Use a spring where precise timing must match another event

  Too little damping lets oscillation last too long.
- Ignore reduced-motion preferences

  When every element rebounds at once, hierarchy and emphasis weaken.

Anatomy

stiffnessdampingtarget value

1StiffnessStiffness: how strongly the spring pulls toward its target.

2DampingDamping: how quickly the motion loses energy and stops bouncing.

3OvershootThe value briefly passes the target, then settles back into place.

4TargetThe final resting position

Variants

Stiff

For a crisp, restrained feel in a productivity tool

Soft

For a gentle, lively feel in a content or social product

No Bounce

When you want the motion to feel alive without overshooting

Typical use cases

Draggable card

Original position

↩

Home page revision review

Draging...rebound when you let go

spring: Let go and rush back to the original position, overshoot lightly and then stop, as if there is physical quality

Bottom sheet

Invite members

Invite

scale briefly crosses 1 and then returns to a stable value; the afterimage indicates the position of the previous frame

Reordered list

Notification reminder

The slider briefly crosses the target position and then rebounds; the residual image on the left indicates the movement trajectory

Playful toggle

In progress
▾

All status

In progress

Completed

Elastic expansion from the trigger point: scale 0.96 → 1, the dotted line is the previous frame
