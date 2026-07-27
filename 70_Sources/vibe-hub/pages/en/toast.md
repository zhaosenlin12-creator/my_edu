---
type: web_source
source_url: "https://vibe-hub.org/en/toast"
title: "Toast"
language: en
category: "toast"
fetched_at: 2026-07-27T10:04:56+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←AlertNotification→

# Toast

You might say

Show a little 'Saved' message in the corner that disappears after a couple of seconds.

**Briefly confirm a small action that just finished**·A toast is useful for lightweight feedback such as Saved, Copied, or Added. It normally disappears after a few seconds. Do not use it as the only place for an important error, an action the user must take, or information they may need later.

Saved

Save

Trigger interaction exampleThe above is a static gesture, click the button to view the interaction effect

### When to use it

- Confirm save or copy

  Saved
- Acknowledge a small background action

  https://vibe-ui.dev/x/8fk2Copy

  Copied
- Show a brief success message

  Network error. Try again.
- Give feedback without interrupting the current task

  Copied to clipboard

  Disappears in 3 seconds

### When NOT to use it

- Put a long explanation in a disappearing message

  Payment failed

  CancelTry payment again
- Use it for an error that needs correction

  **Review declined**
  View reason →
- Stack so many toasts that they cover the page

  SavedSyncedNetwork error
- Make it disappear before it can be read

  Done

  Did that succeed or fail?

Anatomy

Saved

1ToastA brief message that appears near the edge of the interface

2IconUse icons or text to help identify results

3MessageKeep it short and directly describe the results of the operation

Variants

Success

Saved

The operation is successful and does not require the user to continue processing.

Error

Network error. Please try again.

Use an error toast for a minor failure that only requires a retry.

Info

Copied to clipboard

Status confirmation without success or failure tendency

Typical use cases

Saved

Saved

Save

Copied

Link copied to clipboard

Copy link

This file can be viewed by anyone with the link

Added to favorites

Network error. Please try again later.

Setting updated

3 files moved

☑ 📄 Home page revision.fig
☑ 📄 Design specifications.md
☐ 📄 Release list.md

Further reading

[SnackbarMaterial Design ↗](https://m3.material.io/components/snackbar/overview)
