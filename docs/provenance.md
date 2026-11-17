# Откуда взяты механизмы

Study Skills — самостоятельный набор инструкций для Codex, вдохновлённый
[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor). Это независимый проект;
его пакеты не требуют запуска DeepTutor и не являются официальным релизом HKUDS.

Исследован [commit 4c1e000d8563c5ac3b231baaaf149dc4dc4d2406](https://github.com/HKUDS/DeepTutor/commit/4c1e000d8563c5ac3b231baaaf149dc4dc4d2406),
релиз v1.7.3. Анализ выполнен 17 ноября 2026 по исходникам; приложение не запускалось.
Ссылки зафиксированы на этот срез, поэтому поздние изменения upstream здесь не подразумеваются.

| Механизм | Первичный источник | Адаптация |
| --- | --- | --- |
| Цели memory/procedure/concept/design, teach-first, локальная обратная связь | [mastery prompt](https://github.com/HKUDS/DeepTutor/blob/4c1e000d8563c5ac3b231baaaf149dc4dc4d2406/deeptutor/capabilities/mastery/prompts/en/mastery_loop.yaml#L100-L138) | `mastery-tutor`: выбор порядка преподавания и проверки по типу цели |
| Различение помощи, самостоятельной демонстрации и learner override | [policy.py](https://github.com/HKUDS/DeepTutor/blob/4c1e000d8563c5ac3b231baaaf149dc4dc4d2406/deeptutor/learning/policy.py#L82-L158) | Общий контракт evidence; явное происхождение результата |
| План покрытия и генерация отдельных вопросов | [question pipeline](https://github.com/HKUDS/DeepTutor/blob/4c1e000d8563c5ac3b231baaaf149dc4dc4d2406/deeptutor/agents/question/pipeline.py#L547-L608) | `adaptive-practice`: поддержанные вопросы, ключи и частичные ответы |
| Исправление дефектного задания | [repair tool](https://github.com/HKUDS/DeepTutor/blob/4c1e000d8563c5ac3b231baaaf149dc4dc4d2406/deeptutor/capabilities/mastery/tools.py#L2266-L2304) | Аннулирование/переоценка и пересчёт зависимых записей |
| План решения, контрольные результаты и ограничение перепланирования | [solve prompt](https://github.com/HKUDS/DeepTutor/blob/4c1e000d8563c5ac3b231baaaf149dc4dc4d2406/deeptutor/capabilities/solve/prompts/en/system.md#L1-L17) | `guided-solve`: подсказки или проверенный разбор без фиктивных tools |
| Чтение оригинального фрагмента до цитирования | [reading prompt](https://github.com/HKUDS/DeepTutor/blob/4c1e000d8563c5ac3b231baaaf149dc4dc4d2406/deeptutor/capabilities/reading/prompts/en/reading.yaml#L7-L54) | `source-study`: источник, позиция, вопрос и явные границы доступного материала |
| Сопоставление свидетельств и неполное исследование | [research evidence](https://github.com/HKUDS/DeepTutor/blob/4c1e000d8563c5ac3b231baaaf149dc4dc4d2406/deeptutor/agents/research/prompts/en/pipeline.yaml#L93-L176), [partial results](https://github.com/HKUDS/DeepTutor/blob/4c1e000d8563c5ac3b231baaaf149dc4dc4d2406/deeptutor/agents/research/pipeline.py#L585-L721) | `learning-research`: факты, выводы, расхождения и недоступные источники |
| Память с происхождением записей | [memory consolidator](https://github.com/HKUDS/DeepTutor/blob/4c1e000d8563c5ac3b231baaaf149dc4dc4d2406/deeptutor/services/memory/consolidator/__init__.py#L15-L30) | `learning-progress`: упрощённое явное состояние и журнал вместо автоматического L1/L2/L3 |

## Собственные решения

Инструкции написаны заново. В набор не переносились исходный runtime, имена
внутренних tools, сетевые сервисы, web UI или промпт-протокол THINK/TOOL/FINISH.
Существующий пользовательский `socratic-tutor` не использован как основа нового
пакета и не изменяется.

Формат состояния v1, порог двух самостоятельных проверок, интервалы повторения
1/3/7/14/30 дней, файловая блокировка и структура пакетов — решения этого проекта.
Они не объявляются научно валидированной оценкой освоения или точной копией
алгоритмов DeepTutor. Проверки поведения описаны в [evaluation.md](evaluation.md).

`study-coach` — дополнительный мастер-вход этого проекта. Он маршрутизирует
между готовыми шестью сценариями и согласует их работу с общим состоянием.
Его правила переключения и однократного учёта ответа написаны для этого набора;
они не объявляются отдельным компонентом исходного DeepTutor.

## Лицензия и авторство

Существующий [LICENSE](../LICENSE) репозитория — Apache License 2.0.
DeepTutor публикует свой [LICENSE](https://github.com/HKUDS/DeepTutor/blob/4c1e000d8563c5ac3b231baaaf149dc4dc4d2406/LICENSE)
с указанием Data Intelligence Lab, The University of Hong Kong (2025).
Здесь сохранено указание источника механизмов; знаки и название DeepTutor
используются для ссылки на исходный проект.
