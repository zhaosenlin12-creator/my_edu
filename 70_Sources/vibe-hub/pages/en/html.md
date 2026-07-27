---
type: web_source
source_url: "https://vibe-hub.org/en/html"
title: "HTML"
language: en
category: "html"
fetched_at: 2026-07-27T10:05:27+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←MarkdownFrontend→

# HTML

You might say

The code AI wrote has a bunch of angle brackets and English words. What are those for?

**Describe the structure and meaning of a web page**·HTML organizes a page into headings, paragraphs, links, forms, images, and other meaningful elements. CSS controls appearance and JavaScript adds behavior. Choosing the right element improves accessibility, keyboard behavior, search, and maintenance.

<html>
<head> *Meta information*
<body>
<h1> *Title*
<p> *Paragraph*
<a> *Link*

→

**Xiaoli's homepage**
I like hiking and taking pictures. 
View my photo album →

### When to use it

- Build page structure

  A project report for people to readClear headings, highlights, images, and sections  
  Help readers quickly scan for what matters to them.HTML turns content into a reading experience.
- Mark headings and sections

  🔒 report.example.com/launch

  **New product launch report**Open page

  Send a URL and anyone can view it in a browser.
- Create forms and links with native behavior

  ▶ Video↗ LinkFill out form

  A page can provide interactive elements such as media, links, and forms.
- Give content machine-readable meaning

  # Launch plan  
  - Launch this week→**Launch plan**· Launch this week

### When NOT to use it

- Use generic div elements for every role

  <div> card  
  The content that follows may still be inside this element…A missing </div> makes the DOM structure differ from what you expect.
- Choose tags only for their default appearance

  <b><i>text</b></i>The tags overlap improperly; the browser may rearrange them during error recovery.
- Skip heading levels to get a larger font

  <head> Welcome to my websiteThe structure is invalid; the browser may move the content into body during error recovery.
- Put unsafe user content directly into HTML

  Windex.html → Save as .docx

  DOCX is not HTML; browsers do not parse it as page structure.

Anatomy

<a href="https://vibe.guide">Click to see</a>

1Opening TagAdd angle brackets to the tag name to tell the browser "Start here"

2AttributeAdditional information written in the start tag, such as link address and image path

3ContentThe part between the two pairs of angle brackets, only change this part when modifying the copy.

4Closing TagAn extra slash tells the browser "end here"

Variants

div

<div> … </div>

Use it to organize content and layout when there are no more appropriate semantic tags

Headings & p

<h1> <p>

Titles and paragraphs, the skeleton of the article

Link & Image

<a> <img>

a jumps to the URL, img posts the picture

Button & Input

<button> <input>

Interactive parts that can be clicked and filled on the page

Typical use cases

Page document

Help me make a personal homepage

Okay, here is your index.html:

<h1>Xiaoli's homepage</h1>
<p>I like climbing mountains and taking pictures. </p>
<a href="/photos">View my photo album</a>

Article

view-source:https://my-first-page.vercel.app

1 <h1>Xiaoli’s homepage</h1>  
2 <p>I like hiking and taking pictures. </p>  
3 <a href="/photos">View my photo album</a>

Form

**Xiaoli's homepage**

I like hiking and taking pictures.

View my photo album →

<h1>…</h1>  
<p>…</p>  
<a>…</a>

Navigation

Common tag recognition

**<div>** Universal container

**<p>** Paragraph

**<a>** Link

**<img>** Picture

**<button>** Button

**<input>** Input box

Further reading

[Structuring content with HTMLMDN ↗](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content)[HTML: HyperText Markup LanguageMDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTML)
