# Study Coach — AI Agent Skills for Learning

**English** | [Русский](README.ru.md)

AI agent skills for learning with Codex: tutoring, source-based study, guided
problem solving, adaptive practice, research and persistent progress.

One study coach, six focused workflows, and shared learning progress.

Seven learning skills for Codex, inspired by
[DeepTutor](https://github.com/HKUDS/DeepTutor): the `study-coach` coordinator and
six standalone workflows for mastering a topic, studying materials, solving
problems, practicing, researching, and continuing study across chats.

The bundle contains instructions and small reference files. You do not need to
install DeepTutor, configure its server, or transfer API keys. `mastery-tutor` is
a new skill; it does not modify an existing `socratic-tutor` installation.

## Start with one entry point

After installing the bundle, select your study project and write:

```text
$study-coach I want to master SQL using these materials. Start with examples.
```

Then use ordinary language: “explain this passage,” “give me one hint,” “let’s
practice,” or “show my progress.” The coordinator reads the instructions for the
relevant workflow and uses the shared course state. Switching workflows preserves
unfinished tasks, records of assistance, and your position in the material.

To continue in a new chat, open the same study project:

```text
$study-coach Resume the sql course from where we left off.
```

If several courses match, the coordinator asks which one to use. It saves through
the same `learning-progress` skill and has no separate storage.

## Workflows

| Skill | Example prompt |
| --- | --- |
| [study-coach](skills/study-coach/SKILL.md) | `$study-coach Help me study these materials and choose the appropriate workflow.` |
| [mastery-tutor](skills/mastery-tutor/SKILL.md) | `$mastery-tutor Teach me to solve percentage problems. Start with examples.` |
| [source-study](skills/source-study/SKILL.md) | `$source-study Walk me through section 2 of this PDF. Explain how the formulas relate to the diagram.` |
| [guided-solve](skills/guided-solve/SKILL.md) | `$guided-solve Help me with this problem. Give me just one hint for now.` |
| [adaptive-practice](skills/adaptive-practice/SKILL.md) | `$adaptive-practice Prepare me for an exam using these materials and my mistakes.` |
| [learning-research](skills/learning-research/SKILL.md) | `$learning-research Investigate this field and compare approaches using primary sources.` |
| [learning-progress](skills/learning-progress/SKILL.md) | `$learning-progress Save this session so we can resume it in a new chat.` |

Tasks and pace adapt to your goal. Explanations, assisted solutions, independent
assessment, and claims such as “I know this” are recorded separately. You can ask
for a worked solution or defer a goal; neither counts as evidence of mastery.

## Install for a project

Clone or download the repository. From its root, copy **all seven folders** into
`.agents/skills` in the project where you will study. Replace the path below:

```bash
STUDY_PROJECT=/absolute/path/to/your-project
mkdir -p "$STUDY_PROJECT/.agents/skills"
cp -R -n skills/. "$STUDY_PROJECT/.agents/skills/"
```

`-n` preserves existing files. If packages with the same names are already
installed, compare them first: this command does not fully update an existing
installation. For personal use across projects, you can place the same bundle in
`~/.agents/skills`. Cross-references rely on neighboring folders with their
original names.

Codex supports project and user `.agents/skills` directories. In the CLI, use
`$skill-name` or `/skills` to select a skill explicitly. If changes do not appear,
restart Codex. See the [official documentation](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).

All six focused workflows remain directly accessible. You can install just one
for a one-off task. Compatible progress saving requires a neighboring
`learning-progress` skill. If the shared contract is unavailable, the skill
continues the current task and offers a summary you can carry to another chat.
In standalone `mastery-tutor`, the final mastery status remains provisional until
the shared assessment rules are available.

Install the full bundle for `study-coach`: it loads neighboring packages as
needed. If a module is missing, it identifies the unavailable workflow and works
within the available materials and instructions.

## Materials and progress

Attach accessible files, excerpts, and links. Search, PDF and diagram viewing,
code execution, and network access depend on the tools in your environment. An
inaccessible diagram or unreliable answer key results in “not assessed,” rather
than a learner error.

Course state is stored in **your study project**:

```text
learning/<topic-slug>/
  state.json
  journal.md
```

In a new chat, select the same project and ask to resume the relevant course.
If file writing is unavailable, the skill provides a portable state block and
reports that nothing was saved. Local answer keys are accessible to the file
owner; withholding them until after an answer is a presentation rule, not access
control.

Review dates form a queue for the next session. They do not create reminders or
background study sessions. Mastery thresholds and review intervals are documented
working heuristics.

## Validation and development

The skills themselves do not require Python. To validate the repository:

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m unittest discover -s tests -v
python3 tools/validate.py
```

The GitHub Actions workflow runs the same metadata, reference, and JSON checks.
These verify package integrity. Independent trials of tutoring behavior and
their limitations are documented in [docs/evaluation.md](docs/evaluation.md)
(in Russian).

## Sources

The instructions were written from scratch after analyzing DeepTutor v1.7.3,
without its runtime or internal tools. See the
[map of primary sources and original design decisions](docs/provenance.md)
(in Russian). Textbook generation is outside the scope of this bundle.

License: [Apache 2.0](LICENSE).
