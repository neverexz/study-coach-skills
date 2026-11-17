# Study Coach Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add one entrypoint that routes learner requests across the six existing skills while preserving pending work and shared evidence.

**Architecture:** One new `skills/study-coach/SKILL.md` loads sibling instructions as needed. The existing course, assessment and storage contracts remain authoritative; no runtime or parallel state is added.

**Tech Stack:** Markdown, JSON behavior scenarios, existing Python/PyYAML offline checks.

**Spec:** `docs/superpowers/specs/2026-11-17-study-coach-design.md`

## Global Constraints

- Preserve all six standalone entrypoints and the existing state/evidence contract.
- One leading mode per actionable part, one attempt per actual response, one coordinated save per turn.
- Preserve pending IDs, partial groups, source position and assistance when switching.
- Read actual sibling SKILL.md files; no fictional skill-call API or assumed successful loads.
- Missing modules and unavailable writes must have explicit, limited fallbacks.
- No textbook generation, new backend, global installation, merge or push.

## Review Focus

- An answer plus a side question: process the answer once, then help without consuming unanswered siblings.
- A hinted answer after a mode switch: retain assistance and avoid independent mastery credit.
- Resume among multiple courses: clarify identity before reading/writing one as selected.
- Missing skill or contract: explain the missing capability and keep unsupported mastery provisional.
- A failed read/save: distinguish performed work from a proposed handoff and retain original state.

### Task 1: Router and behavioral contract

**Files:** create `skills/study-coach/SKILL.md`, `tests/study-coach-scenarios.json`.
**Consumes:** sibling entrypoints, state format v1 and evidence-rules, actual learner messages.
**Produces:** selected workflow instructions, preserved learner context and one coordinated outcome.

- [ ] Create realistic route and transition inputs with separate evaluator criteria; stage blind requests under ignored work.
- [ ] Run five fresh controls with existing skills and no new master; record actual responses and gaps without forcing a failure claim.
- [ ] Write a compact entrypoint with six route pointers, context restoration, compound-turn sequencing, assistance and one-save ownership; no extra reference unless it earns its size.
- [ ] Run five fresh guided samples on the same transition inputs; read every response.
- [ ] Perform an actual temporary-course transition: grade one submitted item, explain a source passage, preserve two pending siblings, save exactly once.
- [ ] Test missing module and ambiguous resume in isolated fixtures; fix only observed gaps and re-test them.
- [ ] Run bundled quick validator and `python3 tools/validate.py`; commit verified skill and scenarios.

### Task 2: Package integration and final review

**Files:** modify README, `docs/evaluation.md`, `docs/provenance.md`; complete this plan.
**Consumes:** verified Task 1 package; no new production interfaces.

- [ ] Make study-coach the README starting point, retain six direct examples, update current package count to seven and full-bundle installation instructions.
- [ ] Record measured observations and limits; identify master routing as this project's adaptation rather than copied DeepTutor behavior.
- [ ] Run `python3 -m unittest discover -s tests -v`, both validators for all seven packages and an installation-copy/local-link smoke check.
- [ ] Commit integration docs; request one fresh whole-change review against the spec and the five Review Focus cases.
- [ ] Resolve material findings with targeted reproduction and fresh verification; report any untested limits honestly.
- [ ] Verify clean tracked status and leave local commits on the existing feature branch for later publication.

## Execution decisions

Reuse `codex/deeptutor-learning-skills` in the supplied checkout. Execute inline with independent behavioral agents and a final reviewer, following the user's explicit approval to implement. No further execution-method approval is needed. Existing tests/checker stay unchanged unless the new package exposes a genuine integrity-check gap.
