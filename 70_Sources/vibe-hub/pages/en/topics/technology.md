---
type: web_source
source_url: "https://vibe-hub.org/en/topics/technology"
title: "Tech Stack Terms for Vibe Coding"
language: en
category: "topics"
fetched_at: 2026-07-27T10:04:39+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Developer Tools5 entries

### Terminal

AI gave me a command to run, but I don't know what it will do. Is it safe to run?

### npm

AI told me to install dependencies, and one command downloaded a ton of stuff. What's going on?

### Build

Build this commit into a deployable front-end artifact and retain a version identifier; do not treat “build succeeded” as being live.

### CI

For every PR or merge, automatically run lint, build, and key tests, with results shown on the pull request.

### Lint

Use lint to flag unused variables and unhandled promises first, but do not say a passing lint means the button really works.

Testing11 entries

### Acceptance Criteria

Write clear acceptance criteria for the itinerary feature: saving shows the trip, refresh keeps it, and invalid dates explain how to fix them.

### Test Case

Write a failed-login test case so another person can use the same account and steps and see the same result.

### Unit Test

Add unit tests for price calculation: 100 gets 20 off, 99 does not, and external payment must not participate.

### Integration Test

Test that submitting a registration form sends correct fields, the API saves them, and the page shows server errors.

### End-to-End Test

Like a real user, create an itinerary from the travel home page, save it, reopen it, and confirm the confirmation page shows that same trip.

### Smoke Test

After a new version reaches testing, first check that home opens, login works, and the core API responds; if one fails, do not start full regression.

### Regression Test

After changing tax rules, rerun payment, coupons, and order confirmation as well as the new rule to ensure working checkout was not broken.

### Test Coverage

Do not only report “90% coverage”; also show whether the high-risk path combining payment failure and a coupon was actually tested.

### Test Double

When testing an order failure message, use a controllable payment test double that returns “payment rejected” instead of depending on the real payment service every time.

### Test Data and Fixture

Prepare fixed user and product data for the order test, and create it before every run and clean it after so the next run starts identically.

### Flaky Test

Run the same commit five times: it sometimes passes and sometimes times out. Check waiting conditions and shared accounts first; do not hide red with endless retries.

Tech Stack1 entries

### Tech Stack

When someone asks what tech stack I use, what am I supposed to say?

Programming Languages3 entries

### JavaScript

What language makes the interactive parts of a webpage move and respond?

### TypeScript

I've heard there's a stricter version of JavaScript that catches mistakes early. What is it?

### Python

What's the language everyone recommends for automating spreadsheets and files with a script?

Frontend Frameworks3 entries

### React

People keep saying to use React for websites. What's better about it than writing the page directly?

### Vue

Is Vue really friendlier for beginners, and how is it different from React?

### Next.js

Is there a framework for building a full React site with routing and SEO?

CSS & Components2 entries

### Tailwind CSS

Do I really have to open a separate CSS file for every style change? Can I adjust styles right where I write the markup?

### shadcn/ui

Is there a set of good-looking components I can copy into my project and customize?
