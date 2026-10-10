---
tags:
  - review-article
  - copilot
updated: 2026-10-10
---

# تعليمات كوبايلوت

> ⛔ **طريقة كوبايلوت اتلغت يوم 10/10.** الكتابة بقت بوكيل سونِت (`.claude/agents/academic-review-writer.md`).
> الملف ده لسه هو **المصدر الوحيد لقواعد الأسلوب** اللي في البلوك تحت، والوكيل بيقراه كل مرة. عدّل القواعد هنا بس.

> ابعت البلوك ده الأول، وبعدين ابعت الجمل واحدة واحدة.
> بعد ما تلصق النتيجة في `drafts/`، قول لـ Claude "خلصت" عشان يشغّل الفحص.

```
Edit my draft paragraph for a Q2 pharmacology review. Rules:
1. Keep every fact, number, unit, P value and [Tag] exactly. Do not add claims or sources.
2. Sentence length: average 22-25 words. Open each paragraph with one short topic
   sentence (6-10 words). Make 1 sentence in 7 long (36-44 words). Never exceed 45.
3. Never use ", and this" or ", so". Use ", which ..." or start a new sentence.
4. No trailing "-ing" comments (", suggesting...", ", leading to...", ", thereby...").
5. At most one opening connector per paragraph (However / Therefore / Similarly).
   At most 3 contrast openers (However, In contrast, Unlike, While) per section.
6. Hedge interpretations: about 1 sentence in 8 uses may / suggest / appear / likely.
   Never write "the only", "never", "always", "no study" without "to our knowledge".
7. Use the passive voice in about 1 sentence in 5 (e.g. "patients were randomized").
8. Define every abbreviation at first use: long form (ABBR).
9. Banned words: delve, pivotal, crucial, underscore, highlight, robust, promising,
   comprehensive, landscape, meaningful, warrant, foster, leverage, utilize, a total of,
   in order to, plays a key role, it is important to note, this section will.
10. Banned spoken words: cheap, switch on, work against, point to, helped, so far,
    for example, make less, tracked, big, a lot.
11. Do not copy 7 or more words in a row from the source paper. Rewrite number
    strings, e.g. "HR 1.00, 95% CI 0.82 to 1.22".
12. Change as few words as possible. Do not rewrite the paragraph from scratch.
Return only the edited text.
```
