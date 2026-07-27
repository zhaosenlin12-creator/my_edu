---
type: web_source
source_url: "https://vibe-hub.org/en/data-validation"
title: "Validation"
language: en
category: "data-validation"
fetched_at: 2026-07-27T10:05:41+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←CORSAPI→

# Validation

You might say

People can submit complete nonsense. How do I stop bad input before it gets saved?

**Check that incoming data has the expected shape and allowed values**·A required field can be checked when someone leaves it, while cross-field rules usually need a submit-time check. Frontend feedback helps people correct mistakes, but the backend must validate again and return specific field errors.

Know first

[Route & Endpoint](/en/route)[JSON](/en/json)

Email**oil@example.com***✓*
Age**0***✕ Must be 1–120*
role**user***✓*

Backend rules**Do not write if it does not pass**

### When to use it

- Check API request bodies

  See field rules at a glance

  email**Required · email format**price**Number · greater than 0**role**user / admin**
- Validate form submissions on the server

  Errors should point to the specific field.

  Product price**-3**Below the input**Price must be greater than 0**
- Reject impossible or malformed values

  Write to the database only after validation passes

  Receive input→Rule check→Write to database
- Return field-level errors the interface can explain

  Keep rules together in one schema

  email: string().email()price: number().positive()role: enum(["user", "admin"])

### When NOT to use it

- Trust data only because TypeScript compiled

  Page-side checks can be bypassed

  Skip form→Request API directly→Backend still needs validation
- Validate only in the browser

  Status code and result contradict each other

  HTTP**200 OK**Response body**error: invalid email**

  The frontend can easily mistake failure for success.
- Return one vague error for every field

  Do not show internal errors to users.

  **PrismaClientKnownRequestError**at node\_modules/runtime/library.js:129:42

  The page should say: Unable to save right now. Please try again later.
- Use validation as a substitute for authentication or authorization

  Do not silently change critical data.

  User input**Price -99**
  *→*
  System silently changes it to**Price 99**

  Reject it clearly and ask the user to confirm.

Anatomy

Original input*→*Validation rules*→*PassorField error

1Raw InputForms, URLs, headers, and third parties are all untrusted input.

2SchemaDefine types, required fields, ranges, lengths, and allowed values.

3ResultPassing proves schema conformance; authorization, business rules, and output context still need checks.

Typical use cases

Registration

Registration Verification**Describe how to modify next to the field**

Email**oil@**Password**••••**Create account

Incomplete email format · Password must be at least 8 characters

Order creation

Product price**Reject unreasonable values**

Price**-19.90**

Verification result**The price must be greater than 0**

Profile update

Article title**Show length limit when typing**

Title**This is an article title that is longer than allowed...**

Currently**56 words**Maximum**40 words**

Webhook input

Request body Schema**Validate API fields in one place**

email**✓ string**age**✕ Should be 1–120**role**✓ user**

Failure will return 400 or 422 and field-level errors according to API convention

Further reading

[Client-side form validationMDN ↗](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)[Help users enter the right data in formsweb.dev ↗](https://web.dev/learn/forms/validation)
