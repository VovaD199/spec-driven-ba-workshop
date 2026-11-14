# Issue texts (fallback example, Day 2)

> FALLBACK EXAMPLE. If GitHub MCP or the chat is unavailable, these texts can be **read, corrected and pasted by hand** on github.com. Based on `contact-form-feature.md` in this folder. Add your own corrections (see `fallback/en/README.md`). **Do not overwrite the original issue text**: add everything else as separate comments.

## 1. Creating the issue

**Title:** `Contact form — update validation and notifications`

**Body:**

```text
We want to tighten up the contact form. Phone number should be mandatory.
We should also let visitors attach a document (CV or portfolio) when they write to us.
Notifications need to reflect the new field.
```

## 2. Comment "Business context"

```text
Business context (simulation, to be confirmed with the real stakeholder):
- Goal: call back about performance rights; emails get lost.
- Success metric: share of requests answered within 2 working days, now ~50%, target 90%.
- NFR-01 privacy: phone and CV are personal data; keep up to 6 months; access for two employees.
- NFR-02 files: PDF only, up to 5 MB.
- NFR-03 languages: error messages in the visitor's interface language.
```

## 3. Comment "Rules table:"

Paste the table from section 5 of `contact-form-feature.md` (RULE-01…RULE-11, three states). Short version:

| ID | Rule | File | Source of truth | Layer | Is now → Should be |
|---|---|---|---|---|---|
| RULE-01 | Name | `validation.ts`, `validateContactData.ts`; `ContactForm.tsx` | constant / number in the schema | API and UI | 2–50 → unchanged |
| RULE-02 | Email | `validateContactData.ts` (regular expression); `ContactForm.tsx` (`.email()`) | **two different rules** | API and UI | different → ? (Q-09) |
| RULE-03 | Phone | `validateContactData.ts`; `ContactForm.tsx` | regular expression / schema | API and UI | optional → mandatory |
| RULE-04 | Message | `validation.ts`; `ContactForm.tsx`; `i18n/messages` | constant and number in the schema and texts | API and UI | 10–1000 → unchanged |
| RULE-05 | Consent to the policy | `ContactForm.tsx` | zod schema | **UI only** | UI only → ? (Q-08) |
| RULE-08 | Accepting the request | `app/api/collaboration/route.ts` | hard-coded text | API | demo "success" → ? |

## 4. Comment with the impact analysis

| Affected area | Change type | Risk | Recommended action | Regression test idea | Related RULE-IDs |
|---|---|---|---|---|---|
| Form (`ContactForm.tsx`) | changed | medium | Make phone mandatory, add a file field | An empty phone is not sent | RULE-03, RULE-06 |
| API validation (`validateContactData.ts`) | changed | high | Remove the optional-phone branch, align with the form | A request without phone gets 400 | RULE-03 |
| Routes (`collaboration`, `contact`) | changed | medium | Accept a file, choose which route stays | An oversized file is rejected | RULE-06, RULE-08 |
| Mail service (`emailService.ts`) | new work | high | Not called today: connect it and add the attachment | The email contains the phone and a link | RULE-07 |
| Upload service (`upload.ts`) | changed | high | A demo stub today; decide on storage | An uploaded PDF opens | RULE-06 |
| Tests (`ContactForm.test.tsx`, `validateContactData.test.ts`) | changed | medium | Update the expectations | All tests pass | RULE-03 |
| Translations (`i18n/messages`) | changed | low | Error texts for phone and file (uk and en) | The right language is shown | RULE-03, RULE-06 |
| Configuration | new | medium | File size and type limits in constants | Limits come from one constant | RULE-06 |

## 5. Comment "Acceptance criteria:"

Use section 6 of `contact-form-feature.md` (AC-01…AC-12, Given/When/Then, RULE-ID). This is a **separate comment**, not a replacement of the issue body.

## 6. Comment "Open questions for the stakeholder:"

Use section 8 of `contact-form-feature.md` (Q-01…Q-10 with owners and dates).
