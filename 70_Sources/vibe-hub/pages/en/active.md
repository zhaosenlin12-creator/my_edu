---
type: web_source
source_url: "https://vibe-hub.org/en/active"
title: "Active"
language: en
category: "active"
fetched_at: 2026-07-27T10:05:12+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←HoverFocus→

# Active

You might say

When someone presses the button, make it feel like it's being pushed in.

**Show that a control is being pressed right now**·The active state appears during the press between pointer down and release. A small change in color, depth, or scale confirms that the input was received. It is different from a selected item that stays chosen after the interaction.

Hold me
Hover only
List items press too
Hold to see the sink (scale .96), release to bounce back; the right button lacks active and feels dead

### When to use it

- Give a button press physical feedback

  Button→Button
- Show a menu item while it is being clicked

  SubmitSubmit
- Respond to a pointer or key press

  Immediate press feedback
- Complete the hover-focus-active state set

  List item oneList item two (pressed)List item three

### When NOT to use it

- Use active styling as the permanent selected state

  HoverPressed
- Scale a control so far that the layout jumps

  Confirm
- Remove all feedback during a press

  Button
- Make the pressed state look disabled

  Pressed statePressed is temporary; it cannot replace a persistent selected state.

Anatomy

Button👇 Press instantlyButton

1RestHow it looks when nothing is pressed

2PressThe instant between pointer-down and release

3Sinkscale .97 or a darker color — the feeling of “it registered”

Variants

Scale

ButtonButton

The standard press feedback for buttons

Darken

ButtonButton

The fallback when scaling isn't an option

Inset

Button

Physical feel for toggles and levers

Typical use cases

Button press

Order Total**¥ 199.00**

Pay Now

On press: scale(.97) + darker color — you can feel the click

Navigation item

Account & Security›

Notifications›

Privacy›

List item press: darker background + slight sink

Icon control

Me

Favorites

Messages

Settings

Card action

⏮

▶
⏭

Icon button press: shrinks with a ripple

Further reading

[:activeMDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/:active)
