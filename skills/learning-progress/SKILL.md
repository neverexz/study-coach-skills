---
name: learning-progress
description: Use when a learner wants to save or resume a course, inspect learning evidence, correct recorded progress, or carry an unfinished study session into another chat.
---

# Learning Progress

Make the next session start from what the learner actually did. Teaching coverage,
assessed mastery and the learner's own claim are separate records.

## Save or resume

1. Identify the course from the learner's choice or current session. Look for
   `learning/<topic-slug>/state.json` in the learner's working project, not in the
   installed skill folder. If several courses fit, ask which one; retain their IDs.
2. Before reading or writing saved state, load [state-format.md](references/state-format.md).
   It defines version 1, source locators, open questions, revision checks and saving.
   Current records come from the learner's supplied snapshot or the selected project's
   actual `state.json`. The bundled `state-example.json` is fictional format data.
   With no current snapshot, label a handoff as proposed and leave existing revision,
   IDs and source versions unknown; any newly assigned ID must be identified as new.
   An old chat summary is a pointer, not proof that a file was read.
3. Resume with a short account of the goal, last observed work and open next step.
   Retain unanswered questions. Ask for missing context rather than treating an
   interrupted session as completed work.
4. Record meaningful outcomes from actual learner messages, including assistance,
   source and any uncertainty. For assessing or repairing outcomes, load
   [evidence-rules.md](references/evidence-rules.md). A request to advance can defer a
   goal without awarding mastery.
5. Save the changed state and a concise session entry in `journal.md` using the
   write protocol in the format reference. Report saved status only after read-back.
   If journal append fails after state succeeds, report that partial result.

## When files cannot be written

Provide a portable state block and say it has not been saved. Keep its course,
goal, source positions, assisted/independent evidence, pending questions and next
step. Omit keys for unanswered questions; mark them for reconstruction from sources.
If space is limited, preserve these fields before optional history. Label an
abbreviated block as a summary rather than a complete version-1 snapshot.

## Quick decisions

| Situation | Record/action |
| --- | --- |
| Explanation or copied worked answer | Coverage/assisted evidence |
| Learner says “I know it” | Learner claim, distinct from assessment |
| Bad key or unreadable source | Repair or ungraded outcome; recompute dependent records |
| Course/version/revision conflicts | Preserve the file and resolve the conflict |
| No filesystem operations | Portable handoff, no save claim |

Example: “I repeated 6/8 = 3/4 after your hint; 9/12 is unanswered” leaves
independent mastery unassessed and resumes with 9/12. It does not repeat the solved
example or reveal the pending answer.

Keep a compact journal of results, decisions and next actions. Store source text
and learner evidence only as needed; private model reasoning is not a learning record.
