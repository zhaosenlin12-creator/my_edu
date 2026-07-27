---
type: web_source
source_url: "https://vibe-hub.org/en/skeleton"
title: "Skeleton"
language: en
category: "skeleton"
fetched_at: 2026-07-27T10:04:58+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←ProgressResult→

# Skeleton

You might say

While the page is loading, show gray placeholder blocks instead of a spinner the whole time.

**Reserve the layout while content is loading**·A skeleton roughly matches the shape of incoming content so the page stays stable during a short load. It should not be a detailed gray copy of every element. For a tiny action or an unknown layout, a simpler loading indicator may be clearer.

### When to use it

- Initial card or list loading
- Profile content with a known shape
- A page where layout stability matters
- Short waits before real content appears

### When NOT to use it

- Show a skeleton for a task with no known layout

  Loading, please wait…
- Keep it running after a request failed

  📎 design-file.sketch66%
- Animate a complex placeholder that distracts from the page

  The actual content is a form, but the skeleton doesn’t match its layout
- Use it to hide a consistently slow experience

  The request failed, but the skeleton never changed to an error state

Anatomy

1SkeletonA set of placeholder color blocks, the shapes aligned with the real layout

2AvatarCircle or square, corresponding to the media position

3Titleshort, thick line

4LineLong and short gray bars, imitating paragraphs

Variants

List Item

Place space when loading information flow and message list

Paragraph

The long article details page is loaded, first lay out the paragraph shape

Card

Pictures and cover cards occupy space before loading

Typical use cases

Article feed

Profile page

Dashboard cards

Search results
