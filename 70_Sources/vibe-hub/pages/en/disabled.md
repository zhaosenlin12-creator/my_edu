---
type: web_source
source_url: "https://vibe-hub.org/en/disabled"
title: "Disabled"
language: en
category: "disabled"
fetched_at: 2026-07-27T10:05:13+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←DragCursor→

# Disabled

You might say

Keep the submit button gray and unclickable until the form is complete.

**Show that a control is currently unavailable**·A disabled control cannot be operated in the current state. Use it when the action is visible and its future availability matters, and explain what condition is missing. If the action is irrelevant, removing it may be clearer than leaving a page full of disabled controls.

Submit
Please fill in your email address before submitting
Contrast: Submit
When form conditions are not met, disable submission and indicate missing content nearby

### When to use it

- Prevent submission until required input is present

  SubmitSubmit
- Show an unavailable step that may become available

  lin@example.com*Password (required)*Sign upA required field is still empty, so Submit remains disabled.
- Block an action while the same request is running

  Please enter a password first.Sign up
- Represent a permission or state constraint

  Submitting…

### When NOT to use it

- Disable a control without explaining why

  Buy now
- Use low contrast that makes the label unreadable

  MemberHiding an unavailable entry point permanently may keep people from discovering the feature or how to request access.
- Leave keyboard focus on a control that cannot respond

  Delete project
- Disable most of the page instead of clarifying the workflow

  Submit

Anatomy

Submit🚫 Invalid clickTip: Fill in your email address first

1GreyedReduce visual emphasis while keeping text and status still legible

2BlockedNative disabled usually prevents interaction and focus; aria-disabled only expresses semantics and still requires scripts to prevent operations and determine focus strategies.

3ReasonExplain why the control is unavailable and what will make it available

Variants

Native disabled

Submit

Use native disabled for controls that are truly unavailable; test their appearance and behavior in your target browsers

With Reason

Register*Fill in the password first*

The control will become available after a clear condition is met; show that condition nearby

Hidden

(no rendering)

The action does not apply in this context and needs no explanation; omit it instead of showing a disabled control

Typical use cases

Submit button

Register an account

Register

Complete all required fields to enable Register

Unavailable option

![](/assets/avatar-robot.png)Alex Chen
Guest

Project settings
Edit details
Delete project

Guests can view project settings, but only admins can edit or delete them

Loading action

Mechanical keyboard ×1**¥ 199.00**

Delivery: Alex Chen · Nanshan District, Shenzhen

Submitting order...

Keep the button disabled while the order is being submitted to prevent duplicates

Permission-limited control

![](/assets/photo-cat.png)Sold out

Limited-edition cat figurine

¥ 89 · Restock date not announced

Buy now

Further reading

[aria-disabledMDN ↗](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-disabled)
