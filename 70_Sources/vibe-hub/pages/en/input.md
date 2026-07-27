---
type: web_source
source_url: "https://vibe-hub.org/en/input"
title: "Input"
language: en
category: "input"
fetched_at: 2026-07-27T10:04:43+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←LabelTextarea→

# Input

You might say

Add a field where people can enter their email address.

**Let the user enter one line of text**·Use a text input for an account name, nickname, search query, or anything else that fits on one line. Give it a label that stays visible after typing. If the value is invalid, explain what is wrong and how to fix it near the field.

EmailUsed for login notifications — never shown publicly

Invite codeInvite code not found. Check it and try again

Input**≠**Search input

A search input is an [Input](/en/input) with a specific purpose and may include submit, clear, or suggestion behavior. A normal input can collect any short value, such as a name or email.

Input**≠**[AutoComplete](/en/auto-complete)

[Input](/en/input) accepts text. [AutoComplete](/en/auto-complete) offers possible matches as someone types.

### When to use it

- Account and contact details

  oil-oil••••••••

  Sign in
- Search queries

  *🔍 Search topics you are interested in…*
- Short names and titles

  NameAlex Chen

  Email*you@example.com*
- Single-line codes or values

  title2026 Product Plan v3

### When NOT to use it

- Collect a long answer that needs several lines

  This component’s interaction design is very thoughtful…
- Use placeholder text as the only label

  StatusIn progress
- Wait until final submission to reveal every obvious error

  *Name*"Name" disappears after you type.
- Show read-only content in a field that looks editable

  Versionv2.4.0

  It looks editable, but it is not.

Anatomy

Email

Used to receive login notifications

1LabelTells users what to enter — never skip it

2InputHighlights its border on focus, turns red on error

3Help TextAdds format requirements or explains what went wrong

Variants

Default

The go-to shape for most single-line text input

Password

Passwords, keys, and anything that should be masked

With Icon

*🔍*

Search and friends — the icon hints at what to enter

Error

When validation fails — red border plus the reason why

Disabled

This field can't be edited right now

Typical use cases

Sign-in form

Create account

Sign Up

Already have an account? Log in

Search bar

**Guide**
HomeComponentsCourses
*🔍*
![](/assets/avatar-fox.png)

Profile settings

Profile

Avatar![](/assets/avatar-fox.png)Change

Nickname

Email

Save Changes

Project name

📄

📄

Rename File

CancelOK

Further reading

[<input> HTML input elementMDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)[Help users enter data in formsweb.dev ↗](https://web.dev/learn/forms/form-fields)
