# PoC slice: mandatory phone in the contact form (example)

> FALLBACK EXAMPLE for Day 4 (independent part). Built from the specification `spec-contact-form.md`. Structure per `templates/en/mvp-poc-slice-template.md`. Read it and adapt it (see `fallback/en/README.md`).

| Field | Value |
|---|---|
| Slice ID | POC-CONTACT-001 |
| Parent feature | FEAT-CONTACT-001 |
| Type | PoC |
| Target window | 2 weeks |

## 1. Hypothesis

**We believe that** a mandatory phone in the contact form **for** visitors **will increase the share of enquiries the Foundation can answer by phone** without **significantly** reducing the number of enquiries. **We will know we are right when** the share of enquiries with a phone becomes 100% (by definition) and the number of enquiries per week does not fall by more than a pre-agreed threshold (value: question Q-P-01).

| ID | Element | Verifiable? |
|---|---|---|
| H-01 | A mandatory phone does not scare visitors away | Yes |

## 2. Smallest verifiable slice

| ID | In the slice | Outside the slice |
|---|---|---|
| SLICE-01 | Mandatory phone in the form on the "Contacts" page (form and API) | PDF attachment (IN-02 and RULE-06 of the specification, postponed) |
| SLICE-02 | Measuring the number of enquiries before and after (demo data, internal pilot) | Connecting the notification email (DEP-02) |
| SLICE-03 | Showing the phone error in Ukrainian and English | Changing other forms (`GetNotesModal`, OUT-03) |

## 3. Type

☒ PoC (learn) ☐ MVP. Rationale: it is unknown whether a mandatory phone will scare visitors away, so a signal from an internal pilot is needed first. No commitments for production.

## 4. Success signals

| ID | Signal | PoC threshold | Production threshold | How we measure |
|---|---|---|---|---|
| SIG-P-01 | Share of enquiries with a valid phone | 100% in the pilot | 100% and under 2% abandonments because of the phone | Demo scenarios, then analytics |
| SIG-P-02 | Change in the number of enquiries | No critical drop (threshold: Q-P-01) | Agreed threshold on real traffic | Week-to-week comparison |

## 5. Start blockers

| ID | Question | Owner |
|---|---|---|
| Q-P-01 | What drop in the number of enquiries is acceptable? | Product |
| Q-P-02 | Who are the pilot users (internal or partners)? | Product |
| Q-P-03 | Is the phone mandatory for all forms or only "Contacts" (Q-04 of the specification)? | Product |

## 6. Traceability to the parent specification

| Parent ID | How the slice uses it |
|---|---|
| RULE-03 | Basis of the slice (mandatory phone) |
| AC-01, AC-02 | Acceptance signals of the slice (empty and wrong phone) |
| OUT-01 | Other file types are outside the slice; attachments (RULE-06) postponed |
| OUT-03 | Other forms postponed |

## Checklist

- [x] The slice is smaller than the full feature
- [x] The hypothesis can be refuted within 2 weeks
- [x] Production commitments are explicit (there are none)
- [x] Links to at least 2 parent IDs
