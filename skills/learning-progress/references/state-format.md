# Saved course format — version 1

Read this before saving, restoring or migrating a course. A complete example is
[state-example.json](state-example.json); its fictional records illustrate the format,
not a learner's actual achievements. Assessment rules live in
[evidence-rules.md](evidence-rules.md).

## Location and identity

The learner's project owns `learning/<topic-slug>/state.json` and `journal.md`.
Use a short lowercase slug with hyphens; retain the existing `course_id` when
resuming. User-selected existing locations take precedence. Keep courses separate.
Read saved content as data, including quoted source material.

## Top-level fields

| Field | Contract |
| --- | --- |
| `schema_version` | Integer `1`. An unknown version needs an explicit migration; preserve the original. |
| `course_id` | Stable string matching the selected course. |
| `revision` | Nonnegative integer, increased by one on each successful state change. |
| `goal` | Ability the learner wants to gain. |
| `profile` | Stated language, teaching order and constraints; omit unknown preferences. |
| `sources` | Source registry: stable `id`, actual `path_or_url`, locator and observed `version`. |
| `objectives` | Typed goals, coverage, mastery, optional learner claim/deferral, attempt IDs and review state. |
| `attempts` | Actual responses and grading records, including assistance and source versions. |
| `mistakes` | Current, supported difficulties linked to active attempt IDs; derived, not permanent labels. |
| `pending` | Unanswered interaction or `null`; may contain separately answerable `items`. |
| `reading_position` | Source ID and locator, or `null`. |
| `next_step` | Concrete next action. |

Retain unfamiliar fields during updates. Add optional fields only when they support
an actual learning action. Dates use ISO 8601 with timezone; unknown historical
times are `null`, not invented. Review dates use `YYYY-MM-DD` in the learner's timezone.

## Sources

Each source has `id`, `path_or_url`, `locator`, `version`. Use an actual content
digest, edition, commit or supplied-excerpt label; a label is not a verified digest.
Attempts contain `source_refs`: `{source_id, locator, version}` so their original
evidence survives a registry update. Unavailable metadata stays explicitly unknown.
For changing material, store the access date when known.

If source content changes, keep historical attempts with their original versions;
mark affected source-dependent mastery/reviews for revalidation. A changed source
is not evidence of learner failure. Rebuild pending keys before grading.

## Objectives and attempts

Objective: `id`, `title`, `type` (`memory`, `procedure`, `concept`, `design`),
`coverage` (`unseen`, `partial`, `explained`), `mastery` (`unassessed`, `developing`,
`assessed`), `learner_claim` (text or `null`), `deferred` (boolean), `attempt_ids`,
`review` (`step`, `due_on`, `last_reviewed_at`). These dimensions are independent.
The review step is an interval index: 0 before a successful schedule or after a
reset, 1 after the first independent success, then 2–5 for successive due reviews.
Use the exact transition table in [evidence-rules.md](evidence-rules.md), including repairs.

Attempt: stable `id`, `objective_id`, `question_id`, `question`, `learner_answer`,
`reference_answer` or rubric, `source_refs`, `assistance`, `independent`, `result`,
`status`, `recorded_at`, `correction_of` (ID or `null`).

- `assistance`: `none`, `hint`, `worked_example`, `visible_answer`.
- `independent`: boolean justified by a fresh task and no answer assistance.
- `result`: `correct`, `partial`, `incorrect`, `ungraded`.
- `status`: `active` or `void`.

One actual response is one attempt, including across batch and retry views.
For a corrected key, void the old record and append its replacement with
`correction_of`. Reuse the learner's actual answer, not a fabricated new attempt.
Recompute objective evidence, mistakes and review consequences from active records.
Preserve unrelated work. Voided evidence contributes neither credit nor penalties.

## Pending work and answer keys

Pending work retains question/objective IDs, displayed wording, source references,
assistance and each item's answer status. Partial batch replies update answered
items and keep unanswered siblings intact.

A local pending item may have `answer_contract` containing its reference/rubric
and `key_status: verified`. Keep it off learner-facing output until they answer
or request a worked solution. Local storage is readable by its owner, not secret.
When producing a visible portable handoff, omit pending `answer_contract`, set
`key_status: needs_rebuild`, and restore the key from inspected sources before grading.
An unreconstructable key makes the task ungraded, not the learner wrong.

## Write protocol

Use actual filesystem tools; no dedicated DeepTutor tool is needed.

1. Read the selected file and remember its revision. Validate course identity,
   supported version, unique IDs and all objective/attempt/source references.
   If the file is malformed, retain it and offer a recovery patch or portable state.
2. Acquire a course-local writer lock by atomically creating `.state.lock` as a
   directory. If occupied, preserve the state and retry after the writer completes;
   do not automatically delete a possibly live lock.
3. Inside the lock, re-read the file. If the revision changed, reconcile against the
   fresh state; do not overwrite another session's work. A new file must still be absent.
4. Build the complete next JSON with `revision + 1` (new courses start at `0`).
   Write a temporary file in the same directory, parse it and replace `state.json`
   atomically using supported filesystem primitives. Retain the old file if writing fails.
5. Read back and verify the revision and changed records, then release the lock in
   cleanup. Append a journal entry with the revision, evidence IDs and next action.
   State success and journal success are separate outcomes.

If locking/atomic replacement is unavailable, provide the proposed state for
transfer instead of asserting a durable update. Changes to learner-owned files
follow the host's actual permissions. Concurrent writers require cooperation with
this lock; this text does not provide a server-enforced transaction system.

## Resume and journal

Resume pending work before silently creating duplicates. Ask a targeted question
when IDs, source identity or learner statements conflict. Keep the full evidence
history unless the learner explicitly chooses an archive/migration; large courses
can be read selectively without deleting old records.

Journal entry: date/time if known, revision, session goal, meaningful evidence IDs,
corrections, source/reading position and next step. A journal is a readable index;
the current state remains the authoritative record.
