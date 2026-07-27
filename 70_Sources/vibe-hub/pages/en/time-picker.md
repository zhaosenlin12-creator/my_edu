---
type: web_source
source_url: "https://vibe-hub.org/en/time-picker"
title: "TimePicker"
language: en
category: "time-picker"
fetched_at: 2026-07-27T10:04:47+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←DatePickerUpload→

# TimePicker

You might say

Let people choose the time instead of typing it themselves.

**Choose a specific time within allowed hours**·A time picker lets people choose hours and minutes, and sometimes seconds. Make the 12-hour or 24-hour format clear, define the minute step, and show which times are unavailable.

Know first

[Input](/en/input)

14:30

131415

:

003045

### When to use it

- Appointment time

  14:30

  131415

  003045
- Reminder time

  Business hours09:00→18:00
- Business hours

  Every day09:00Sync data automatically
- Schedule with fixed time steps

  09:0009:3010:0010:30

  30-minute increments prevent choosing 09:17

### When NOT to use it

- Ask for seconds when that precision is not useful

  14:30When an exact time matters, include the date too
- Mix 12-hour and 24-hour formats

  MorningAfternoonEvening

  0030

  Choosing “Morning” doesn’t need a minute-by-minute panel
- Offer unavailable times and reject them later

  Time3:00 PM

  Couldn’t parse. Enter a time as HH:mm
- Hide the relevant time zone

  14:30Cross-time-zone schedules should clearly show the time zone

Anatomy

14:30131415

1TriggerShows the selected time

2Time ColumnScrollable columns for hours and minutes

3Time OptionAn available time

4SelectedThe selected time, highlighted in the center

Variants

24-hour

131415

:

003045

When meetings and scheduled tasks need an unambiguous time format

Range

09:00

*→*

18:00

Choose a start and end time

12-hour

010203

:

3045

AMPM

When users prefer AM/PM time

Step

09:0009:3010:0010:30

When availability is limited to approved time slots

Typical use cases

Meeting booking

**New meeting**

Time
14:30
Today · About 1 hour

131415

:

003045

Reminder

**Business hours**Outside of the time, the store automatically displays "Closed"09:00*→*21:30

**Lunch break**No order taking during this period12:00*→*13:30

Store hours

**Daily push**

Every day 08:30 Push to all members

Next push: tomorrow 08:30

Scheduled task

**07:30**Workday · Get up

**09:00**Weekend · Morning Run

+ Add alarm

Further reading

[<input type="time">MDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/time)
