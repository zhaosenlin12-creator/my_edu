---
type: web_source
source_url: "https://vibe-hub.org/en/animation"
title: "Animation"
language: en
category: "animation"
fetched_at: 2026-07-27T10:05:13+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←TransitionEasing→

# Animation

You might say

Make this icon loop through a subtle motion, like gently floating up and down.

**Run a planned sequence of visual changes**·Animation can repeat, play through keyframes, or express a larger state change that a simple transition cannot. Use it to explain progress or spatial relationships, not just to keep the screen moving. Provide a reduced-motion alternative when movement is substantial.

Know first

[Transition](/en/transition)

0%50%100%@keyframes Define the node and the browser fills in the middle

### When to use it

- Loading indicator

  Loading, please wait…
- Onboarding explanation

  0%50%100%

  Break the motion into keyframes and let the browser fill in between.
- Attention to a new but important event

  123
- A multi-stage visual sequence

  Hover color changetransition

  Loading pulseanimation

  State transitions vs. autonomous playback: each has its own job.

### When NOT to use it

- Loop decorative motion near reading content
- Delay a task until an animation finishes

  Hover color change@keyframes

  Simple hover effects can use transition.
- Use movement that conflicts with the interface state

  ↩

  Without fill-mode: forwards, it returns to the initial frame when finished.
- Ignore performance and reduced-motion preferences

  Reduce motion

  Respect the user’s reduced-motion preference.

Anatomy

*0%**100%*2sease-in-outinfinite ⟳

1KeyframesThe node of the action, the intermediate frame is completed by the browser

2DurationHow long does it take to play it all?

3TimingThe speed between each frame, see easing

4Iteration1 entry, infinite cycle

Variants

Once

Entry arrangement, stop at the last frame after playing

Infinite

⟳

Continuous states such as loading and breathing

Alternate

↔

Reciprocating motions such as swinging and flashing

Typical use cases

Loading

@keyframes breathing: transparency 0.4 ↔ 1 loop, telling the user "loading"

Success state

![](/assets/avatar-robot.png)

AI Assistant

Generating reply, will take about 5 seconds...

animation: rotate 0.8s infinite, until the data comes back

Feature tour

Visits

12,480

▲ 8.2%

New user

326

▲ 3.1%

Conversion rate

4.6%

▼ 0.4%

animation-delay: 0msanimation-delay: 100msanimation-delay: 200ms

animation-delay enters the scene one by one, and the page "lights up" rhythmically

Data update

![](/assets/avatar-fox.png)

**New reply** has been added to the list and the changes are marked with a short entry animation

New

![](/assets/avatar-robot.png)

**Robot Assistant** liked your article

1 hour ago

Background highlight flashes once
→
→
Stop at the last frame, no loop

Further reading

[animationMDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/animation)
