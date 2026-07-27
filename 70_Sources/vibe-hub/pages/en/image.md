---
type: web_source
source_url: "https://vibe-hub.org/en/image"
title: "Image"
language: en
category: "image"
fetched_at: 2026-07-27T10:04:54+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←EmptyFile→

# Image

You might say

Let me add images to the article, and make sure they don't get distorted on phones.

**Display an image with the right size, crop, and fallback**·An image component can handle aspect ratio, cropping, lazy loading, preview, and loading failure consistently. Reserve its space to prevent layout shifts. Meaningful images need alternative text; purely decorative images should be ignored by screen readers.

🔍 Preview

⚠  
Loading failed

Image**≠**[Icon](/en/icon)

[Image](/en/image) shows a photo, illustration, or the content itself. icon is a small reusable symbol for an action or status.

Image**≠**[Video](/en/video)

[Image](/en/image) is one static frame. video has time-based content such as play, pause, duration, and sound.

### When to use it

- Product and article media

  CoverProduct image
- Profile or team photos

  Thumbnail→ ClickEnlarge preview
- Responsive thumbnails

  ⚠ Couldn’t loadShow a placeholder and explanation when loading fails
- Images that need preview or loading states

  The container is square and the image is wide; crop to fill without distortion

### When NOT to use it

- Stretch an image into the wrong ratio

  Forcing the dimensions stretches the image out of proportion
- Load full-size files for tiny thumbnails

  Loading many images at once noticeably slows the page
- Leave a broken-image icon with no fallback

  Product launch · 50% off for a limited timeText that exists only in an image can’t be searched or read by screen readers
- Write alternative text that adds no useful meaning

  ⚠ Couldn’t loadWithout alt text, there’s no description if the image fails to load

Anatomy

🔍 Preview

1ImageDecide on size and cut

2ImgWhat is really shown

3MaskHover to appear, click to enlarge

Variants

Cover

The proportion of the container is fixed and it would rather be cut off than deformed.

Contain

The content of the picture cannot be cropped, and the whole picture must be read even if the margins are left.

Circle

Special for avatars, cut into rounded corners

Fallback

⚠  
Loading failed

Placeholder when image loading error occurs

Typical use cases

Product photo

Desktop lifting table

¥1,299

Outdoor mountaineering bag 40L

¥459

Article cover

![](/assets/avatar-fox.png)

**Alex Chen** · 2 hours ago

This set of scene diagrams is so intuitive that it has been copied into the team specifications 👍

![](/assets/avatar-robot.png)

**maya-lee** · 5 hours ago

Zhengchou how to explain the empty status to newcomers, forwarded

Gallery preview

Article image (preview mask appears when hovering):

🔍 Preview

User profile

🖼️ Image loading failed

alt="Mountain Hiking Route Real Shots" —— Placeholder and explanatory text are still displayed when loading fails.

Further reading

[<img>: The Image Embed elementMDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)[Learn Imagesweb.dev ↗](https://web.dev/learn/images)
