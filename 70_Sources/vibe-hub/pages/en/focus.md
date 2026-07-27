---
type: web_source
source_url: "https://vibe-hub.org/en/focus"
title: "Focus"
language: en
category: "focus"
fetched_at: 2026-07-27T10:05:12+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←ActiveDrag→

# Focus

You might say

I can't tell where I am when I use Tab. Can you add a clear focus outline?

**Show which element will receive keyboard input**·Focus identifies the interactive element currently controlled by the keyboard or another input method. A visible focus indicator is essential for navigation and form entry. It may differ from hover, but it should be at least as easy to see.

Tab to me
Walk through with Tab — only the visible ring tells you where you are

### When to use it

- Keyboard navigation

  *🔍 Search topics you are interested in…*
- Form field editing

  Save
- Menu and dialog control

  ① Name② Email③ Phone
- Any interactive element that can receive input

  Custom checkbox

### When NOT to use it

- Remove the browser outline without a replacement

  outline: none
- Show focus only after a mouse click if keyboard users need it

  Save
- Use an indicator with too little contrast

  <div onclick>
- Move focus somewhere unexpected after an action

  ② Name① Email③ Phone

Anatomy

Inputting...Stroke 2px+Tab → Next

1TargetThe control currently holding focus

2Focus RingTells everyone “focus is right here”

3Tab OrderThe route the Tab key travels; follows DOM order by default

Variants

Outline

Button

When the browser's default focus style is already clear

Ring

Input

Brand-color outer glow, more modern

Background

Menu item

For focused list and menu items

Typical use cases

Form field

Complete Your Profile

`Tab ⇥` Press to move focus to the next field

Button

![](/assets/avatar-fox.png)

Nice color palette

Focused input: brand-color ring + glow — the cursor is easy to spot

Navigation

Push Notifications

🔊 VoiceOver: “Push Notifications, switch, on”

Dialog

🔍
theme
`⌘K`

Switch to dark mode

Theme & appearance settings

Further reading

[:focus-visibleMDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/:focus-visible)[Understanding SC 2.4.7: Focus VisibleWCAG ↗](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html)
