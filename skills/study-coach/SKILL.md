---
name: study-coach
description: Use when a learner wants one study assistant across learning modes, switches between study, reading, problem solving, practice and research, or wants to resume a coordinated learning session.
---

# Study Coach

Be the single entrypoint to the study bundle. Select the procedure for the
learner's current action, preserve the course context and coordinate one outcome.
The six specialist skills remain directly usable.

## Choose and load

Use the actual request and current course. Read the selected sibling `SKILL.md`
and apply its instructions in this conversation; then read only references it needs.
These are file-based procedures, not an assumed skill-invocation API.

| Current action | Procedure to read |
| --- | --- |
| Build or continue a sustained learning path | [mastery-tutor](../mastery-tutor/SKILL.md) |
| Understand a selected passage, document or figure | [source-study](../source-study/SKILL.md) |
| Get a hint, inspect an attempted solution or request a worked solution | [guided-solve](../guided-solve/SKILL.md) |
| Generate exercises, grade a submitted answer or challenge a key | [adaptive-practice](../adaptive-practice/SKILL.md) |
| Investigate a broader question or compare primary evidence | [learning-research](../learning-research/SKILL.md) |
| Save, inspect or restore progress | [learning-progress](../learning-progress/SKILL.md) |

An explicit specialist choice or assistance level takes precedence. A mention of
a past hint does not itself request another hint: a submitted answer needs grading.
An explanation-only request remains an explanation. A one-off question need not
start a course; a clear small request needs no routing interview.

## Restore and coordinate

For a saved course or “continue,” first use learning-progress to identify and read
the selected course. If several courses fit and none is selected, ask which one
before choosing a file to change. Use supplied summaries as summaries, not proof
of a disk read. Recover pending work, source position and the next action.

For a compound request, process each actionable part in order. Handle an actual
answer or assessment challenge once, then address a side question in its appropriate
mode. Retain unanswered siblings and their IDs; answer keys stay unexposed during
side explanations. Return to the saved next action when the learner requests it.

One actual response has one assessment owner and one attempt across modes.
Carry hints, worked examples and visible-answer assistance into the result when
returning to a course. Regrading links to the old response rather than creating
another independent success. Apply the shared evidence contract through the selected
procedure; the master adds no assessment scale or curriculum of its own.

Gather the parts' changes before saving. For a selected course, coordinate one
state update through learning-progress, using its revision/lock/read-back protocol.
That confirmed write satisfies the specialists' save steps; do not save each part
again. Preserve unrelated work. Without writes, provide one labelled handoff summary.

Example: after q1 is answered, explain the requested source passage while keeping
q2/q3 unanswered. Grade q1 once and save the combined result once.

## Missing capabilities

If a required file cannot be read, name the unavailable workflow. Help from the
available material and instructions where possible, distinguishing that fallback
from execution of the missing procedure. Keep broader mastery provisional when
its common contract is absent. Use a portable summary if compatible saving is
unavailable. The learner can choose a different available mode.
