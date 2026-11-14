# PoC summary: mandatory phone and minimum message length (example)

> FALLBACK EXAMPLE for Day 3 (current hypothesis, RULE/AC from Day 2). Both changes were really applied to the lf-client template and checked with `npx jest …` (Linux, Node 22). **Nothing was checked in the browser or in `npm run dev` mode**: this is stated below in "Not proven". Read it, repeat the probes yourself and add your own observations (see `fallback/en/README.md`). Code changes do not go into the PR, only this document.

## 1. Hypothesis

*"If we make the phone mandatory and reduce the minimum message length, the system will behave consistently on the client and on the server."* (RULE-03, RULE-04, AC-01, AC-02.)

## 2. Sandbox setup

Branch `poc/day-3` from `main` (or temporary changes reverted with `git restore .`). Documents were committed first, code was reverted afterwards, nothing reached `main`.

## 3. Changes made

1. **Probe 1 (phone):** on the server, in `app/lib/utils/validateContactData.ts` the phone check was made unconditional (instead of `if (phoneNumber)`); in `ContactForm.tsx` `.optional()` was removed from the phone schema.
2. **Probe 2 (message length):** `MESSAGE_MIN_LENGTH` in `app/constants/validation.ts` was changed from 10 to 5. The number `.min(10, …)` in `ContactForm.tsx` and the error text in `i18n/messages` were **not touched**: this makes the mismatch visible.

## 4. Evidence

- **Probe 1, tests:** `npx jest app/lib/utils/validateContactData.test.ts --coverage=false`. Before the change 14 of 14 green. After the change **1 red**: `should return no errors for valid input` (the test input contains no phone, so the server now returns an error). The other 13 are green.
- **Probe 1, conclusion:** the old test encodes the rule "phone is optional" (RULE-03). A red test is not a breakage but proof that the rule is changing and the test must be updated together with the requirement (AC-01).
- **Probe 2, tests:** `npx jest app/lib/utils --coverage=false`. After the change **1 red**: `should return error if message is too short` (its message "Too short" has 9 characters and is now valid), 194 tests green.
- **Probe 2, rule duplication (from code):** the message length is written in at least three places: the constant `MESSAGE_MIN_LENGTH`, the number `.min(10` in `ContactForm.tsx`, the error text in `i18n/messages` (`en` and `uk`). Changing only the constant leaves the form and the server with different rules.

## 5. Validation checklist

**Proven (test results I saw myself):**
- The old test `should return no errors for valid input` turns red when the phone becomes mandatory on the server.
- The old test `should return error if message is too short` turns red when the minimum becomes 5.

**Not proven:**
- What the form shows in the browser without a phone (is there an error and a "required" mark?): the browser was not opened.
- Whether the form in the browser accepts or rejects a 6-character message (from code it still requires 10).
- Whether `/api/collaboration`, which the "Contacts" page really calls, behaves the same.
- Whether `GetNotesModal` needs the same rule (Q-04).

**Developer needed:**
- Whether a mandatory phone breaks existing enquiries and integrations.
- Why the client and the server have different numbers instead of a shared constant.
- Which minimum length is right (a question for the stakeholder).

## 6. Recommended next step

Agree Q-04 (scope of the mandatory phone) with the stakeholder and a single source for the length rules; update the old tests together with the requirement (AC-01, AC-02), not after it.

## Extra: stretch S1 and S2 (from an earlier probe on Windows, `npm run dev` mode)

- **S1 (seed):** after removing the `OurMission` block of the `about-us` page in `scripts/seed-memory-mongo.js`, the pages `/en/about-us` and `/uk/about-us` answered 500 ("Something went wrong"), with a `ZodError` in the terminal, field `OurMission` required. The page did not degrade gracefully. Question for the developer: what happens in production.
- **S2 (label):** the text "Support the Foundation" appears in several keys of `i18n/messages/en.json`; the Ukrainian translation is separate in `uk.json`. The change was not applied.
