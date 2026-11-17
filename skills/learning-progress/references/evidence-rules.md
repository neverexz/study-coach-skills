# Evidence, assessment and review

Read when creating, grading or repairing learning evidence. These are transparent
working rules adapted from DeepTutor, not validated measurements of a learner's mind.

## Match the check to the objective

| Type | Evidence to seek |
| --- | --- |
| `memory` | Recall without seeing the answer, then a distinct recall/application check. |
| `procedure` | Perform the procedure on new inputs and explain/check a consequential step. |
| `concept` | Explain meaning and apply it to a new case or counterexample. |
| `design` | Make a defensible choice, explain tradeoffs and handle a changed constraint. |

Record coverage from teaching. Record attempts from actual learner answers. Award
`mastery: assessed` only after at least two distinct, active, independently correct
checks matched to the objective, with a fresh application or unprompted recall.
An immediate paraphrase/copy of a shown answer is assisted work. A result from an
unverified source/key or ambiguous grading is `ungraded`. A partial answer needs
specific feedback or clarification, not an automatic full pass.

The two-check threshold is a v1 heuristic. A future failed independent review
returns mastery to `developing`; do not erase earlier success. Self-report and
explicit advance/defer requests remain separate from assessed status.

## Assistance and grading

Record whether a hint, worked example or visible answer supported the response.
An assisted correct attempt is useful practice but does not satisfy an independent
check. Use supported equivalent wording and solutions; quote the learner's actual
answer or preserve it exactly in the record. Distinguish correctness from perceived
difficulty. If interpretation is uncertain, ask one focused clarification and keep
the attempt ungraded until there is a sound basis.

For visual tasks, inspect the original image/table and its locator before writing
the key. A labeled picture/direct table reading is guided practice. A generated
replacement is not evidence about an unavailable original figure.

## Repair

Inspect the disputed question, recorded learner answer, key/rubric and original
source. If defective, void it or append a supported corrected assessment linked to
the old record; recompute all dependent mastery, mistakes and review effects.
Unanswered siblings and unrelated attempts survive. If the only negative evidence
was voided, remove its mistake and review penalty. A correction is not an extra
independent success. The learner need not solve a defective question again.

## Review heuristic

`review.step` is the interval index, not an ability level. Use the same index for
new answers and corrected/replayed answers:

| Event | Stored step | Next due date |
| --- | --- | --- |
| First independently correct response, including after a reset | `1` | Answer date + 1 day |
| Independently correct due review at step 1/2/3/4 | `2`/`3`/`4`/`5` | Review date + 3/7/14/30 days respectively |
| Independently correct due review at step 5 | `5` | Review date + 30 days |
| Independently incorrect/partial response | `0` | Response date, due today |
| Assisted practice or ungraded/void outcome | Unchanged | No additional scheduling consequence |

An additional practice check before the due date does not advance the review
interval. Recompute corrections from remaining valid events with this same table;
when none remain, leave `due_on: null` and `step: 0`. If historical dates or review
context are missing, leave uncertain replay results provisional rather than inventing dates.

Store a date in the learner's timezone and explain why an item is due when useful.
Dates are a review queue, not reminders: no background work is created. If the
current date/timezone is unknown, ask or leave the due date unset.
