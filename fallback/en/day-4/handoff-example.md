# Handoff pack: contact form (example)

> FALLBACK EXAMPLE for Day 4. Compiled from the specification and the analysis of Days 2–4 (`spec-contact-form.md`, `../day-2/contact-form-feature.md`). **The mockup sections are illustrative** (I did not generate a real Figma mockup): replace them with your own findings. Read it, verify against the code and add your own corrections (see `fallback/en/README.md`).

## 1. Short description of the feature
Site visitors write to the Foundation through a form, but the phone is optional and no document can be attached. The change makes the phone mandatory, optionally allows attaching a PDF up to 5 MB, and must show the new data in the notification email.

## 2. Affected areas
- Browser form: `app/shared/components/forms/contact-form/ContactForm.tsx` (phone rules, file field).
- Sending from the form: `app/shared/components/forms/offer-collaboration-form/OfferCollaborationForm.tsx` (the request is JSON today).
- Server: `app/lib/utils/validateContactData.ts`, `app/constants/validation.ts`, `app/api/collaboration/route.ts` (and the unused `app/api/contact/route.ts`).
- Notifications and files: `app/services/email/emailService.ts` (not connected), `app/services/upload/upload.ts` (stub).
- Texts: `i18n/messages/en.json`, `uk.json`.
- Form and validation tests.

## 3. Dependencies
- Storage for files (missing), mail connection (missing).
- A new file selection field in the UI (no analogue in `app/shared/components/`).
- Decisions about attachment storage (`Q-01`) and privacy (`Q-02`).

## 4. Clarifying questions
Blockers (owner and date are in `spec-contact-form.md`): Q-01 where the attachment is stored; Q-02 privacy (6 months, access for two); Q-03 who receives the notification; Q-04 whether the phone is mandatory in all forms; Q-07 virus scanning of files; Q-08 consent to the policy on the server. The rest (Q-05, Q-06, Q-09…Q-16) do not block the start.

## 5. Risks
- **Blocker:** there is no storage for files and no mail: attachments are impossible without them.
- **Important:** mismatch of client and server rules (email, lengths) can lead to different behaviour.
- **Important:** privacy policy for CVs (personal data).
- **Minor:** phone error labels need uk/en alignment.

## 6. Missing states (from the mockup analysis; replace with your own)
Removing the chosen file; upload interrupted halfway; re-sending after an error; narrow screen.

## 7. Proposed acceptance criteria (for QA)
AC-01 empty phone: error, request not sent. AC-04 PDF up to 5 MB is attached. AC-05 and AC-06 file over 5 MB or non-PDF: error. AC-08 without consent to the policy the form is not submitted. AC-10 the notification contains the phone and a link to the file (full list AC-01…AC-12 in `spec-contact-form.md`).

## 8. Evidence summary
**Proven:** the rules are written from the code (checked on the template); the form on "Contacts" posts to `/api/collaboration`; no notification is built today. **Not proven:** the mockup behaviour in the browser after implementation; the choice of storage; legal requirements for CVs.

## 9. Traceability matrix
Full matrix: `spec-contact-form.md`, section 9 (Request → Rule → AC → Design → Test idea → Status). Orphans: RULE-02 without an AC (waiting for Q-09).

## Definition of Ready
| Section | Ready? | What is missing |
|---|---|---|
| 1. Description | ready | |
| 2–3. Areas and dependencies | ready | |
| 4. Questions | ready | all have owners and dates (in the specification) |
| 5. Risks | ready | |
| 6. Missing states | not ready | illustrative: replace with states from your own mockup |
| 7. Acceptance criteria | ready | AC-01…AC-12 have RULEs; the AC are verifiable |
| 8. Evidence | ready | honestly split into "proven / not proven" |
| 9. Matrix | ready | the RULE-02 orphan is explained |

Commit for which the pack was DoR: `<paste git rev-parse --short HEAD>`.
