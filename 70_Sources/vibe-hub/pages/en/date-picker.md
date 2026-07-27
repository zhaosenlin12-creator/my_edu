---
type: web_source
source_url: "https://vibe-hub.org/en/date-picker"
title: "DatePicker"
language: en
category: "date-picker"
fetched_at: 2026-07-27T10:04:47+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←TreeSelectTimePicker→

# DatePicker

You might say

Give people a calendar to choose a date instead of making them type it in.

**Choose a date or date range from a calendar**·A date picker reduces ambiguity by showing dates in a calendar. It may select one day or a range. State the allowed dates, whether the start and end days are included, and which time zone applies when people work across regions.

Know first

[Input](/en/input)

2026-07-21*📅*

‹**July 2026**›

MonTueWedThuFriSatSun

293012345
6789101112
13141516171819
20212223242526
272829303112

### When to use it

- Appointment date

  2026-07-21

  July 2026

  MonTueWedThuFriSatDay

  20212223242526
- Travel dates

  07-10→07-17

  1011121314151617
- Report range

  Choose an appointment date

  19202122232425

  Past dates can’t be selected
- A date with clear availability rules

  TodayLast 7 daysLast 30 days

  07-15 ~ 07-21

### When NOT to use it

- Use a calendar for a year that is faster to type

  Date2026/7/32

  A manually entered date can have both an invalid format and an invalid day
- Allow impossible ranges without feedback

  14:30

  131415

  003045
- Hide disabled-date rules

  13141516171819

  For a broad range, a full calendar adds unnecessary effort
- Mix date formats without explaining them

  FrontendBackendDesign

Anatomy

7 Month›1314151617181920212223242526

1TriggerShow the selected date in a consistent format

2HeaderUse the navigation controls to change the year or month

3Day GridA seven-column grid that shows every day in the month

4Day CellAn ordinary date; highlight it on hover

5Selected DayThe selected date, shown with a solid highlight

Variants

Single

1314151617181920212223242526

To select a single date, such as a birthday or due date

Range

07-10

*→*

07-17

1011121314151617

When someone needs to select a date range

Disabled

19202122232425

Past dates are unavailable

When a date is unavailable, explain why before someone selects it

Shortcuts

TodayLast 7 daysLast 30 days

07-15 ~ 07-21

Offer common date ranges as quick picks

Typical use cases

Booking

**Operating Report**
Last 7 days
07-15 ~ 07-21*📅*

Sales

¥ 82,410

▲ 12.4%

Order volume

1,286

▲ 8.1%

Price per customer

¥ 64

▼ 2.3%

Travel search

**Book an in-person session**

Choose an arrival date. Gray dates are fully booked.

2026-07-23*📅*
Confirm reservation

MonTueWedThuFriSatSun

20212223242526

Analytics filter

**Website 2.0 launch**In progress

Owner
![](/assets/avatar-fox.png)Alex Chen

Deadline
2026-07-31*📅*

10 days left · The owner will be notified if the deadline passes

Deadline setting

Shenzhen ⇄ Hangzhou
Check-in 07-24
→
Departure 07-27
Search

MonTueWedThuFriSatSun

20212223242526

272829303112

Further reading

[<input type="date">MDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date)[Date Picker Dialog ExampleWAI-ARIA APG ↗](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/examples/datepicker-dialog/)
