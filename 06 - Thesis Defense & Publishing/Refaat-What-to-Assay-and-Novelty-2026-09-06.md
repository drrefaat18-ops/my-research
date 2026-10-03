---
title: أحلل إيه علشان أنشر دوليًا؟ — إعادة بناء مبنية على البروتوكول والأدلة
date: 2026-09-06
updated: 2026-10-02
type: research-decision
status: evidence-based-pending-supervisor-approval
confidence: moderate-high
supersedes: النسخة السابقة من نفس الملف (محفوظة في سجل التعديلات)
evidence: "[[evidence-2026-10-02/A-endpoints-survey]] · [[evidence-2026-10-02/B-endpoint-validity]] · [[evidence-2026-10-02/C-novelty]] · [[evidence-2026-10-02/D-stats]]"
tags: [thesis, assays, novelty, statistics, arrive, bjp, smash, rebuilt-2026-10-02]
---

# أحلل إيه علشان أنشر دوليًا؟

> [!info] الملف ده اتعاد من الأول يوم 2 أكتوبر 2026
> المرجع الملزم الوحيد هو نص البروتوكول المعتمد:
> ```
> 00-Sources/protocol/Protocol.pdf  (text: scripts/protocol_dump.txt)
> ```
> كل معلومة في الملف ده معاها رقم مرجع اتأكدنا منه مباشرة من قواعد البيانات.
> التفاصيل الكاملة وسجل كل استعلام موجودين في أربع ملفات أدلة داخل الفولدر ده:
> ```
> evidence-2026-10-02/
> ```

---

## 0. الخلاصة في سطور

1. القياسات اللي المحكّم بيدوّر عليها أولًا قياسات سريرية بسيطة ببلاش تقريبًا، والبروتوكول مفيهوش ولا واحد منها. لازم تتضاف:
```
Arthritis score + paw volume/thickness (serial) + body weight
```
2. القطاع النسيجي لازم يتاخد من الكاحل، مش الركبة، ومعاه صبغة الغضروف، والعظم يتفك تكلسه بمحلول الإديتا.
3. السيتوكينات التلاتة اللي في البروتوكول تفضل.
4. مؤشرات الإجهاد التأكسدي اللي طلبها د. أحمد مراد هي أرخص جزء ميكانيكي في الرسالة وأسهله تنفيذًا في بورسعيد.
5. تلات قياسات من البروتوكول نادرة في الأبحاث المنشورة، وهي أول حاجة ممكن تتشال لو الفلوس مش مكفية، لكن ده محتاج موافقة المشرف:
```
ACPA (7%) · TLR4 (~2%) · p38 MAPK (7%)
```
6. قياس إنزيم الإشارة ده بالصورة اللي في البروتوكول هيطلع نتيجة ثابتة مش مفهومة، لأن الأبحاث كلها بتقيس الصورة المفسفرة منه:
```
total p38 MAPK ELISA
```
7. التصميم الحالي مش هيقدر يثبت إن الدوا بيقلل جرعة الكورتيزون، لأن مفيش مجموعة بريدنيزولون 5 لوحدها. فيه حل من غير أي تكلفة إضافية (القسم 6).
8. العدد المقترح 8 حيوانات مريضة فعلًا في كل مجموعة.
9. الجدة موجودة لكن لازم تتصاغ بحدود. وفيه بحث مصري قريب جدًا لازم يتذكر:
```
Ashour 2019, Mod Rheumatol — gemfibrozil (PPARα agonist) + reduced prednisolone in AIA
```

---

## 1. ليه الملف القديم اتعاد

الأخطاء دي اتطلعت بمقارنة الملف القديم بنص البروتوكول وبالأدلة:

| # | Old claim | Problem | Evidence |
|---|---|---|---|
| 1 | ELISA panel = TNF-α, IL-6, ACPA | IL-1β omitted; protocol lists it | Protocol p.4–5 |
| 2 | N = 90 (10/group) | Protocol states n per group is **not specified** | Protocol p.3 |
| 3 | Safranin-O, EDTA, phospho-p38 "in protocol" | Not in protocol text; added by a derived note | Protocol p.4–5 |
| 4 | "CFA model is purely cell-mediated, no autoantibodies" | False: sera of AIA rats contain antibodies to chondrocyte antigen | Feige 1994, PMID 7948607 |
| 5 | Bougarne 2009 justifies not measuring PPAR-α/GR | Paper is cell + mouse + fenofibrate work; no PEA, no rat, no joint; predicts two-directional interaction | PMID 19376972 |
| 6 | NLR/SII "zero cost" | Needs EDTA whole blood + rodent-calibrated CBC; not in protocol; only rat-CFA precedent is negative | Alghulami 2024, PMID 38619760 |
| 7 | Cost figures (~250,000 / ~36,000 EGP) | No source | — |
| 8 | Section 6-و relies on NF-κB IHC while Tier A drops it | Internal contradiction | — |
| 9 | Novelty: 6 PubMed queries | Single database, no reproducible log | — |
| 10 | Knee histology accepted without question | AIA lesions are maximal in ankle/tarsus | Conway 1995, PMID 7629505; SMASH 2021 |

> [!warning] الملفات القديمة دي اتبنت على نفس الافتراضات، فمتعتمدش عليها في قرار التحاليل:
>
> [[Codex-Antigravity-Consensus-Lean-Budget-Verdict]]
>
> [[Main-Protocol-7-Groups]]

---

## 2. البروتوكول ملزمك بإيه بالحرف

البروتوكول بيحدد تسع مجموعات وتمن قياسات، ومش بيحدد عدد الحيوانات في كل مجموعة:

```
Groups (9): Negative control (paraffin oil) · CFA control · Prednisolone 10 · m-PEA 200 ·
            PEA/Pred 50/5 · 100/5 · 200/5 · Tacrolimus 1.8 · Baricitinib 10 (mg/kg, oral, D16–D45)
Endpoints (8): Serum ELISA: ACPA, TNF-α, IL-1β, IL-6
               Knee: histopathology; IHC NF-κB p65 nuclear; IHC TLR4
               Knee homogenate ELISA: p38 MAPK
```

أي حذف أو إضافة أو تغيير في مكان أخد العينة يعتبر تعديل على بروتوكول معتمد، ومحتاج موافقة المشرفين. كل التوصيات اللي جاية هنا اقتراحات بالأدلة، ومش قرارات نهائية.

---

## 3. المحكّم الدولي بيطلب إيه

### 3.1 معايير النشر (اتقرت كاملة)

| Standard | What it requires (relevant here) | Ref |
|---|---|---|
| ARRIVE 2.0 Essential 10 | Exact n/group + how n was decided; named primary outcome; randomisation method; who was blinded at each stage; effect sizes with CI | PMID 32663219 |
| BJP, Curtis 2018 | No statistics on groups n<5; equal groups; randomisation + blinded analysis; post hoc only after significant F; triage rejection if these are combined failures | PMID 29520785 |
| SMASH 2021 | Hind-paw ankle/tarsal joints; separate 0–3 scores (inflammation, erosion, cartilage); Safranin-O/toluidine blue for cartilage; EDTA decalcification for IHC; ≥2 sections/animal; blinded; sample-size calculation | PMID 33602797 |
| Bolon 2011 | Routine for all rodent arthritis studies: body weight, hind-paw swelling, BMD, hind-paw histology; AIA n = 6–8 randomised | PMID 21253435 |

> [!note] مجلة الصيدلة البريطانية طلعت تحديث لإرشاداتها سنة 2025، ولسه ما اتقراش. لو هتنشر فيها، لازم يتراجع قبل الإرسال:
> ```
> Curtis 2025, PMID 39865712
> ```

### 3.2 الأبحاث المنشورة بتقيس إيه فعلًا

اتراجع 59 بحث على نفس النموذج في الجرذان بين 2021 و2026، منهم 29 اتقروا كاملين. النسب اللي تحت من الأبحاث اللي اتقرت كاملة:

| Endpoint | Frequency (full text, n=29) |
|---|---|
| Clinical severity (score or paw) | **100%** |
| Paw volume/thickness | **93%** |
| ≥1 of TNF-α / IL-1β / IL-6 | **86%** |
| Joint histology (H&E) | 69% |
| Body weight | 69% |
| Arthritis score | 66% |
| CBC/haematology | 48% |
| NF-κB (any method) | 31% |
| Any oxidative-stress marker | 34% |
| Liver/kidney safety | 31% |
| ACPA | 7% |
| MAPK | 7% |
| TLR4 | 0% (1/59 overall) |
| Sample-size calculation reported | **0%** |
| Blinding reported | 28% |

متوسط عدد الحيوانات في المجموعة 8، وبيتراوح من 4 لـ18.

ولا بحث من دول حسب حجم العينة قبل التجربة، وأقل من التلت ذكروا التعمية. يعني لو التزمت بالمعايير اللي فوق، بحثك هيبقى أقوى من أغلب المنشور، ومن غير أي تكلفة.

> [!caution] حدود المسح ده
> ربع المجلة اللي اتنشر فيها كل بحث ما اتأكدش، لأن موقع التصنيف كان قافل الوصول. والأبحاث اتختارت يدويًا، مش بعينة عشوائية. النسب بتوصف الأبحاث اللي اتنشرت فعلًا، ومش بتضمن هيطلب إيه محكّم بعينه.

---

## 4. قرار كل تحليل

| Endpoint | In protocol? | Literature freq. | Validity in rat AIA | Recommendation |
|---|---|---|---|---|
| Arthritis score, paw volume/thickness, body weight (serial, D0–D45) | ❌ | 66–100% | Strong | **ADD — core, ~zero cost** |
| Histology H&E + Safranin-O, **ankle**, EDTA | Knee only | 69% | Strong for ankle (PMID 7629505) | **KEEP, move site to ankle** (approval) |
| Serum TNF-α, IL-1β, IL-6 | ✅ | 86% (≥1) | Strong (PMIDs 38334976, 34472749) | **KEEP** |
| NF-κB p65 nuclear IHC | ✅ | 31% | Moderate–strong (PMID 38334976) | **KEEP** — mechanistic link to PEA/GR question |
| Oxidative stress: MDA + GSH (± SOD, CAT) | ❌ (supervisor request) | 34% | Strong (PMIDs 36139795, 40439876) | **ADD — cheapest mechanistic block** |
| Serum ACPA | ✅ | 7% | Moderate; rat kit specificity unvalidated | Keep only if supervisor insists; first candidate to cut |
| TLR4 IHC | ✅ | ~2% | Moderate (PMID 32791152 — has 2026 erratum) | Secondary; cut before NF-κB if budget forces |
| p38 MAPK ELISA (total) | ✅ | 7% (all phospho) | Weak — field measures phospho-p38 | **Drop, or replace by p-p38 IHC on FFPE** (approval) |
| NLR/SII (CBC, EDTA blood) | ❌ | 48% CBC; NLR in AIA = 1 negative study | Weak | Exploratory only, if CBC is available |
| Glucose, ALT, creatinine (local kits) | ❌ | 31% | Inference: supports steroid-safety argument | Optional, cheap |

### ملاحظات على الجدول

**الكاحل بدل الركبة:** الالتهاب في النموذج ده بيبقى أشد ما يكون في الكاحل وعظام مشط القدم، وده المكان اللي إرشادات تقييم القطاعات النسيجية بتوصي بيه. الركبة هي المكان المعتاد في نموذج تاني مختلف، اسمه المختصر شبه اسم نموذجنا.

**محلول فك التكلس:** لازم يتحدد قبل ما البلوكات تتعمل، لأن الأحماض القوية بتبوّظ البروتينات اللي في النواة، وساعتها صبغة النواة مش هتنجح، والغلطة دي مش بتتصلح بعدين.
```
EDTA decalcification (SMASH Table 5)
```

**السيتوكينات في يوم 46:** يوم الذبح في البروتوكول متأخر عن كل الأبحاث اللي اتلقت، وكانت كلها بين اليوم 22 والـ40. احتمال إن مستوى السيتوكينات في السيرم يبقى واطي احتمال حقيقي، بس ما لقيناش مرجع يثبته. الحل اللي ببلاش: كل عينات التحليل الواحد تتعمل على طبق واحد، والمجموعات تتوزع بالتساوي على الأطباق.

**الأجسام المضادة دي:** فيه أبحاث قاستها في نفس النموذج، منها بحث مصري، لكن الكيتات المتاحة ما اتأكدش إنها بتقيس الجسم المضاد ده بالذات في الجرذان. لو اتقاست، لازم تسجل رقم الكتالوج وتكتب الحدود دي في المناقشة.
```
ACPA precedent: PMID 36139795 (Egypt), 38619760 · kit caveat: PMID 32895186
```

**إنزيم الإشارة:** كل الأبحاث بتقيس الصورة المفسفرة منه. الصورة الكلية بتتقاس بس علشان النتيجة تتنسب ليها، ومش بتتغير مع العلاج. والصورة المفسفرة مش هتستحمل النقل من غير سلسلة تبريد. لو المشرف مصمم على قياس منه، الأأمن إنه يتعمل بالصبغة على البلوكات، لأن التثبيت بالفورمالين بيحافظ عليه.
```
PMIDs 32497675, 23711830, 23897050, 29160881
```

**مؤشرات الدم المحسوبة:** مش ببلاش زي ما الملف القديم قال. محتاجة صورة دم كاملة على أنبوبة خاصة، وعلى جهاز معاير للجرذان. والبحث الوحيد على نفس النموذج لقى نتيجتها ضعيفة. لو هتتقاس، تتسجل من الأول إنها قياس استكشافي.

**مرجع لازم يتشال:** البحث ده عليه تحذيرين رسميين من المجلة سنة 2026، فمتستشهدش بيه:
```
D'Agostino 2007, PMID 17565008 — 2 Expressions of Concern (2026)
```
استعمل بداله:
```
Lo Verme 2005, Mol Pharmacol, PMID 15465922 (PPAR-α-null mice)
```

---

## 5. مؤشرات الإجهاد التأكسدي (طلب د. أحمد مراد)

دي أقوى نقطة في الرسالة من ناحية التنفيذ. كل المؤشرات دي بتتقاس بكيتات لونية على جهاز الطيف الضوئي العادي، من غير جهاز قراءة أطباق، وفيه أربع دراسات على نفس النموذج متفقة مع بعض، منها اتنين مصريين.

```
MDA (TBARS)  — 532 nm
GSH          — 412 nm
SOD          — ~560 nm
Catalase     — 240/510 nm
Nitrite (NO) — 540 nm (Griess)
TAC          — ~505 nm
```

**الأولوية حسب الميزانية:**
- الحد الأدنى: اتنين بس، لأنهم الاتنين الأكتر تكرارًا في الأبحاث.
```
MDA + GSH
```
- لو الميزانية تسمح:
```
+ SOD + CAT
```

**نوع العينة:** السيرم كفاية وأرخص، وده اللي عمله البحث المصري ده:
```
Shaaban 2022, PMID 36139795
```

**الثبات:** الكاتالاز والجلوتاثيون بيتأثروا بسرعة بالتجميد والتسييح. الأفضل يتعملوا فورًا في بورسعيد. الباقيين يستحملوا تجميد مرة واحدة.

**مهم:** الأرقام اللي فوق عن الطول الموجي وعن كتالوج الشركة المصرية معلومات تشغيلية، مش من أبحاث. راجعها على كتالوج الشركة نفسه.

---

## 6. التصميم والإحصاء

### 6.1 مشكلة غياب مجموعة بريدنيزولون 5 لوحدها

لو البريدنيزولون 5 لوحده بيدي نفس تأثير البريدنيزولون 10، يبقى تساوي الخليط مع 10 مش هيثبت أي حاجة. والتصميم الحالي ما يقدرش يستبعد الاحتمال ده.

**الحل من غير تكلفة إضافية** (محتاج موافقة المشرف):
```
Replace PEA/Pred 100/5  →  Prednisolone 5 alone
```
كده يبقى عندك مقارنة مباشرة بين الخليط والبريدنيزولون 5، ويفضل عندك نقطتين لجرعة الدوا الطبيعي.

ولو التبديل اترفض، المقارنة بين الخليط والبريدنيزولون 10 تتعرض كتقدير بفترة ثقة، وتتوصف إنها استكشافية، ومتتوصفش أبدًا إنهم "متساويين".

### 6.2 عدد الحيوانات

| Method | Result | Usable? |
|---|---|---|
| Mead resource equation (k=9) | n = 3/group | ❌ violates BJP n≥5 |
| Power, combo vs CFA (d≈2.5) | 5–6/group | ✅ |
| Power, weaker arms (d≈1–1.5) | 8–10 → 25–75% power | Partial |
| Combo superior to Pred 10 (realistic SD) | 20–27/group | ❌ not affordable |
| Non-inferiority vs Pred 10 (realistic SD, 50% margin) | 31/group | ❌ |

**الاقتراح:**
- 8 حيوانات مريضة فعلًا في كل مجموعة، يعني 72.
- اعمل الالتهاب في عدد زيادة شوية، وفي اليوم 15 وزّع على المجموعات بس الحيوانات اللي الالتهاب ظهر فيها، بشرط يتحدد مقدمًا.
- القياسات السريرية تتعمل على كل الحيوانات. التحاليل الغالية تتعمل على 6 في كل مجموعة، يتختاروا عشوائيًا قبل ما الأكواد تتفك. كده يبقوا 54 عينة بس.
- مصادر حساب حجم التأثير:
```
Morvaridi 2025 (PMID 40099241) · Slovák 2017 (PMID 29113115)
```
- أرقام الدراسة الاستطلاعية بتاعتك لازم تحل محل أرقام الأبحاث دي قبل ما العدد يتحسم.

### 6.3 القياس الأساسي والمقارنات المحددة مقدمًا

**القياس الأساسي:** حجم الالتهاب الكلي على مدار فترة العلاج، يعني المساحة تحت منحنى درجة الالتهاب، مع حساب درجة اليوم 15 لكل حيوان.
```
Primary: AUC of arthritis score D16–D45, ANCOVA adjusted for D15 score
Alternative: AUC of contralateral paw volume (choose by pilot variance)
```

**المقارنات الأساسية (تصحيح بطريقة هولم على التلاتة):**
```
C1  Pred 10        vs CFA control   (assay sensitivity)
C2  PEA/Pred 200/5 vs CFA control   (combination efficacy)
C3  PEA/Pred 200/5 vs Pred 10       (sparing — estimate + 95% CI)
C4  Dose trend 50/5 → 100/5 → 200/5 (secondary)
```
باقي المقارنات تتعمل ضد مجموعة الالتهاب من غير علاج. ومتعملش المقارنات الـ36 كلها ببعض.

### 6.4 التحليل

**القياسات المتكررة:**
```
AUC + ANCOVA (Matthews 1990, PMID 2106931); mixed model as sensitivity
```

**درجات القطاعات النسيجية:**
```
Kruskal–Wallis → Dunn–Holm (planned pairs) or ordinal regression
```
- قارئ تاني من غير ما يعرف المجموعات يقرا 20% من الشرايح.

**وحدة التحليل هي الحيوان:** الحقول المجهرية والتكرار في نفس الطبق بيتعمل لهم متوسط ويطلعوا رقم واحد للحيوان.

### 6.5 التوزيع العشوائي والتعمية (ببلاش)

1. حد مش بيدّي الدوا ومش بيقيس هو اللي يعمل جدول التوزيع العشوائي، ويحتفظ بالمفتاح.
2. في اليوم 15 الحيوانات تترتب حسب درجة الالتهاب، وتتوزع في مجموعات من 8.
3. الأدوية تتحضر في أنابيب مكتوب عليها حروف بس.
4. اللي بيقيس الرجل والدرجة ميعرفش المجموعات.
5. العينات اللي رايحة القاهرة أو طنطا تاخد كود عشوائي تاني.
6. المجموعات تتوزع على الأقفاص وأطباق التحاليل ودفعات الصبغة.
7. خطة التحليل تتكتب في صفحة واحدة بتاريخ قبل اليوم صفر، وتترفع على الموقع المجاني ده:
```
OSF preregistration (free)
```

---

## 7. الجدة العلمية — بحدود

اتبحث يوم 2 أكتوبر 2026 في القواعد دي:
```
PubMed · Europe PMC (full text + preprints) · OpenAlex · Semantic Scholar (partial) · ClinicalTrials.gov · Crossref · citation chasing
```
طلع حوالي 1180 نتيجة، فضل منهم حوالي 390 بعد حذف المكرر، واتقرا ملخص حوالي 45 منهم.

**القاعدتين المدفوعتين لسه ما اتبحثش فيهم.** نص الاستعلامات جاهز في القسم الخامس من الملف ده، شغّله من بنك المعرفة المصري:
[[evidence-2026-10-02/C-novelty#5. Query strings for manual Scopus and Web of Science runs (via EKB)]]

### 7.1 الادعاءات اللي تقدر تقولها (لازم تذكر القواعد والتاريخ)

```
Within the databases and queries listed (searched 2 October 2026), no previous study was identified that:
 (1) combined PEA, in any formulation, with a systemic glucocorticoid in an experimental arthritis model;
 (2) tested whether PEA allows the prednisolone dose to be reduced while preserving anti-arthritic efficacy;
 (3) compared PEA head-to-head with a JAK inhibitor (baricitinib) or a calcineurin inhibitor (tacrolimus) in any model.
```

### 7.2 الادعاءات اللي متقولهاش

```
✗ "First study to combine PEA with a corticosteroid"       → Noli 2019 (PMID 31237065, cats, methylprednisolone taper)
✗ "First PEA study in CFA rats"                             → Bartolucci 2018 (PMID 30121836, m-PEA, CFA-TMJ)
✗ "First PEA study in arthritis"                            → Impellizzeri 2013 (PMID 24246048, CIA mice)
✗ "First PPAR-based glucocorticoid-sparing approach in AIA" → Ashour 2019 (PMID 30074417, gemfibrozil, Egypt)
✗ "First natural-product steroid-sparing strategy in AIA"   → Morvaridi 2025, Barbosa Retameiro 2025, Du 2016
✗ "First endocannabinoid modulator + glucocorticoid"        → Nass 2021 (PMID 34042520)
✗ "PEA never tested in RA patients"                         → Parisi 2021 (PMID 34056884)
```

### 7.3 أبحاث لازم تتذكر في المناقشة

```
Impellizzeri 2013 · Bartolucci 2018 · Bonezzi 2016 · Lowin 2015 · Noli 2019 · Parisi 2021 ·
Ashour 2019 · Barbosa Retameiro 2025 · Morvaridi 2025 · Du 2016 · Nass 2021 · NCT07680101
```

أهمهم البحث المصري ده. استعمل منشّط لنفس المستقبل اللي الدوا الطبيعي بيشتغل عليه، مع جرعة بريدنيزولون أقل، في نفس النموذج:
```
Ashour 2019, PMID 30074417
```
المحكّم غالبًا هيسأل: إيه الجديد عن البحث ده؟ والإجابة اللي ليها أساس: الدوا الطبيعي ده بالذات، ومقارنته وجهًا لوجه بالدواين المرجعيين، وتصميم الجرعات المتدرجة.

**وصف بحث القطط:** الدوا ده اتدّى أثناء تقليل جرعة الكورتيزون وبعد ما وقف، علشان يأخر رجوع المرض. يعني مش مقارنة بتقلل الجرعة، ومينفعش يتوصف بالطريقة دي.

---

## 8. قرارات محتاجة المشرف قبل اليوم صفر

| # | Decision | Recommendation | Cost |
|---|---|---|---|
| 1 | Histology site | **Decided 2026-10-02: knee kept (supervisor request)** — justify knee in Methods; cite ankle literature as limitation | ~0 |
| 2 | Decalcification | EDTA, written in protocol | ~0 |
| 3 | Add clinical measures | Score + paw + body weight, serial | ~0 |
| 4 | Add oxidative stress | MDA + GSH (± SOD, CAT), serum | Low (local kits) |
| 5 | Pred-5-alone arm | Replace 100/5 arm | 0 added |
| 6 | n per group | 8 evaluable; assays on random 6 | Saves assays |
| 7 | p38 MAPK | Drop, or p-p38 IHC on FFPE | Saves money |
| 8 | ACPA / TLR4 | Keep or cut — supervisor's call | Saves money if cut |
| 9 | Primary outcome + analysis plan | Written + dated before D0 | 0 |

---

## 9. حدود الشغل ده

1. ربع المجلات ما اتأكدش.
2. القاعدتين المدفوعتين لسه ما اتبحثش فيهم.
3. قاعدة واحدة من المجانية رفضت معظم الاستعلامات.
4. بحث الكاحل الأصلي القديم نسخة ممسوحة ضوئيًا، ومنقولش منه بالحرف.
5. البحث المصري اللي قاس المستقبل المناعي بالصبغة في الكاحل عليه تصحيح سنة 2026، ولازم يتقرا قبل ما تعتمد عليه.
6. طريقة إعطاء الدوا في بحث المفصل الفكي ما اتأكدتش من ملخصه.
7. مفيش أي رقم تكلفة في الملف ده، لأن الأسعار لازم تيجي من عرض سعر فعلي من المعمل.

---

## 10. أهم المراجع (كلها اتأكدت يوم 2026-10-02)

```
Standards
  Percie du Sert 2020, PLoS Biol — ARRIVE 2.0 ............................ PMID 32663219
  Curtis 2018, Br J Pharmacol — design & analysis II ..................... PMID 29520785
  Hayer 2021, Ann Rheum Dis — SMASH ...................................... PMID 33602797
  Bolon 2011, J Biomed Biotechnol — rodent arthritis methods ............. PMID 21253435
Model / endpoints
  Conway 1995, J Exp Med — ankle/metatarsal lesions in AIA ............... PMID 7629505
  Feige 1994, Autoimmunity — antibodies in AIA rats ...................... PMID 7948607
  Wu 2024, J Pharm Pharmacol — serum+synovial cytokines, nuclear p65 ..... PMID 38334976
  El-Shiekh 2021, J Ethnopharmacol — Egypt, D16–D40 window ............... PMID 33418032
  Shaaban 2022, Antioxidants — Egypt, ACPA + serum oxidative panel ....... PMID 36139795
  Anwar 2025, Inflammopharmacology — oxidative stress, paw caliper ....... PMID 40439876
  Alghulami 2024, Inflammopharmacology — NLR in CFA rats (weak) .......... PMID 38619760
  Gowayed 2020, Life Sci — TLR4 IHC, AIA (erratum 2026) .................. PMID 32791152
Mechanism
  Lo Verme 2005, Mol Pharmacol — PEA acts via PPAR-α ..................... PMID 15465922
  Bougarne 2009, PNAS — PPARα–GRα crosstalk (cells/mice) ................. PMID 19376972
Novelty precedents
  Impellizzeri 2013 PMID 24246048 · Bartolucci 2018 PMID 30121836 · Noli 2019 PMID 31237065
  Ashour 2019 PMID 30074417 · Barbosa Retameiro 2025 PMID 41370192 · Morvaridi 2025 PMID 40099241
  Du 2016 PMID 26773773 · Nass 2021 PMID 34042520 · Parisi 2021 PMID 34056884
Statistics
  Arifin 2017 PMID 29386977 · Matthews 1990 PMID 2106931 · Slovák 2017 PMID 29113115
```

---

## روابط
- البروتوكول الأصلي:
```
00-Sources/protocol/Protocol.pdf
```
- ملفات الأدلة:

[[evidence-2026-10-02/A-endpoints-survey]]

[[evidence-2026-10-02/B-endpoint-validity]]

[[evidence-2026-10-02/C-novelty]]

[[evidence-2026-10-02/D-stats]]

- خريطة القسم:

[[06-MOC-Thesis-Defense-and-Publishing]]
