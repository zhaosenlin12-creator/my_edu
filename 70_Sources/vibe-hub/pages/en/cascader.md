---
type: web_source
source_url: "https://vibe-hub.org/en/cascader"
title: "Cascader"
language: en
category: "cascader"
fetched_at: 2026-07-27T10:04:47+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←AutoCompleteTreeSelect→

# Cascader

You might say

For the address, let people choose state, then city, then neighborhood one level at a time.

**Choose a path one level at a time**·A cascader works for data such as country, state, and city or a nested product category. Keep the current path visible and explain whether a parent level can be selected. If users need items from several branches at once, a tree selector is usually clearer.

Know first

[Select](/en/select)

Guangdong Province / Shenzhen City / Nanshan District

Guangdong Province*▸*Guangxi*▸*

Guangzhou*▸*Shenzhen*▸*

Futian DistrictNanshan District

### When to use it

- Region selection

  Province / City / DistrictGuangdong ProvinceShenzhenNanshan District
- Product category

  Engineering / FrontendEngineering ▸Platform Engineering ▸Frontend
- Organization path

  Electronics ▸Phones & Communications ▸Smartphones
- Any choice that follows one hierarchy path

  AddressGuangdong / Shenzhen / Nanshan

  Show the full path so the selection is unmistakable

### When NOT to use it

- Use it for data with no real parent-child relationship

  In progress ▸In progressThe data has one level, so it doesn’t need a second menu
- Hide the chosen path after the panel closes

  Engineering ×2

  ☑ Engineering☑ Frontend☐ Backend☐ Design
- Use several steps when each level has only a few options

  PublicMembers onlyPrivate
- Make parent selection rules unclear

  Nanshan

  Guangdong / Shenzhen / **Nanshan**DistrictGuangdong / Guangzhou / **Nanshan**Subdistrict

Anatomy

Nanshan DistrictShenzhen*▸*Guangzhou City*▸*

1TriggerShows the selected path, such as "Guangdong/Shenzhen/Nanshan"

2ColumnOne level per column; selecting an item opens the next column

3OptionAn option for the current level

4ArrowIndicates that this item has child levels; click to expand them to the right

Variants

Region

Guangdong Province*▸*

Shenzhen City*▸*

Nanshan District

Addresses and other data with a clear parent-child hierarchy

Path Echo

Guangdong Province / Shenzhen City / Nanshan District

When users need to see every selected level.

Leaf Only

Nanshan District

When the hierarchy only helps with selection and the form should submit just the final-level value.

Searchable

🔍Nanshan

Guangdong Province / Shenzhen City / **Nanshan** DistrictGuangxi / Guilin City / **Nanshan** Street

When there are many options and users need to search for a path directly

Typical use cases

Shipping region

Region
Guangdong Province / Shenzhen City / Nanshan District

Guangdong Province*▸*Guangxi*▸*

Guangzhou*▸*Shenzhen*▸*

Futian DistrictNanshan District

Product category

**Product management**
Digital electrical appliances / mobile communications

📱

Smartphone Pro

¥ 3,999

🎧

Noise-canceling headphones

¥ 899

⌚

Sports watch

¥ 1,299

Department path

![](/assets/avatar-fox.png)Alex Chen
Technical Center / Front-end Group

Technical Center*▸*Marketing Department*▸*

Platform R&D*▸*Big Data*▸*

Front-end groupBack-end group

Content taxonomy

Enterprise certification

Company name

Industry
Information Technology / Internet

Submit certification
