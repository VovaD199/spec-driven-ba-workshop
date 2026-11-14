# Mockup analysis of the contact form: observations and questions (example)

> FALLBACK EXAMPLE for Day 3 (extra task). Compiled **from the requirement** (mandatory phone, PDF attachment up to 5 MB), not from a real Figma mockup: I did not generate a mockup. Use it as a structure sample; write your own observations about your mockup separately. See `fallback/en/README.md`.

## What a typical mockup shows (check against your own)

Empty form, form with data, phone error, oversized file, non-PDF, uploading, success, send error; both languages.

## The analyst's own observations (before AI)

1. Is there a "file removed" state if the user changes their mind?
2. Is a message character counter shown (the code has `maxLength` and an auto-hiding limit message)?
3. Do field and error labels match the texts in the site's `i18n/messages`?

## Hidden assumptions

- The mockup assumes the phone is always in international format with `+`; the code accepts only `+` and digits, 11–16 characters.
- The mockup assumes the attachment goes into a storage that the template does not have (`upload.ts` is a demo stub).
- The mockup assumes a notification email, while in the template `emailService` is never called.

## Missing states

- Upload interrupted halfway.
- Re-sending after an error.
- Narrow screen.
- Network unavailable.

## Questions by category

Numbering continues Day 2 (it has Q-01…Q-10, so here we start at Q-11); questions already in Day 2 (storage, notification channel, phone scope, button) are not duplicated.

- Q-11 | [Business rules] Is there a limit on the number of files per enquiry? | product owner
- Q-12 | [UI behaviour] Can the chosen file be removed, and is the entered data kept after an error? | UX designer
- Q-13 | [Edge cases] What to do with a corrupted PDF and a double click on "Send"? | tech lead
- Q-14 | [Accessibility] Does a screen reader announce errors of the file field, and can the file be chosen from the keyboard? | UX designer
- Q-15 | [Privacy] Is separate consent for processing the CV needed (beyond the general policy)? | legal / personal data officer
- Q-16 | [Localisation] In which language are errors if the site and browser languages differ? | UX designer (NFR-03 says "interface language": clarify which language that is)
