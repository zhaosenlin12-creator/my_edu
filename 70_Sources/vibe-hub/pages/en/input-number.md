---
type: web_source
source_url: "https://vibe-hub.org/en/input-number"
title: "InputNumber"
language: en
category: "input-number"
fetched_at: 2026-07-27T10:04:44+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←TextareaRadio→

# InputNumber

You might say

Only let people enter numbers for the quantity, with plus and minus controls if possible.

**Enter a number with a defined range and step**·A number input works for quantity, stock, price, and other numeric values. It can limit the format, minimum, maximum, and step size. Business rules such as available stock or a valid price still need to be checked again when the form is submitted.

Know first

[Input](/en/input)

*Number Input**Numeric Stepper*

−+
−+yuan

InputNumber**≠**[Steps](/en/steps)

Some design systems call both controls Stepper. [InputNumber](/en/input-number) increases or decreases a number; [Steps](/en/steps) shows the stages of a process.

### When to use it

- Product quantity

  Mechanical keyboard−2＋
- Stock level

  Stock−50＋
- Price or budget

  −1＋

  Minimum 1, maximum 99; anything outside is blocked
- A number with clear limits

  Pricing19.90yuan

  Always keep two decimal places

### When NOT to use it

- Collect a phone number or account number that is not used in calculations

  Mobile−138\*\*\*\*6688＋

  You can’t increment or decrement a phone number
- Hide the unit when it changes the meaning

  Budget≈ 450
- Rely on the browser control as the only validation

  2026-07-21 📅

  Dates have their own picker
- Use tiny step buttons as the only way to enter a large value

  −12,800＋

  For a wide numeric range, support direct entry

Anatomy

−＋

1InputNumberThe input and plus/minus buttons form one control, also called a numeric stepper.

2MinusClick to decrease the value by one step

3InputUsers can also type a value directly

4PlusDisable it after it reaches the upper limit.

Variants

Default

−＋

For simple numeric input, such as quantity or inventory

With Unit

−＋piece

Prices and quantities need a visible unit.

Small

−＋

In cards, rows, and other tight spaces

Disabled

−＋

This value is currently not allowed to be changed

Typical use cases

Shopping quantity

![](/assets/photo-cat.png)

Wireless mechanical keyboard · Brown switches

87 keys / Bluetooth dual mode

¥ 329.00

−+

Total 2 items, total **¥ 658.00**

Inventory editor

Inventory management · Wireless mechanical keyboard

Stock on hand−+*pieces*

Low-stock alert−+*items*

We’ll notify you on the dashboard when stock falls below this level

Budget setting

Hand-brewed coffee trial class

Limit 5 seats per person · Class starts on July 26th

Limited time

Number of copies to purchase
−+Register now

Team size

Product pricing

Price−+*yuan*

Member price−+*yuan*

Automatically retain two decimal places, the minimum is not less than 0.01 yuan

Further reading

[<input type="number">MDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/number)
