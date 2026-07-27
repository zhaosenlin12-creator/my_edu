---
type: web_source
source_url: "https://vibe-hub.org/en/auto-complete"
title: "AutoComplete"
language: en
category: "auto-complete"
fetched_at: 2026-07-27T10:04:46+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←SelectCascader→

# AutoComplete

You might say

When someone types the first few letters, show suggestions and let them click one to finish the entry.

**Show matching suggestions while the user types**·Autocomplete works for addresses, contacts, and tags that have common answers but may still allow free text. The user can choose a suggestion or keep typing. If only listed values are valid, use a searchable [Select](/en/select) instead.

Know first

[Input](/en/input)[Select](/en/select)

**Vibe** Coding beginner guide
**Vibe**Hub component guide
**Vibe** design guidelines

AutoComplete**≠**[Select](/en/select)

[AutoComplete](/en/auto-complete) offers matches based on what someone types. [Select](/en/select) needs no typing and chooses only from a fixed list.

AutoComplete**≠**Combobox

A combobox is the complete control of an input plus a popup option list. Autocomplete emphasizes the behavior of showing matches as someone types; component libraries often use the terms differently.

### When to use it

- Address entry

  vibe

  **vibe** coding basics**vibe**-ui-guide**vibe** design guidelines
- Contact lookup

  oil-oil@

  oil-oil@**gmail.com**oil-oil@**qq.com**oil-oil@**163.com**
- Tag suggestions

  *🔍 Search components…*

  Recent searchesDate pickerForm validation
- Search with likely matches

  ⌘ New

  ➕ New project📄 New document📁 New folder

### When NOT to use it

- Force a suggestion when free text should remain valid

  All states

  All statesIn progressCompletedExpired
- Show unrelated results before enough text is entered

  Province / City / DistrictGuangdong ProvinceShenzhenNanshan District
- Change the typed value without clear confirmation

  AllIn progressCompleted
- Use it for a tiny fixed list

  CityShenzhenx

  Invalid values can still be submitted, affecting later reporting

Anatomy

**vibe** coding getting started guidevibe-ui-guide component illustration

1InputThe same type of field users type into for ordinary input

2Suggestion PanelUpdates suggestions as the user types

3SuggestionOne suggestion; users can move through suggestions with the keyboard

4Matched TextHighlights matching keywords to show why the suggestion appears.

Variants

Search Suggest

**vibe** Getting started with coding**vibe**-ui-guide

Type candidate words in the search box

Email Suffix

alex.chen@**gmail.com**alex.chen@**qq.com**

Semi-fixed format input such as email and URL

History

🕘 date picker🕘 form validation

Allow users to reselect recently searched content with one click

Grouped

Component**Button**Documentation**Button** design guidelines

When candidates are from different types, group them by type for easier identification

Typical use cases

Address form

**VibeHub**
🔔

**Button** · Component
**Button** guidelines · Documentation
Radio **button** · Component

Mention a teammate

Log in to your account

maya-lee@**gmail.com**
maya-lee@**qq.com**

Tag editor

Shipping address

Building R2-B, South Area, Science and Technology Park, **Nanshan** District, Shenzhen
Zone C, Shekou Sea World, **Nanshan** District, Shenzhen
No. 12, **Nanshan** Street, Guangzhou

Search box

⌘ New

➕ New project
📄 New document

Further reading

[Combobox PatternWAI-ARIA APG ↗](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)
