---
type: web_source
source_url: "https://vibe-hub.org/en/centering"
title: "Centering"
language: en
category: "centering"
fetched_at: 2026-07-27T10:05:19+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←PositionBox Model→

# Centering

You might say

Can you center this box both horizontally and vertically? Why is that always so hard?

**Align an element to the middle of the available space**·Centering may mean horizontal alignment, vertical alignment, or both. Text can use text alignment, a fixed-width block can use automatic margins, and flexible layouts can use flex or grid. Start by identifying what should be centered inside which container.

Know first

[Flex](/en/flex)[Grid](/en/grid)

flex

grid

absolute

### When to use it

- Center text inside a heading or button

  Sign inSet both the main and cross axes to center.
- Center a fixed-width content column

  display: grid + place-items: center gets it done in two lines.
- Center an empty state in a panel

  Headline centered horizontallytext-align: center only handles the horizontal axis.
- Align an item on both axes in a known container

  margin: 0 auto centers a fixed-width block.

### When NOT to use it

- Use absolute offsets without knowing the container size

  table-cell can center content, but flex or grid is usually more direct for new layouts.
- Center long body text when left alignment is easier to read

  Positioning with a fixed margin shifts when the container gets wider.
- Add spaces or line breaks until something looks centered

  With only left/top: 50%, the element grows down and right from the center.
- Apply centering to the whole page when only one child needs it

  Without a fixed width, margin: 0 auto cannot center it.

Anatomy

ElementMain axis: justify-content: centerCross axis: align-items: center

1ContainerSet display: flex on the parent so it controls how its children are aligned.

2Centered ItemThe child element being centered

3Justify Contentjustify-content: center aligns the child along the main axis.

4Align Itemsalign-items: center aligns the child along the cross axis.

Variants

Flex

The most commonly used centering method in ordinary containers

Grid

It is most economical when the parent element is already grid

Absolute

It’s common in old codes, just recognize it

Typical use cases

Empty state

Login Vibe

Log in

Dialog content

![](/assets/empty-box.png)

No favorites yet

Go shopping and collect your favorite components

Login panel

New feature available

Write the front end like chat

Describe the effect you want and leave the rest to AI

Try it now
View demo →

Loading indicator

Why is centering so difficult?

Further reading

[Centering in CSS: A Complete GuideCSS-Tricks ↗](https://css-tricks.com/centering-css-complete-guide/)
