---
type: web_source
source_url: "https://vibe-hub.org/en/select"
title: "Select"
language: en
category: "select"
fetched_at: 2026-07-27T10:04:45+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←RateAutoComplete→

# Select

You might say

There are too many choices to show all at once. Put them in a dropdown people can open and pick from.

**Choose one value from a collapsed list**·Use a select when answers come from a fixed list but do not need to stay visible all the time. A few options are clearer as [Radio](/en/radio) buttons. If users may type their own answer, use an input or [AutoComplete](/en/auto-complete).

*Select Box*

All Status

All Status*✓*
In Progress*✓*
Completed*✓*
Expired*✓*

Select**≠**[Dropdown](/en/dropdown)

[Select](/en/select) chooses a form value. [Dropdown](/en/dropdown) opens actions or navigation, such as Rename, Export, or Delete.

Select**≠**[AutoComplete](/en/auto-complete)

[Select](/en/select) chooses only from a fixed list. [AutoComplete](/en/auto-complete) offers suggestions while someone types and may or may not permit a custom value.

### When to use it

- Country or region

  All states

  All statesIn progressCompletedExpired
- Role or status

  Choose a city

  BeijingShanghaiGuangzhouShenzhenHangzhou…
- A medium-sized fixed list

  All statesAll categoriesRecently updated
- A compact choice inside a form

  Choose a template

  AI Product Requirements Template (with review checklist)User Research Report Template

### When NOT to use it

- Hide two or three simple choices in a dropdown

  AllIn progressCompleted
- Use it when users need to compare long descriptions

  FrontendBackendDesign
- Allow a value outside the list without making that clear

  Province / City / DistrictGuangdong ProvinceShenzhenNanshan District
- Leave the selected value ambiguous after the menu closes

  Custom tag

  FrontendBackend➕ Create "Custom tag"

Anatomy

All statusIn progressAll status*✓*

1TriggerIts resting state — shows the currently selected value

2Selected LabelTells the user what's selected right now

3CaretSignals that the control can expand and its appearance changes when open

4DropdownThe overlay that holds all options — it can be searchable and grouped

5OptionHighlights on hover; the selected one gets a checkmark

Variants

Default

All Status

All Status*✓*
In Progress*✓*

The default shape when options are fixed and only one gets picked

Multiple

FrontendBackend

For picking several at once from a longer list

Searchable

🔍Shenzhen

ShenzhenShanghai

With dozens of options, typing finds the target fast

Clearable

In Progress*✕*

When the filter is optional — one click back to nothing selected

Disabled

All Status

Temporarily locked until conditions are met, preventing misclicks

Typical use cases

Country picker

**Task List**
In Progress

Homepage RedesignIn Progress

Payment Flow ReviewIn Progress

Tracking Plan ReviewNot Started

Role setting

City

Guangdong · Shenzhen

Guangdong · Shenzhen*✓*
Guangdong · Guangzhou
Zhejiang · Hangzhou

Status filter

**Interface Language**The language shown across the interfaceEnglish

**Time Zone**Affects how events and reminders show timeUTC+8 Beijing

Form option

**Traffic Trend**
Weekly

W26W27W28W29W30W31

Further reading

[<select>: The HTML Select elementMDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)[Listbox PatternWAI-ARIA APG ↗](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/)
