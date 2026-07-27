---
type: web_source
source_url: "https://vibe-hub.org/en/form"
title: "Form"
language: en
category: "form"
fetched_at: 2026-07-27T10:04:49+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←UploadColorPicker→

# Form

You might say

Build a sign-up page where people fill in their information and submit it.

**Collect several fields and submit them as one task**·A form organizes multiple inputs into a task such as creating an account or placing an order. It needs clear labels, validation, error placement, submission state, and a final result so people know what to fix and whether their data was saved.

Know first

[Input](/en/input)[Button](/en/button)

Name

Email✕ Enter a valid email address

City

Shenzhen

Shenzhen*✓*
Guangzhou*✓*
Hangzhou*✓*

SaveCancel

Form**≠**Fieldset

A [Form](/en/form) collects and submits a complete task. A fieldset only groups related fields inside a form and commonly uses a legend to name the group.

### When to use it

- Account registration

  oil-oil••••••••

  Sign in
- Checkout

  NameAlex Chen

  Email*you@example.com*
- Create or edit a record

  Emailoil-oil@abc

  ✕ Invalid email format
- Any task that submits several related fields

  NameAlex Chen

  CityShenzhen

  Notifications

  Save

### When NOT to use it

- Ask for information that is not needed for the task

  Search form

  *Enter keywords…*Submit

  One search field doesn’t need extra form structure
- Clear every field after one error

  Too many fields on one page make the form burdensome
- Show only a generic error at the top

  Password123

  Submission failed: password must be at least 8 charactersThe rule is hidden until submission fails
- Allow repeated submission while the first request is running

  Versionv2.4.0

  Authoroil-oil

  Putting read-only information in fields makes people think they can edit it

Anatomy

Email✕ Enter a valid email address

Save

1Form ItemA complete unit of a field: label + control + error

2LabelTells users what to enter

3ControlThe control where someone enters or chooses a value

4ErrorA nearby message that explains how to fix a validation error

5ActionsSubmit or cancel actions; make the primary action most prominent

Variants

Horizontal

Name

Save

When there are fewer fields and the page is wider, place the label on the left

Vertical

Name

Save

When there are many fields or the page is narrow, place the label above the input box

Inline

All status

All status*✓*
In Progress*✓*
Completed*✓*

Query

When filter controls and the search action should stay on one row

Validation

Email✕ Enter a valid email address

When validation fails, explain the error next to the affected field.

Typical use cases

Registration

LoginRegister

Log in

Checkout

Nickname

City

Shenzhen

Shenzhen*✓*
Guangzhou*✓*
Hangzhou*✓*

SaveCancel

Project settings

New project

Template: Blank project

Template: Blank project*✓*
Template: Product Introduction*✓*
Template: Data Kanban*✓*

CancelCreate

Contact form

All status

All status*✓*
In Progress*✓*
Completed*✓*

Last 7 days

Last 7 days*✓*
Last 30 days*✓*
This year*✓*

QueryReset

Order #20260721-018Completed¥ 329

Order #20260721-017In progress¥ 89

Further reading

[<form>: The Form elementMDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)[Learn Formsweb.dev ↗](https://web.dev/learn/forms)
