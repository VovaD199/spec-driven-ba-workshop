# AI check notes (example)

> FALLBACK EXAMPLE for Day 4. This is an **example of structure and tone**: the AI claims and verdicts are illustrative, because your own run produces them. Fill in your own notes after you do steps 2–4 of block 6 yourself (see `fallback/en/README.md`). The Invented count here is **not a metric**: what matters is that you checked the claims against the specification.

## Claim audit (5 random Grounded)

| AI claim | AI label | Quote from the specification (ID, section) | Confirmed? | My verdict |
|---|---|---|---|---|
| "The phone is mandatory in the form and on the server" | Grounded | RULE-03: "Phone mandatory; format `+` and digits, 11–16 characters" (section 4) | Yes | Correct |
| "Attachment up to 10 MB" | Grounded | RULE-06 / NFR-02: "PDF only, up to 5 MB" (sections 4, NFR) | **No** | The number is invented; the AI labelled it Grounded without a quote. Fixed to 5 MB |
| "The notification goes to the Foundation's mailbox" | Grounded | ASM-02 (section 6) | Partly | This is an assumption, not a rule: Q-03 is open. Label changed to Inferred |
| "Consent to the policy is checked on the server" | Grounded | RULE-05: "UI only", Q-08 (sections 4, 7) | **No** | The opposite of what the specification says |
| "Errors are shown in the interface language" | Grounded | NFR-03, AC-11 (NFR, section 8) | Yes | Correct, but "interface language" is still being clarified (Q-16) |

## What turned out to be Invented and what the specification lacked:
The file size limit (10 MB) and the server-side consent check were invented by the AI although labelled Grounded. The specification lacked an explicit "Agreed / Open" status next to the rules.

## Which gap I closed and how:
I added a note "Agreed (simulation) / Open Q-08" to RULE-05 and RULE-06, and marked the status of every row in the traceability matrix. This closed the place where the AI took an invention for a fact.

## Result of the re-run:
After the re-run the audit of the same types of claims again found one invention (the error language for mixed languages): the AI labelled it Inferred, and the quote pointed to Q-16. This is the right behaviour: the invention became an open question, not a fact.

## What surprised me:
The AI labels as Grounded even what is not in the specification if it sounds plausible (10 MB). Without a quote with an ID the label is worth nothing: you must check the quote, not the label.
