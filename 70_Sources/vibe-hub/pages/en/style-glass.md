---
type: web_source
source_url: "https://vibe-hub.org/en/style-glass"
title: "Glassmorphism"
language: en
category: "style-glass"
fetched_at: 2026-07-27T10:05:53+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←Bento GridNeo-Brutalism→

# Glassmorphism

You might say

Use translucent frosted-glass panels where you can faintly see the background through them.

**Use translucent, blurred surfaces to separate layered content**·Glassmorphism combines transparent color, backdrop blur, light borders, and layered backgrounds. It can make floating controls feel connected to the scene behind them. Readability depends on the background, so important text needs a stable surface and sufficient contrast.

![Album cover](/assets/slide-forest.png)

NOW PLAYING

## After the rain

Arlo Parks · Softly

1:423:56

**01**Slow motionRaveena*3:12*

**02**After the rainArlo Parks*3:56*

**03**Salt airGolden Vessel*2:48*

Design Principles

- Use translucency only where a real layer relationship exists
- Keep text contrast stable across changing backgrounds
- Pair blur with a visible tint and edge
- Limit the number of overlapping glass surfaces
- Provide a clear fallback when blur is unavailable

### When to use it

- Media controls over imagery

  Now playing ▶
- Floating navigation

  Floating card
- A compact overlay or status panel

  Log in
- A visual product with controlled backgrounds

### When NOT to use it

- Place body text on unpredictable transparent backgrounds
- Nest many blurred panels
- Use glass on every card and control

  Full-screen blur can hurt scrolling and animation on lower-powered devices.
- Rely on blur alone to show boundaries

  Insufficient text contrast

Anatomy

Bright background+
Translucent background+
blur blur+
 Semi-transparent white stroke=
Suspended soft shadow

1BackdropThere needs to be perceptible changes in light and shade or color behind the scene, and the blur should not interfere with the foreground.

2TintTransparency adjusts by subject and contrast; no blur behind is visible at full opacity

3blur()The blur value is debugged according to component size and background complexity, and provides filter-free fallback.

4Edge LightThin strokes can enhance material boundaries, and the color and intensity should match the light and dark theme.

5ShadowDrop shadows can lift overlays from the background, but do not require the use of color or a fixed range

AI Prompt

> Glassmorphism interface on a controlled vivid gradient, translucent cards, backdrop blur, 1px semi-transparent white borders, soft colored shadows, stable high-contrast text surfaces

Typical use cases

Media player

![](/assets/slide-forest.png)

Night Voyager

Bucai · My Three Body

1:243:12

⏮▶⏭

Random
 Lyrics
 Radio

Floating navbar

Welcome back

Log in to your Aurora account

you@example.com

••••••••

Log in

Don’t have an account yet? **Free registration →**

Dashboard overlay

**Pulse Data Desk**
This week ⌄

Active users

**Example**

Explanation of calculation method

Conversion rate

**Example**

Explanation of calculation method

Revenue

**Example**

Explanation of calculation method

Visit trends in the past 7 days

Visual landing page

Flying

Wi-Fi

Bluetooth

Do not disturb

Brightness

volume

Further reading

[backdrop-filterMDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter)
