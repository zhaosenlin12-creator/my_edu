---
type: web_source
source_url: "https://vibe-hub.org/en/segmented"
title: "Segmented"
language: en
category: "segmented"
fetched_at: 2026-07-27T10:04:53+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←TabsCollapse→

# Segmented

You might say

Put two or three choices side by side so people can tap one to switch, like the iPhone control.

**Switch quickly between a few short, exclusive modes**·A segmented control keeps several short options visible together. It often changes a view, sort order, or time range and usually does not navigate to a new page. If options are numerous or their labels are long, choose another control.

Know first

[Radio](/en/radio)[Tabs](/en/tabs)

*Segmented Control*

EventsKanbanCalendar

Segmented**≠**[Button](/en/button)

[Segmented](/en/segmented) contains mutually exclusive choices: selecting one clears another. A [Button](/en/button) or button group runs actions and does not imply exclusive options.

### When to use it

- List or grid view

  ListKanbanCalendar
- Short time ranges

  PreviewSource

  The content stays the same; only the view changes
- Sort mode

  DayWeekMonth

  A small set of short labels is easy to scan
- A few mutually exclusive display modes

  TodayThis weekThis month

### When NOT to use it

- Use it for many long choices

  OverviewSettingsLogs
- Treat it as primary page navigation

  AllFrontendBackendDesignOperationsTestingToo many options squeeze each label and make scanning harder
- Use icons whose meaning is not obvious

  PriorityLowMediumHigh

  Submit

  If it only takes effect on submit, radio buttons are clearer
- Use it as an on-off setting; choose a [Switch](/en/switch)

  OnOff

  For two states, a switch is easier to use

Anatomy

ListKanbanCalendar

1SegmentedThe overall container, with a rounded gray background

2ActiveThe white highlight that indicates the current value

3SegmentThe remaining options; users can select them with a click.

Variants

Default

ListKanbanCalendar

When a small number of side-by-side views need to be quickly switched at the original position

Icon

☰ List▦ Board📅 Calendar

When labels are too abstract on their own, add icons to help users recognize them

Small

DayWeekMonth

For use in toolbars where space is tight

Typical use cases

View switcher

**Iterative tasks**EventsKanbanCalendar

To-do · 2

Login page UI walkthrough

Integration testing

In progress · 1

Kanban drag and drop sorting

Complete · 5

Requirements Review

Time-range filter

**Visit trend**PolylineColumnPie chart

OneTwoThreeFourFiveSixthDay

Sort control

**Data Center**DayWeekMonth

Active users this week

2,318

This week’s order

486

This week’s revenue

¥36,000

Editor mode

README.mdPreviewSource code

1 **# vibe-ui-guide**

2 Front-end entry component illustration

3 - Each component comes with a screenshot of the real interface

4 - Explain when to use and when not to use

Further reading

[Segmented controlsApple HIG ↗](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)
