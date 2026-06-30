# Sample Platform Schedule

## Project

AI Server Platform X100

This sample schedule is fictional and is used to demonstrate Plan-to-Production Intelligence System workflows.

---

## Milestones

| Milestone            | Target Date | Description                                                                  |
| -------------------- | ----------: | ---------------------------------------------------------------------------- |
| Plan Complete        |  2026-07-15 | Product scope, architecture assumptions, and RFQ package reviewed            |
| Requirement Complete |  2026-08-01 | Function-level requirements and feature checklists completed                 |
| Feature Complete     |  2026-09-15 | BIOS, BMC, EC, Driver, OS, and Application features implemented and testable |
| DVT Hardware Ready   |  2026-09-30 | DVT hardware available for validation and stress testing                     |
| Pilot Build Start    |  2026-10-15 | Pilot systems built for validation and customer qualification                |
| Pilot Exit           |  2026-11-01 | Sev1 and gating issues closed or approved with recovery plan                 |
| Production Readiness |  2026-11-30 | Production build exit readiness confirmed                                    |
| RFD                  |  2026-12-10 | Ready for Fulfillment Decision                                               |
| RTS                  |  2026-12-20 | Ready to Ship                                                                |
| Sustaining Handoff   |  2027-01-15 | Remaining approved issues transferred to sustaining team                     |

---

## Milestone Readiness Criteria

### Requirement Complete

* All major requirement documents reviewed.
* Function-level feature checklists generated.
* Owners assigned for BIOS, BMC, EC, Driver, OS, Application, Validation, Factory, and Quality.
* Cross-team dependencies identified.
* Open requirement questions documented.

### Feature Complete

* Required BIOS features implemented and testable.
* Required BMC features implemented and testable.
* EC / MCU firmware supports power sequencing and recovery behavior.
* Driver and OS integration are ready for pilot validation.
* Validation test cases are aligned with feature checklist.
* Critical upstream inputs delivered, including thermal tables and graphics configuration inputs.

### Pilot Exit

* Sev1 and gating issues closed.
* Sev2 issues have recovery plans.
* Reproducibility confirmed for critical issues.
* Machine availability confirmed for debug owners.
* QT verification status available for closed issues.
* Resource gaps escalated if issue volume exceeds team capacity.

### Production Readiness

* Must-fix issues closed.
* ATS and post-RTS candidates approved by required stakeholders.
* AQE, Manufacturing, Validation, Services, and Program teams aligned.
* Production build exit risk reviewed.
* Factory diagnostics ready.
* Production blocking risks closed or accepted.

### Sustaining Handoff

* Remaining open issues documented.
* Approved recovery plans transferred.
* Fix timing agreed.
* QT verification status documented.
* Sustain team accepts handoff package.
