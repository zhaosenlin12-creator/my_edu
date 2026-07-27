---
type: web_source
source_url: "https://vibe-hub.org/en/markdown"
title: "Markdown"
language: en
category: "markdown"
fetched_at: 2026-07-27T10:05:27+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←StateHTML→

# Markdown

You might say

The document AI wrote is full of # signs and asterisks. What is that, and can it turn into nicely formatted text?

**Write structured text with lightweight punctuation**·Markdown uses simple characters for headings, lists, links, code, and emphasis. It is convenient for documentation and content stored as plain text. Different renderers support different extensions, so preview the actual output and treat embedded HTML carefully.

SOURCE · Source code

**#** Weekend Plan
**\*\***Hike the mountain**\*\*** on Saturday, start early
**-** Bring water and snacks
**```**
npm run dev
**```**

→

RENDERED · After rendering

Weekend Plan
**Mountain climbing on Saturday**, start early
Bring water and snacks
npm run dev

Markdown**≠**Rich-text editor

Markdown uses punctuation for headings, bold text, and lists, so you edit plain text. A rich-text editor shows formatted content directly, like a familiar document app.

### When to use it

- README and documentation

  **#** Requirements  
  **-** The home page needs a sticky navigation bar  
  **-** Use blue buttonsUse headings and lists to express requirements so AI can recognize the hierarchy.
- Notes and knowledge bases

  **Weekend plan**  
  · **Saturday**Hiking  
  · Rest on SundayMany chat products render Markdown-style text as headings and lists.
- Content that needs version control

  Two columns for side-by-side comparison.
- Text with headings, links, lists, and code

  README.md  
  **#** My first page  
  **##** How to run  
  **-** npm installPlain text works in many editors, making it easy to save and review over time.

### When NOT to use it

- Assume every Markdown renderer behaves the same

  # Weekly update \*\*completed\*\*: home-page redesign - bug fixesThe target chat box does not parse Markdown, so # and \*\* appear literally.
- Use complicated tables for layout

  Wnotes.md → Save as notes.docx

  Conversion may change Markdown structure or escape some characters.
- Insert untrusted HTML without sanitizing it

  Price　　　¥199  
  In stock　　　42Markdown collapses consecutive spaces; use a table or list for layout.
- Expect precise visual design from plain Markdown alone

  ```  
  npm run dev  
  The body text below also became codeA missing closing backtick makes the following content parse as a code block.

Anatomy

# Weekend Plan
\*\*Mountain climbing on Saturday\*\*, start early
- Bring water and snacks
```npm run dev```

1Heading# represents the first-level title, ## represents the second-level title; the specific font size is determined by the renderer style.

2BoldUse \*\* to clamp the words and make them bold after rendering; \* An asterisk is italic

3List- At the beginning, one item per line; add a number in front to form an ordered list

4Code FenceThree backticks, one line above and one below, and the content in the middle is displayed as equal width.

Variants

Heading

**#** First-level title**##** Second-level title

Organize chapters by content hierarchy; whether to retain only one first-level heading is determined by publishing specifications

Bold & List

**\*\***Key points**\*\*****-** The first item

Emphasize key points and list matters

Code Fence

**```**npm run dev**```**

Paste the command and code and display them as they are with equal width.

Link & Image

[Text](Website)![Picture](Address)

The picture has one more exclamation mark than the link

Typical use cases

README

maya-lee / **my-first-page**Public

CodeIssuesPull requests

My first page

The personal homepage written for me by **AI** has been deployed to Vercel.

· Changed avatar over the weekend  
· Add blog page next week

npm run dev

Documentation

Write a weekend plan for me

Weekend Plan

**Saturday**: Hiking, remember to bring water

· Rest at home on Sunday

This chat product renders Markdown style text into titles, lists and codes

Blog draft

# Weekend plan  
\*\*Saturday hiking\*\*  
- Bring water and snacks

Weekend Plan

**Saturday mountain climbing**

· Bring water and snacks

Typora / VS Code preview: write symbols on the left and effects on the right

Project notes

# Weekly Report \*\*Completed this week\*\*: Home page redesign - 3 bugs fixed

The # and \*\* here are not parsed

The chat box does not render Markdown → convert it to plain text first, or send a screenshot directly
