---
type: web_source
source_url: "https://vibe-hub.org/en/progress"
title: "Progress"
language: en
category: "progress"
fetched_at: 2026-07-27T10:04:58+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←TooltipSkeleton→

# Progress

You might say

Show upload progress so people don't think the file upload is stuck.

**Show how much of a task has been completed**·A progress indicator helps people understand the state of an upload, installation, or multi-step task. Use a percentage when the total is known; otherwise show ongoing activity without pretending to know the finish time. State success, failure, and cancellation clearly.

Uploading...66%

Progress**≠**[Spinner](/en/spinner)

[Progress](/en/progress) uses a track to show overall completion and can show a percentage when it is measurable. spinner usually marks a brief local wait with no known completion ratio.

Progress**≠**[Steps](/en/steps)

[Progress](/en/progress) shows continuous completion. [Steps](/en/steps) names the stages so people know where they are in a process.

### When to use it

- File upload

  📎 design-file.sketch66%
- Import or export

  Getting started3/5
- Installation

  Storage6.6 / 10 GB
- A task with measurable completion

  Exporting 1,024 records…42%

### When NOT to use it

- Show a fake percentage when progress is unknown

  Loading, please wait…
- Leave a completed task stuck below 100%

  Saved
- Use animation without a readable status

  *66%*Storage used
- Hide failure or cancellation behind the same loading state

  Uploading…12%

  Stuck at 12% for 10 minutes.

Anatomy

Uploading...

66%

1ProgressThe entire component, strip is the most common form

2TrackThe gray bottom slot represents the total amount

3FillThe completed part grows in real time

4LabelWhat is being done, such as "Uploading..."

5PercentSpecific numbers to ease waiting anxiety

Variants

Line

Uploading...66%

Default form, horizontal progress such as uploading and downloading

Circle

*66%*

When the location is tight or you want to highlight the percentage number

Success

Upload completed

After the task is completed, keep the final progress and explain the results

Exception

Network interruption, upload failed

If it fails halfway, stop at the error location and explain the reason.

Typical use cases

Upload

📎 Homepage design draft.fig2.3 / 3.5 MB

Uploading...66%

Data import

*80%*

**Data completeness**
Upload your avatar to unlock all functions
To improve →

Installation

**Storage Space**6.2 / 10 GB used

Photos 3.8 GB · Documents 1.6 GB

Profile completion

⬇ Export order data in batchesIn progress

Exporting the 3rd / 5th file, please do not close the page

Further reading

[<progress>: The Progress Indicator elementMDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress)
