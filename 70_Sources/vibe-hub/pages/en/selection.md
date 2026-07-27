---
type: web_source
source_url: "https://vibe-hub.org/en/selection"
title: "Selection"
language: en
category: "selection"
fetched_at: 2026-07-27T10:05:16+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←CursorHover→

# Selection

You might say

Change the text highlight color to our brand color when people select text.

**Show which text or items the user has selected**·Selection highlights the text, rows, files, or objects included in the next action. Keep it distinct from hover and focus, and make the selected set remain clear while menus or toolbars open. The visual state should match the actual data selection.

Default

Drag to select some text, the part in the middle is the highlight, with colors picked by the browser.

Brand

Drag to select some text, the part in the middle is the highlight, echoing the brand color.

### When to use it

- Highlight selected text

  Drag to select some text, this part is selected, and the colors are determined by the browser and operating system.
- Choose rows for a bulk action

  In the same sentence, Use the brand color for selection, first confirm its contrast and scope.
- Select files or canvas objects

  Dark background, white text ✓Light background, dark text ✓
- Keep a current item visibly chosen

  Saveuser-select: none

### When NOT to use it

- Use the same style for hover, focus, and selection

  In this sentencepart of it is selected, but the state is not clear.
- Clear a multi-selection without warning

  Button label selectedDragging over the click target accidentally selected the button label.
- Show a selected appearance before the data is selected

  SelectionSelectionSelection
- Rely on color alone for important item selection

  The body copy uses user-select: none, so people cannot select and copy what they need.

Anatomy

The previous paragraph is not selected, This paragraph was dragged and selected, and the rest was not selected

1TextThe unselected part stays exactly as it was

2SelectionThe span of text covered by the mouse drag

3BackgroundThe background of ::selection

4ColorThe color of ::selection; must contrast enough with the background

Variants

Default

Selection

When the browser default already meets the product's needs

Brand

Selection

A low-cost, polished nod to your brand color

NoSelect

Drag handle · user-select: none

Drag handles or interaction-only decoration that should not be selected

Typical use cases

Text selection

Three Habits for Better Prompts

When writing a prompt, state your goal first, then give context. The model can't read your mind, so list every key constraint clearly instead of expecting it to guess.

📋 Copy

Table rows

1.card {

2  border-radius: 12px;

3  padding: 16px;

4}

File browser

Save Draft
✕ Meant to click, dragged a blue streak

Save Draft
✓ user-select: none prevents mis-selection

Design canvas

MUSEON STUDIO

Let good ideas be seen by the world

Selection color = brand color, one line of ::selection

Further reading

[::selectionMDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/::selection)[user-selectMDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/user-select)
