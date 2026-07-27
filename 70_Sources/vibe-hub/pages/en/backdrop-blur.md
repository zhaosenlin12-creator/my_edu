---
type: web_source
source_url: "https://vibe-hub.org/en/backdrop-blur"
title: "Backdrop Blur"
language: en
category: "backdrop-blur"
fetched_at: 2026-07-27T10:05:15+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←Corner FeelDark Mode→

# Backdrop Blur

You might say

Make the navigation bar translucent so the content behind it blurs as it scrolls past.

**Blur the content behind a translucent surface**·Backdrop blur creates a frosted-glass effect by blurring what is behind a partly transparent element. It can separate a floating header or overlay while keeping context visible. Always provide enough background color and contrast, because blur support and source imagery vary.

Know first

[Opacity](/en/opacity)

**Mountain Guesthouse · Genting**

At an altitude of 1,200 meters, you can see the sea of clouds when you open the window.

backdrop-filter: blur(12px)

### When to use it

- Floating header over imagery

  Navigation · Frosted glass
- Compact overlay or control surface

  Dialog · Frosted-glass overlay
- Glass-style panel with readable text

  Mountain Lodge · Cloud PeakA glass card over a landscape image feels light and layered.
- Separate a layer without fully hiding the background

  A translucent rgba background + blur: a natural pair.

### When NOT to use it

- Place low-contrast text over unpredictable images

  A solid white background makes blur pointless.An opaque background means the frosted-glass effect cannot work.
- Apply strong blur to many nested surfaces

  A heavy blur covers the entire page.Heavy blur over a large area is both slow and hard to read.
- Rely on blur as the only boundary

  When the background is too transparent and not blurred enough, the body text and background interfere with each other.Ensure text contrast and readability first.
- Ignore browsers or devices where the effect is limited

  Stacking several blur layers on mobile can hurt performance on lower-end devices.

Anatomy

+blur(12px)+rgba white 55%=frosted glass card

1BackdropWhat’s behind the elements: images, gradients, scrolling pages

2blur()The blur radius of backdrop-filter, the larger it is, the harder it is to see

3rgba TintWithout it, blur will not take effect, and it can easily maintain the text contrast.

4Frosted CardThe final effect of the superposition of the three: vague and clear-cut

Variants

Light

Light glass

When the background is bright and text contrast can still be maintained

Dark

Dark glass

Dark basemap or night mode interface

Strong

Strong blur

There needs to be a stronger sense of isolation behind pop-up windows

Typical use cases

Floating navbar

**Dali Ancient City after the rain**

32,000 reads · 486 collections

**One-day cycling route around Erhai Lake**

18,000 reads · 302 collections

**Travel Notes**
Homepage
Destination
My

Media controls

**Mountain Homestay · Genting**

1,200 meters above sea level, open the window and see the sea of clouds

¥ 688 / night
Available to order

Overlay panel

**Save changes before exiting?** 

"Home Page Revision v2" has unsaved changes

Do not saveSave

Glass card

![](/assets/slide-forest.png)

Night Voyager

Bucai · My Three Body

⏮▶⏭

Further reading

[backdrop-filterMDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter)
