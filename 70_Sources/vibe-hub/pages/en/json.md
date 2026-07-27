---
type: web_source
source_url: "https://vibe-hub.org/en/json"
title: "JSON"
language: en
category: "json"
fetched_at: 2026-07-27T10:05:21+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←APICORS→

# JSON

You might say

AI keeps returning data with curly braces inside curly braces. How do I read and write it?

**Represent structured data as text that programs can exchange**·JSON stores objects, arrays, strings, numbers, booleans, and null in a widely supported text format. APIs often use it for request and response bodies. The text must follow strict syntax, and the receiving side still needs to validate the expected fields and types.

Know first

[HTTP](/en/http)

*JavaScript Object Notation*

```
{
  "name": "Button",
  "price": 0,
  "free": true,
  "tags": ["General", "Form"]
}
```

### When to use it

- API request and response

  { "data": { "list": [ … ] } }Confirm the overall structure first, then read fields by level.
- Configuration file

  [{…}"text"42]

  An ordered list of JSON values; whether they share a shape depends on the API contract.
- Store structured data temporarily

  data→user→name

  Nested fields must be read by level.
- Exchange nested values between systems

  {"a":1,"b":[2,3]}→Format

### When NOT to use it

- Add comments or trailing commas where strict JSON is required

  { name: "Xiaolin" }The key lacks double quotes, so it cannot be parsed as JSON.
- Assume parsed JSON has the correct fields

  [ "a", "b", ]JSON does not allow a trailing comma after the last item.
- Use JSON for a large binary file

  { 'name': 'Xiaolin' }JSON keys and strings must use double quotes.
- Expose secret data just because the format is readable

  { // comment "a": 1 }JSON does not support comments.

Anatomy

```
{
  "tags": ["Universal", "form"]
}
```

1ObjectA pair of curly brackets enclosing the whole, describing "a thing"

2KeyThe name to the left of the colon must be in double quotes

3ArrayAn ordered list enclosed in square brackets, which is used to render [List](/en/list)

4ValueThe content on the right side of the colon: string, number, Boolean, object, array

Variants

Object

{ "name": "button", "price": 0 }

Curly braces enclose key-value pairs to describe something

Array

[ "General", "Form", "Feedback" ]

Square brackets enclose the list, the order is meaningful

Nested

{ "user": { "roles": […] } }

Objects are arrays, and real data is like this

Typical use cases

API response

HeadersPreviewResponse

▾ **data**: {…}  
▾ **list**: [3]  
▾ **0**: {name: "Button", price: 0}  
▾ **1**: {name: "Text input", price: 0}  
▸ **2**: {…}  
**total**: 42

Preview helps you arrange JSON into a collapsible tree

Configuration

data.json

{

"site": "Vibe Picture Book",

"stats": {

"components": 48,

"online": true

},

"tags": ["General", "Form"]

}

Webhook payload

1 {

2 "name": "Button",

3 "tags": ["Universal",],

4 }

✕ Line 3: There is an extra comma after the last item in the array

Exported data

$ curl -s https://api.vibeui.dev/user/1 | jq

{

"id": 1,

"name": "Alex Chen",

"roles": [

"admin",

"editor"

]

}

# jq Format compressed JSON into an indented structure

Further reading

[Working with JSONMDN ↗](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/JSON)
