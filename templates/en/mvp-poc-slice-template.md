# PoC/MVP slice template (owner: analyst)

Use when the team needs **time-boxed validation** before full delivery. It does not replace the full specification template. Link to the parent feature: `FEAT-____`.

---

## Header
| Field | Value |
|-------|-------|
| Slice ID | POC-____ |
| Parent feature | FEAT-____ |
| Type | PoC / MVP / Spike |
| Owner (analyst) | |
| Technical partner | |
| Target window | e.g. 2 weeks |
| Status | Draft / Approved / In progress / Done |

---

## 1. Hypothesis
**We believe that** …  
**For** … (segment / actor)  
**Will achieve** … (observable outcome)  
**We will know we are right when** … (signal)

| ID | Hypothesis element | Testable? |
|----|--------------------|-----------|
| H-01 | | Yes / No |

**Good enough:** one sentence a stakeholder can repeat without reading the full spec.

---

## 2. Smallest testable slice
| ID | In the slice | Outside the slice (defer) |
|----|--------------|---------------------------|
| SLICE-01 | | |
| SLICE-02 | | |

- [ ] Fits the agreed time box (e.g. ≤ 2 weeks)
- [ ] No production commitments unless stated in §4
- [ ] Fake / manual steps are documented, if any

---

## 3. Intent: MVP or PoC
| Dimension | PoC (learn) | MVP (minimum value) |
|-----------|-------------|---------------------|
| Main goal | Test an assumption | Ship useful value |
| Audience | Internal + friendly pilots | Real users |
| Quality bar | Enough to see the signal | Enough to support and measure |
| Success | Learned / stopped / changed course | Retention / conversion / operation |

**This initiative:** ☐ PoC  ☐ MVP  ☐ Hybrid (explain below)

---

## 4. Success signals: PoC vs production
| ID | Signal | PoC threshold | Production threshold | How we measure |
|----|--------|---------------|----------------------|----------------|
| SIG-P-01 | | | | |
| SIG-P-02 | | | | |

**Enough for a PoC:** at least one **quantitative** and one **qualitative** signal with an owner and a date.

---

## 5. Blocking open questions
| ID | Question | Blocks | Owner | Due |
|----|----------|--------|-------|-----|
| Q-P-01 | | | | |

---

## Slice checklist (before start)
- [ ] Hypothesis is falsifiable
- [ ] Slice IN/OUT reviewed with engineering
- [ ] PoC vs MVP intent agreed with the sponsor
- [ ] Success signals have owners and dates
- [ ] Parent RULE/OUT IDs listed below

## Traceability to the parent specification
| Parent item ID | How the slice uses it |
|----------------|-----------------------|
| RULE-01 | |
| OUT-02 | |

---

## Anti-patterns
- PoC scope creep disguised as "one more story"
- MVP without a support/operations plan when real users are in scope
- Success signals that only measure "we shipped code"
