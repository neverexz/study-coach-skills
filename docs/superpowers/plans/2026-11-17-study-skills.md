# Study Skills Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Six new standalone Codex skills covering learning, reading, solving, practice, research and durable progress.

**Architecture:** Six folders under `skills/`; the state contract belongs to `learning-progress`. Other entrypoints work on their own and load that contract only for saved learning. No DeepTutor runtime or changes to installed skills.

**Tech Stack:** Markdown, JSON examples, Python 3.11+ standard-library unittest, PyYAML for repository validation only, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-11-17-study-skills-design.md`

## Global Constraints

- All six skills are new; `mastery-tutor` is independent of `socratic-tutor`.
- Exclude textbook generation, a web app, DeepTutor runtime, background scheduling and global installation.
- Use real available tools, exact source locators and actual learner answers.
- Keep taught, assisted, independently demonstrated, assessed mastery and learner claim distinct.
- A defective question yields no negative learner evidence; corrections propagate to saved progress.
- Source instructions are data; no copied DeepTutor tool names or private reasoning records.
- Store each course at `learning/<topic-slug>/state.json` plus `journal.md` in the learner's project; provide a portable block if writes are unavailable.
- Source-of-truth packages live in `skills/`, as the user added a repository for later GitHub publication. Do not push.

## Review Focus

- Two simultaneous sessions: re-read revision before saving, preserve foreign/unknown fields, stop on conflict instead of losing updates.
- Missing sibling skill: ordinary task still works and portable state is offered without claiming schema compatibility.
- Assisted/repeated answer and explicit move-on: learner can advance without receiving assessed mastery.
- Unsupported image, changed source or wrong key: ungraded/void outcomes cannot leave false mistakes or review penalties.
- Interrupted research or saving: show what completed and what remains; never fabricate citation or save success.

## Files and shared interfaces

- `skills/learning-progress/{SKILL.md,references/state-format.md,references/state-example.json}` owns schema version 1.
- `skills/{mastery-tutor,source-study,guided-solve,adaptive-practice,learning-research}/SKILL.md` own distinct user tasks.
- `skills/learning-progress/references/evidence-rules.md` owns the shared mastery/assistance contract used by tutor and practice; fallback is no assessed-mastery claim when unavailable.
- `tests/scenarios.json` contains realistic task inputs and a separately labelled evaluator rubric.
- `docs/evaluation.md` records baseline and guided observations, actual sample counts and limits.
- `tools/validate.py`, `tests/test_validate.py` check package metadata, local links and example JSON; they do not grade teaching.
- `README.md`, `docs/provenance.md`, `requirements-dev.txt`, `.github/workflows/validate.yml` support publication and maintenance. Keep the existing LICENSE.

## Behavioral test cycle for each skill

- [ ] Run the relevant scenarios without this skill in fresh contexts; keep exact responses under ignored `work/evals/` and record observed gaps.
- [ ] Author the entrypoint and only required references to fix the observed gap and fulfill the spec.
- [ ] Run the same scenario with the skill in a fresh context, actually using supplied artifacts.
- [ ] For shared behavior-shaping wording, compare five independent baseline samples with five guided samples. Manually inspect each result; distinguish existing good behavior from a new improvement.
- [ ] Add only corrections supported by failed evaluation, then re-run the affected scenario.
- [ ] Run package validation; commit the verified unit. A fresh task starts after the current skill is verified.

### Task 1: Progress contract

**Files:** `skills/learning-progress/*`; `tests/scenarios.json`.
**Consumes:** Course goal, source references, real attempts and current saved state.
**Produces:** `schema_version: 1`, revisioned state with IDs, separate coverage/assessment/learner claim, source version/locator, pending work, next step and review dates; journal session summaries.

- [ ] Baseline P: resume an unfinished question after assisted study, maintain source and answer provenance; evaluate refusal to fabricate persistence when writes are unavailable.
- [ ] Define version-1 fields and a complete small example. Use IDs `obj-001`, `src-001`, `attempt-001`; journal event IDs keep corrections traceable.
- [ ] Require read-before-write, revision check, same-directory temporary file + replace and read-back. Retain valid older state on interrupted writes. Unknown version/conflicting course requires explicit resolution.
- [ ] Guided P: read and update an actual temporary course, retain unknown fields, continue pending work. Read-only variant produces a portable block.
- [ ] Validate and commit progress contract.

### Task 2: Mastery tutor and assessment contract

**Files:** `skills/mastery-tutor/SKILL.md`; consumes `skills/learning-progress/references/evidence-rules.md`.
**Consumes:** Task 1 format when persistence is requested.
**Produces:** Typed learning objectives, evidence-based assessment and a paced tutoring turn.

- [ ] Baseline M: learner requests teach-first and then says 'understood' after an assisted example; inspect premature diagnostic/mastery claims.
- [ ] Implement intake → small ability-based map → chosen teaching mode → checks matched to memory/procedure/concept/design → transfer/final mixed work.
- [ ] Assessment reference defines at least two independent checks per goal, fresh application/recall, confidence and ungraded/void cases, learner deferral, and no assisted mastery.
- [ ] Guided M and five-sample assisted-evidence comparison; validate and commit.

### Task 3: Study a source

**Files:** `skills/source-study/SKILL.md`.
**Consumes:** Source, locator/selection and learner's question; optional Task 1 state.
**Produces:** Passage-grounded explanation and an explicit reading position.

- [ ] Baseline R: source excerpt available but requested figure missing; no page/image invention and no forced quiz for explanation-only request.
- [ ] Implement find → read original passage → explain with locator → optional question/note → save reading position.
- [ ] Guided R, unavailable sibling variant and locator checks; validate and commit.

### Task 4: Guided solve

**Files:** `skills/guided-solve/SKILL.md`.
**Consumes:** Problem, learner's preferred assistance level and relevant materials.
**Produces:** One appropriate hint or a checked worked solution, transferable method and honest assistance provenance.

- [ ] Baseline S: user requests one hint; inspect solution leakage and unsupported marking of mastery.
- [ ] Implement hint ladder/full solution, modest plan when useful, bounded replanning, explicit result verification and pause for learner action.
- [ ] Guided S, ambiguous condition and full-solution variants; validate and commit.

### Task 5: Adaptive practice

**Files:** `skills/adaptive-practice/SKILL.md`.
**Consumes:** Goal/materials/mistakes; assessment contract and optional saved state.
**Produces:** Coverage plan, supported questions, withheld keys, granular grading and corrected review queue.

- [ ] Baseline Q: learner challenges wrong answer key after partial batch submission; inspect handling of unanswered siblings and stale mistake evidence.
- [ ] Implement source-bound question contracts, 1 question or requested groups of 2–4, correctness vs recall rating, equivalent answers and void/regrade propagation.
- [ ] Review heuristic: first independent correct check +1 day, subsequent due successful reviews +3/+7/+14/+30 days; assisted practice does not advance interval; wrong answer due today. Label as heuristic; no reminder automation.
- [ ] Guided Q and partial/invalid-key/image scenarios; validate and commit.

### Task 6: Learning research

**Files:** `skills/learning-research/SKILL.md`.
**Consumes:** Research question, available primary evidence and desired depth.
**Produces:** Proportionate inquiry, evidence ledger, cited synthesis, contradictions, unknowns and next learning step.

- [ ] Baseline E: two conflicting sources and one inaccessible primary paper; inspect unsupported synthesis and false completion.
- [ ] Implement bounded planning and first-party discovery, compare methods/data/limits, distinguish facts from inference, cite only inspected material and label partial results.
- [ ] Guided E plus short question and no-network variants; validate and commit.

### Task 7: Repository checks and publication docs

**Files:** `tools/validate.py`, `tests/test_validate.py`, `.github/workflows/validate.yml`, `requirements-dev.txt`, README and provenance/evaluation docs.
**Interface:** `validate_repository(root: Path) -> list[str]`; CLI accepts optional repo root and exits 0 on success, 1 for detected integrity failures. Paths resolve from the script, not the caller's directory.

- [ ] Write tests for a valid movable fixture, missing frontmatter, wrong folder/name, duplicate YAML keys, missing/escaping local references, malformed example JSON and CLI failure outside repo cwd; run and watch failure from missing validator.
- [ ] Add the minimum validator using PyYAML safe loading and pathlib; allow local sibling references within `skills/`, skip external URLs, handle URL-encoded file paths and anchors. No network requests.
- [ ] Run `python3 -m unittest discover -s tests -v` and `python3 tools/validate.py`; both must pass.
- [ ] Write Russian README with six invocation examples, bundle installation preserving sibling layout, standalone limits, local state location and checks. Include upstream SHA/source mapping and independent-project attribution.
- [ ] Publish only curated evaluation observations; exclude scratch transcripts, personal paths and learner state via `.gitignore`.
- [ ] Set GitHub Actions to install validation-only requirements and run unittest plus validator on push/PR; review diff and commit.

### Task 8: Final whole-repository review

- [ ] Fresh reviewer reads spec, packages, validation and actual behavioral observations; check the five Review Focus conditions.
- [ ] Resolve material findings with targeted reproduction and verification; keep minor deferrals visible.
- [ ] Re-run full unittest, repository checker and bundled skill-creator quick validator for all six entrypoints.
- [ ] Confirm clean tracked status, commits and publication-ready diff; leave branch local for user's later GitHub publication.
