# Specification: contact form (example, 8 artefacts + NFR + matrix)

> FALLBACK EXAMPLE for Day 4. This is a **consolidation** of Days 2–3 (`../day-2/contact-form-feature.md`, `../day-3/figma-analysis-example.md`): **IDs are kept unchanged** (RULE-01…RULE-11, AC-01…AC-12, Q-01…Q-16); scope, NFR and a traceability matrix are added. Confidence levels: **Grounded** (in the code, the request or the stakeholder answer from the simulation), **Inferred** (a logical conclusion), **Invented** (made up: not used here, the unknown goes to open questions). Read it, verify against the code and add your own corrections (see `fallback/en/README.md`). The structure follows `templates/en/ba-refinement-template.md`. Figma frame names in the matrix are illustrative: replace them with yours.

| Field | Value |
|---|---|
| Feature ID | FEAT-CONTACT-001 |
| Name | Contact form: mandatory phone and attachment |
| Status | Refinement |
| Source | issue "Contact form — update validation and notifications" (original kept) |

## 1. Problem

**Who is affected:** site visitors writing to the Foundation and employees who process enquiries. **Pain:** emails get lost and a reply is needed within 2 working days; the phone is optional and documents (CV, portfolio) cannot be sent. **Metric:** share of enquiries answered within 2 days: now ≈50 %, target 90 % (stakeholder answer in the simulation). **Desired outcome:** the Foundation receives an enquiry with a phone and, optionally, a document.

## 2. Scope

| ID | In scope | Note |
|---|---|---|
| IN-01 | Mandatory phone in the contact form | Grounded (issue) |
| IN-02 | Optional PDF attachment up to 5 MB | Grounded (issue, stakeholder answer) |
| IN-03 | Showing the phone and the attachment in the notification | Grounded (issue) |

| ID | Out of scope | Reason |
|---|---|---|
| OUT-01 | Other file types | Stakeholder: PDF only |
| OUT-02 | Anti-spam and request rate limiting | Separate topic, question Q-06 |
| OUT-03 | Changing other forms (`GetNotesModal`) | Not in the request, question Q-04 |

## 3. Actors and flow

Actors: visitor, Foundation employee. Main flow: the visitor fills in the form → the form checks the fields → request to `/api/collaboration` → the server checks → "success" → confirmation window → the employee receives a notification (no notification is built today, RULE-07).

## 4. Business rules

IDs and numbering are **the same as in Day 2** (full three states: `../day-2/contact-form-feature.md`, section 5).

| ID | Rule (should be) | Source |
|---|---|---|
| RULE-01 | Name 2–50 characters | Code, unchanged |
| RULE-02 | Email: the client and server rule must be one (decision open) | Code (mismatch), Q-09 |
| RULE-03 | Phone mandatory; format `+` and digits, 11–16 characters | Issue, code |
| RULE-04 | Message 10–1000 characters | Code, unchanged |
| RULE-05 | Consent to the policy mandatory (whether to check on the server: decision open) | Code (UI only), Q-08 |
| RULE-06 | Attachment optional, PDF only up to 5 MB | Issue, stakeholder answer |
| RULE-07 | The notification contains the phone and a link to the attachment | Issue, Q-03 |
| RULE-08 | Accepting the request (demo "success" today) | Code, decision open |
| RULE-09 | State of the "Send" button | Code, Q-05 |
| RULE-10 | Request rate limiting | Not found in the code, Q-06 |
| RULE-11 | The maximum length message disappears automatically | Code, unchanged |

## 5. Constraints and dependencies

| ID | Type | Description |
|---|---|---|
| DEP-01 | Technical | No storage for files (`upload.ts` is a stub), Q-01 |
| DEP-02 | Technical | Mail service not connected (`emailService` is not called), Q-03 |

## 6. Assumptions

| ID | Assumption | How to verify |
|---|---|---|
| ASM-01 | The mandatory phone applies only to the form on "Contacts" | Q-04 |
| ASM-02 | The notification is sent to the Foundation's mailbox | Q-03 |
| ASM-03 | "Interface language" (NFR-03) means the page language, not the browser language | Q-16 |

## 7. Open questions

IDs **kept from Day 2** (Q-01…Q-10) and Day 3 (Q-11…Q-16). Owner and date are in the full Day 2/3 tables. Blockers for the start of development:

| ID | Question | Blocks | Owner |
|---|---|---|---|
| Q-01 | Where is the attachment stored? | RULE-06, DEP-01 | tech lead |
| Q-02 | How do we implement privacy (6 months, access for two)? | NFR-01, AC-12 | personal data officer |
| Q-03 | Who receives the notification and through which channel? | RULE-07, AC-10 | head of the enquiries team |
| Q-04 | Does the mandatory phone apply to all forms? | RULE-03, OUT-03 | product owner |
| Q-07 | Should files be scanned for viruses? | NFR-04 | security / tech lead |
| Q-08 | Should consent to the policy be checked on the server? | RULE-05, AC-08 | legal / product owner |

The rest (Q-05, Q-06, Q-09, Q-10, Q-11…Q-16) do not block the start and stay for refinement.

## 8. Acceptance signals

AC-01…AC-12 from Day 2 unchanged (Given/When/Then wording: `../day-2/contact-form-feature.md`, section 6). Here only the way to verify.

| ID | Signal | How we verify | Rules |
|---|---|---|---|
| AC-01 | Empty phone: error, request not sent | Demo, test | RULE-03 |
| AC-02 | Wrong phone format: error | Demo, test | RULE-03 |
| AC-03 | Correct phone: request is sent | Demo | RULE-03 |
| AC-04 | PDF ≤ 5 MB is attached | Demo | RULE-06 |
| AC-05 | File over 5 MB: error, not added | Demo | RULE-06 |
| AC-06 | Non-PDF: error | Demo | RULE-06 |
| AC-07 | Without a file the request is sent | Demo | RULE-06 |
| AC-08 | Without consent the form is not submitted | Demo | RULE-05 |
| AC-09 | The button is disabled while sending | Demo | RULE-09 |
| AC-10 | The notification contains the phone and a link | Demo | RULE-07 |
| AC-11 | Errors in the interface language | Demo | RULE-03, RULE-06, NFR-03 |
| AC-12 | Attachments older than 6 months are deleted | Test on a test storage | RULE-06, NFR-01 |

## 9. Traceability

Full matrix per `templates/en/traceability-matrix-template.md`: from request to test idea. Statuses: Draft, Agreed (date and who), Open (depends on Q).

| Request (Source) | Requirement / rule | AC | Design (Figma frame) | Test idea | Status |
|---|---|---|---|---|---|
| issue, sentence 1 "Phone number should be mandatory" | RULE-03 | AC-01, AC-02, AC-03 | "Form: empty", "Form: phone error" | `validateContactData`: a request without a phone returns an error; the form is not sent | Agreed (simulation); Open Q-04 for other forms |
| issue, sentence 2 "attach a document (CV or portfolio)" | RULE-06 | AC-04, AC-05, AC-06, AC-07 | "Form: file selected", "File: too large", "File: wrong type" | A file of 5 MB + 1 byte is rejected; `.docx` is rejected | Agreed (simulation); Open Q-01, Q-07, Q-10 |
| issue, sentence 3 "Notifications need to reflect the new field" | RULE-07 | AC-10 | (no frame: email) | The notification email contains the phone and a link | Open Q-03 |
| stakeholder answer: privacy 6 months | NFR-01 | AC-12 | (no frame) | Cleanup deletes a file aged 6 months + 1 day | Open Q-02 |
| stakeholder answer: error language | NFR-03 | AC-11 | "Form: errors" (uk, en) | The phone error is shown in uk and en | Agreed (simulation); Open Q-16 |
| code: consent to the policy only in the UI | RULE-05 | AC-08 | "Form: consent unchecked" | A direct API request without consent | Open Q-08 |
| code: two email rules | RULE-02 | (no AC written: a gap) | | | Open Q-09 |
| code: the button is disabled only while sending | RULE-09 | AC-09 | "Form: submitting" | A double click does not make two requests | Open Q-05 |

**Orphans:** RULE-02 without an AC (waiting for Q-09); RULE-01, RULE-04, RULE-08, RULE-10, RULE-11 are not touched by the request and are not needed in the matrix. This is a conscious decision, not an omission.

## NFR

| ID | Category | Requirement | Source |
|---|---|---|---|
| NFR-01 | Privacy | Phone and CV are personal data: keep no longer than 6 months, access for two employees only | stakeholder answer; Q-02 |
| NFR-02 | Files | PDF only, up to 5 MB | stakeholder answer |
| NFR-03 | Localisation | Errors in the visitor's interface language (uk, en) | stakeholder answer |
| NFR-04 | Security | The file is checked for type and malicious content before storing | Inferred; Q-07 (the stakeholder "did not think about it") |
| NFR-05 | Accessibility | The file field and errors are accessible from the keyboard and by a screen reader | Inferred; Q-14 |

## Refinement checklist

- [x] IDs kept from Day 2 (compared with `contact-form-feature.md`)
- [x] Every AC has a RULE; orphans in the matrix are explained
- [x] NFR ≥ 4, privacy included
- [x] Questions have owners (full tables of Days 2 and 3)
