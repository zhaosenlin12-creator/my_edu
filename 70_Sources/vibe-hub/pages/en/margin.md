---
type: web_source
source_url: "https://vibe-hub.org/en/margin"
title: "Margin"
language: en
category: "margin"
fetched_at: 2026-07-27T10:05:04+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←SpacePadding→

# Margin

You might say

This block is too close to the one next to it. Add a little more space between them.

**Create space outside an element**·Margin controls the space between an element and the things around it. It helps separate groups, but it does not add room inside a box. Use a shared spacing scale and let the parent layout handle repeated gaps when possible.

Know first

[Space](/en/space)

Card A24Card B

### When to use it

- Separate one block from another
- Add outer breathing room around a component

  margin: 0 auto centers a fixed-width block.
- Push a section away from its neighbors

  Use margin-bottom uniformly, and the spacing is only in one direction.
- Adjust one edge without changing the content area

  ★Save

### When NOT to use it

- Use margin to create room inside a box

  Block A · margin-bottom: 20↕ Combined into 20 (not 32)Block B · margin-top: 12
- Stack several margins until the result is hard to predict

  margin ↔ adds space outsidepadding ↔ adds space inside**Content**
- Choose unrelated values throughout the same page

  A negative margin makes an element overlap the section before it.
- Use negative margin as the default way to fix layout

  An empty div used only to create spacing

Anatomy

Content

1MarginTransparent space outside the border, used to separate adjacent elements

2BorderThe boundary of the element, beyond which is the territory of margin

3PaddingBetween content and border, with background color

4ContentThe place where words and pictures really stay

Variants

16px

margin: 16px

Use it when all sides need to be evenly spaced

margin-bottom

TitleText

Paragraphs and fields only leave space downwards

0 auto

auto

Fixed-width containers are centered on the page

Negative

Cover imageTitle bar

Fine-tune alignment or deliberately layer a little more

Typical use cases

Section spacing

**This week’s orders**+12%

1,284

↕

margin-bottom: 16px

**Latest news**

Little Fox commented on "Home Page Revision"

Card separation

**v2.4 update log**

margin-top: 8px

Added dark mode and component search, and fixed 12 known issues.

margin-top: 24px, new chapters stay away

**v2.3 update log**

Form groups

**Login account**

For fixed-width cards, write **margin: 0 auto**, and the remaining space will be automatically divided equally on both sides

Page rhythm

★Collection

✕ The icon is 2px higher and not aligned

★Collection

✓ margin-top: 2px fine-tuned and aligned

Further reading

[marginMDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/margin)[Mastering margin collapsingMDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_box_model/Mastering_margin_collapsing)
