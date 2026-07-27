---
type: web_source
source_url: "https://vibe-hub.org/en/popconfirm"
title: "Popconfirm"
language: en
category: "popconfirm"
fetched_at: 2026-07-27T10:04:57+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←DrawerPopover→

# Popconfirm

You might say

On delete, ask 'Are you sure?' next to the button instead of opening a big dialog.

**Ask for confirmation next to the action that caused it**·A popconfirm is a small confirmation panel anchored to a button or link. It works for a simple, local action with a short explanation. Use a [Modal](/en/modal) when the risk is high, the explanation is longer, or more information must be entered.

Know first

[Popover](/en/popover)[Modal](/en/modal)

*⚠*Delete this record?

CancelConfirm

Delete

### When to use it

- Remove one item

  ⚠ Delete this record?

  CancelConfirm

  Delete
- Discard a small local change

  Confirm deletion?

  CancelConfirm
- Confirm a reversible table action

  Remove Alex Chen from the team?

  CancelConfirm

  Remove
- Ask a short yes-or-no question in context

  Clear all inputs?

  CancelClear

  Clear

### When NOT to use it

- Confirm a high-risk action with too little explanation

  ⚠ Delete all 1,024 records? This can’t be undone!

  CancelDelete permanently

  Delete all
- Use it for a form or several decisions

  Deleting this project permanently removes its files, members, and settings. Make sure important data is backed up.

  CancelDelete
- Place it where the triggering control may move away

  💡 Drag to reorder

  CancelGot it

  Hover over me
- Ask for confirmation on harmless, easily reversible actions

  Confirm deletion?

  Confirm

  Confirm one more time?

  Confirm

Anatomy

*⚠*Delete this record?

CancelConfirm

Delete

1BubbleA small, unmasked card positioned beside its trigger button

2MessageUse a one-sentence question, often paired with a ⚠ icon

3ActionsOffer Confirm and Cancel; make the confirmation label describe the consequence

4TriggerIt opens on click, and its arrow points to the trigger.

Variants

Default

Remove this member from the team?

CancelConfirm

Remove

For lightweight, recoverable actions where confirmation can prevent mistakes, such as removing a member

Warning

*⚠*Clear all inputs?

CancelClear

Clear

When an action could accidentally clear entered content

Danger

*⚠*Delete this record?

CancelDelete

Delete

For deletion, use a red confirmation button to emphasize the consequence

Typical use cases

Remove tag

*⚠*Delete this record?

CancelDelete

📄 Home page revision.fig
2 hours ago
Delete

Delete row

Remove Alex Chen from the team?

CancelConfirm

![](/assets/avatar-fox.png)Alex Chen · Product Manager
Remove

Discard draft

*⚠*Clear all inputs?

CancelClear

Clear

Leave a group

Unpublish this article? It will return to draft status.

CancelConfirm

📝 Summer Activity Plan
Published
Unpublish
