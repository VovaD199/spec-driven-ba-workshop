# PoC notes: what I saw in the running app (example)

> FALLBACK EXAMPLE for Day 3. Test results were taken on the template (Linux, Node 22); the browser items were **not checked**, and that is stated. Your notes must be yours: repeat the probes and write what you see (see `fallback/en/README.md`).

## Probe 1: mandatory phone
What I changed: on the server the phone check became unconditional (`validateContactData.ts`); in `ContactForm.tsx` I removed `.optional()`.
What I saw in the browser: did not check.
What the tests showed: `npx jest app/lib/utils/validateContactData.test.ts --coverage=false`: 13 green, 1 red (`should return no errors for valid input`: the test input has no phone). This is a finding: the old test encodes "phone is optional".

## Probe 2: minimum message length
What I changed: `MESSAGE_MIN_LENGTH` from 10 to 5 in `app/constants/validation.ts`; I did not touch `.min(10` in `ContactForm.tsx` or the texts in `i18n/messages`.
What I saw in the browser: did not check; from code the form will still require 10, i.e. a mismatch with the server appeared.
What the tests showed: `npx jest app/lib/utils --coverage=false`: 1 red (`should return error if message is too short`: "Too short" has 9 characters and is now valid), 194 green.

## My questions for developers (no Q-NN number; the analyst moves them into the feature document after agreement)
- Should the form and the server take the minimum length from one place? | tech lead
- Who updates the old tests together with a rule change? | tech lead
