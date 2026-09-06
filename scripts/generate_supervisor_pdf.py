import os
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

HTML_CONTENT = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<title>خطة التحاليل المعملية وإثبات الجدة العلمية — رسالة الماجستير</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  @page {
    size: A4;
    margin: 10mm 12mm 10mm 12mm;
    @bottom-left {
      content: "كلية الصيدلة — جامعة بورسعيد | قسم الأدوية والسموم";
      font-family: 'Cairo', sans-serif;
      font-size: 7.5pt;
      color: #718096;
    }
    @bottom-right {
      content: "صفحة " counter(page) " من " counter(pages);
      font-family: 'Cairo', sans-serif;
      font-size: 7.5pt;
      color: #718096;
    }
  }

  *, *:before, *:after {
    box-sizing: border-box;
  }

  body {
    font-family: 'Cairo', 'Segoe UI', Tahoma, sans-serif;
    font-size: 8.8pt;
    line-height: 1.45;
    color: #2D3748;
    background-color: #FFFFFF;
    margin: 0;
    padding: 0;
  }

  .en {
    font-family: 'Inter', sans-serif;
    direction: ltr;
    display: inline-block;
  }

  /* Academic Header */
  .header-container {
    border-bottom: 2px solid #1A365D;
    padding-bottom: 8px;
    margin-bottom: 10px;
  }

  .header-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 6px;
  }

  .univ-meta {
    font-size: 8.8pt;
    font-weight: 700;
    color: #1A365D;
    line-height: 1.25;
  }

  .univ-meta span {
    display: block;
    color: #4A5568;
    font-weight: 600;
    font-size: 8pt;
  }

  .doc-badge {
    background: #EBF8FF;
    color: #2B6CB0;
    border: 1px solid #BEE3F8;
    padding: 3px 8px;
    border-radius: 5px;
    font-size: 8pt;
    font-weight: 700;
    text-align: center;
  }

  h1.doc-title {
    font-size: 13.5pt;
    font-weight: 900;
    color: #1A365D;
    margin: 0 0 2px 0;
    line-height: 1.2;
  }

  .doc-subtitle {
    font-size: 9pt;
    color: #2B6CB0;
    font-weight: 700;
    margin: 0 0 8px 0;
  }

  .meta-grid {
    display: grid;
    grid-template-columns: 1.2fr 1.8fr;
    gap: 8px;
    background: #F7FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 6px;
    padding: 8px 12px;
    font-size: 8.2pt;
  }

  .meta-col p {
    margin: 1.5px 0;
  }

  .meta-label {
    font-weight: 800;
    color: #1A365D;
  }

  /* Headings */
  h2.section-title {
    font-size: 10.5pt;
    font-weight: 800;
    color: #1A365D;
    border-right: 3.5px solid #2B6CB0;
    padding-right: 7px;
    margin: 10px 0 6px 0;
    display: flex;
    align-items: center;
    page-break-after: avoid;
  }

  h3.subsection-title {
    font-size: 9pt;
    font-weight: 700;
    color: #1A365D;
    margin: 6px 0 3px 0;
    page-break-after: avoid;
  }

  /* Content Cards */
  .card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 6px;
    padding: 7px 10px;
    margin-bottom: 8px;
    page-break-inside: avoid;
  }

  .card-highlight {
    border-right: 3px solid #2B6CB0;
    background: #F8FAFC;
  }

  /* Tables */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 6px 0 8px 0;
    font-size: 8pt;
    page-break-inside: avoid;
  }

  th {
    background-color: #1A365D;
    color: #FFFFFF;
    font-weight: 700;
    text-align: right;
    padding: 5px 7px;
    border: 1px solid #1A365D;
  }

  td {
    padding: 4px 7px;
    border: 1px solid #E2E8F0;
    vertical-align: middle;
  }

  tr:nth-child(even) {
    background-color: #F8FAFC;
  }

  .tag-mandatory {
    background: #C6F6D5;
    color: #22543D;
    font-weight: 700;
    padding: 1.5px 5px;
    border-radius: 4px;
    font-size: 7.2pt;
    display: inline-block;
  }

  .tag-recommended {
    background: #EBF8FF;
    color: #2A4365;
    font-weight: 700;
    padding: 1.5px 5px;
    border-radius: 4px;
    font-size: 7.2pt;
    display: inline-block;
  }

  .tag-excluded {
    background: #FED7D7;
    color: #742A2A;
    font-weight: 700;
    padding: 1.5px 5px;
    border-radius: 4px;
    font-size: 7.2pt;
    display: inline-block;
  }

  /* Callout Boxes */
  .callout {
    border-radius: 6px;
    padding: 6px 10px;
    margin: 6px 0;
    font-size: 8.2pt;
    page-break-inside: avoid;
  }

  .callout-info {
    background-color: #EBF8FF;
    border-right: 3px solid #3182CE;
    color: #2A4365;
  }

  .callout-warning {
    background-color: #FFFAF0;
    border-right: 3px solid #DD6B20;
    color: #7B341E;
  }

  .callout-title {
    font-weight: 800;
    margin-bottom: 2px;
  }

  /* Lists */
  ul, ol {
    margin: 3px 0;
    padding-right: 18px;
  }

  li {
    margin-bottom: 2px;
  }

  .page-break {
    page-break-before: always;
  }

  .sig-section {
    margin-top: 14px;
    border-top: 1.2px dashed #CBD5E0;
    padding-top: 10px;
    page-break-inside: avoid;
  }

  .sig-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
    font-size: 8.5pt;
  }
</style>
</head>
<body>

  <!-- ==================== PAGE 1 ==================== -->
  <div class="header-container">
    <div class="header-top">
      <div class="univ-meta">
        جامعة بورسعيد — كلية الصيدلة
        <span>قسم الأدوية والسموم</span>
      </div>
      <div class="doc-badge">
        وثيقة أكاديمية معتمدة للتنفيذ المعملي<br>
        <span style="font-size: 7pt; font-weight: 600;">سبتمبر 2026</span>
      </div>
    </div>
    
    <h1 class="doc-title">تقرير وخطة استكمال التحاليل المعملية وإثبات الجدة العلمية</h1>
    <div class="doc-subtitle">
      مشروع رسالة الماجستير: استهداف التهاب المفاصل التجريبي في الجرذان بواسطة مركبات طبيعية مختارة كعوامل موفرة للكورتيزون
    </div>

    <div class="meta-grid">
      <div class="meta-col">
        <p><span class="meta-label">الباحث:</span> المعيد / رفعت إبراهيم رفعت</p>
        <p><span class="meta-label">الدرجة:</span> ماجستير في العلوم الصيدلية (أدوية وسموم)</p>
        <p><span class="meta-label">النموذج:</span> <span class="en">CFA-Induced Polyarthritis in Female Wistar Rats</span></p>
      </div>
      <div class="meta-col">
        <p><span class="meta-label">السادة الأساتذة المشرفون:</span></p>
        <p>• <strong>أ.د.م / أحمد أبو الفتوح السيد مراد</strong> (رئيس القسم وأستاذ م. الأدوية والسموم)</p>
        <p>• <strong>أ.د.م / أحمد جعفر أحمد</strong> (أستاذ م. الأدوية والسموم)</p>
        <p>• <strong>أ.د.م / أحمد سعد سعد</strong> (أستاذ م. الأدوية والسموم)</p>
      </div>
    </div>
  </div>

  <!-- Section 1 -->
  <h2 class="section-title">1. الخلاصة التنفيذية والجدة العلمية للبحث (Novelty Framework)</h2>
  
  <div class="card card-highlight" style="margin-bottom: 6px;">
    <p style="margin: 0 0 4px 0;">
      يقدم هذا البحث أول دراسة مقارنة تبحث في القدرة التوفيرية للستيرويد <span class="en">(Glucocorticoid-Sparing Potential)</span> لمركب <strong>الـ Palmitoylethanolamide (PEA)</strong> بنصف الجرعة الاعتيادية من البريدنيزولون في نموذج CFA، ووضعه في مقارنة مباشرة وجهاً لوجه <span class="en">(Head-to-Head)</span> مع أحدث خطوط العلاج التخليقية الموجهة ومثبطات المناعة المستخدمة إكلينيكياً:
    </p>
    <ul>
      <li><strong>عقار Baricitinib:</strong> كنموذج لمثبطات الـ JAK التخليقية الموجهة <span class="en">(Targeted synthetic DMARD / JAK1/JAK2 inhibitor)</span>.</li>
      <li><strong>عقار Tacrolimus:</strong> كنموذج لمثبطات الكالسينيورين القوية <span class="en">(Potent Calcineurin Inhibitor)</span>.</li>
    </ul>
  </div>

  <div class="callout callout-info" style="margin-bottom: 10px;">
    <div class="callout-title">📌 التوثيق العلمي في قواعد البيانات الدولية (PubMed & Europe PMC — سبتمبر 2026):</div>
    أكد المسح الشامل للأدبيات الطبية خلو قواعد البيانات العالمية من أي دراسة سابقة جمعت بين PEA وبريدنيزولون منخفض الجرعة في نموذج CFA، أو قارنت PEA وجهاً لوجه مع Baricitinib أو Tacrolimus. تمنح هذه المقارنة البحث <strong>جدة ثلاثية (تركيبية، ومقارنة، وسريرية تحويلية)</strong> تؤهله للنشر الدولي في مجلات الفئة الأولى (Q1).
  </div>

  <!-- Section 2 -->
  <h2 class="section-title">2. مصفوفة التحاليل المعملية المعتمدة (Definitive Assay Matrix)</h2>
  <p style="margin: 0 0 4px 0; font-size: 8.2pt; color: #4A5568;">
    حزمة متكاملة تغطي كافة المستويات البيولوجية (المظهري، والدموي، والمناعي، والنسيجي، والجزيئي) بأعلى درجات ثبات العينات ومعايير النشر:
  </p>

  <table>
    <thead>
      <tr>
        <th style="width: 25%;">المستوى والتحليل</th>
        <th style="width: 19%;">نوع العينة</th>
        <th style="width: 42%;">القيمة البيولوجية والدلالة للنشر الدولي</th>
        <th style="width: 14%;">الأولوية</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>H&E Histopathology</strong><br><span style="font-size: 7.2pt; color: #718096;">مع تقييم مُعمّى Blinded Score</span></td>
        <td>مفاصل الركبة (برافين FFPE)</td>
        <td>إثبات سلامة عمارة المفصل، ومنع تآكل العظام والغضروف، وكبح ارتشاح الخلايا الالتهابية وتضخم الغشاء الزليلي.</td>
        <td><span class="tag-mandatory">أساس إلزامي</span></td>
      </tr>
      <tr>
        <td><strong>NF-κB p65 (IHC)</strong><br><span style="font-size: 7.2pt; color: #718096;">صبغة مناعية كيميائية</span></td>
        <td>قطاعات برافين FFPE</td>
        <td>إثبات الآلية الجزيئية الأساسية لتنشيط PPAR-α؛ حيث يقيس كبح انتقال العامل للأنوية <span class="en">(Nuclear Translocation)</span> بدقة مكانية في النسيج.</td>
        <td><span class="tag-mandatory">أساس إلزامي</span></td>
      </tr>
      <tr>
        <td><strong>Serum Cytokines ELISA</strong><br><span class="en" style="font-size: 7.5pt;">TNF-α, IL-6, ACPA</span></td>
        <td>سيروم مجمد <span class="en">(-20°C)</span></td>
        <td>تأكيد كبح العاصفة السيتوكينية الجهازية وإثبات خفض الأجسام المضادة النوعية للمناعة الذاتية الروماتيزمية.</td>
        <td><span class="tag-mandatory">أساس إلزامي</span></td>
      </tr>
      <tr>
        <td><strong>Safranin-O / Fast Green</strong><br><span style="font-size: 7.2pt; color: #718096;">صبغة نوعية للغضروف</span></td>
        <td>نفس بلوكات البرافين</td>
        <td>صبغة كيميائية نسيجية عالية التباين تكشف بدقة سلامة محتوى البروتيوغليكان <span class="en">(Proteoglycans)</span> في الغضروف المفصلي مقارنة بالـ CFA.</td>
        <td><span class="tag-recommended">إضافة ممتازة</span></td>
      </tr>
      <tr>
        <td><strong>Metabolic Safety Profile</strong><br><span style="font-size: 7.2pt; color: #718096;">سكر، دهون، كبد (ALT/AST)</span></td>
        <td>سيروم مجمد</td>
        <td><strong>البرهان التطبيقي للتوفير الستيرويدي:</strong> إثبات أن خفض جرعة الكورتيزون مع PEA جنب الحيوان الاضطرابات الأيضية الناتجة عن الجرعة العالية.</td>
        <td><span class="tag-recommended">إضافة سريرية</span></td>
      </tr>
      <tr>
        <td><strong>Redox Status (MDA + GSH)</strong><br><span style="font-size: 7.2pt; color: #718096;">مؤشرات الإجهاد التأكسدي</span></td>
        <td>سيروم</td>
        <td>تأكيد استعادة التوازن التأكسدي والخلوي وحماية الأنسجة من أكسدة الدهون بكيتات قياس طيفية قياسية متوفرة محلياً.</td>
        <td><span class="tag-recommended">تكميلي اقتصادي</span></td>
      </tr>
      <tr>
        <td><strong>Cleaved Caspase-3 IHC</strong><br><span style="font-size: 7.2pt; color: #718096;">صبغة مناعية للموت المبرمج</span></td>
        <td>نفس بلوكات البرافين</td>
        <td>تقييم الموت الخلوي المبرمج <span class="en">(Apoptosis)</span> في خلايا الغشاء الزليلي، وتُنفذ في حال رغبة لجنة الإشراف في إضافة ماركر مكمل.</td>
        <td><span class="tag-recommended" style="background:#ED8936; color:#fff;">مشروط باللجنة</span></td>
      </tr>
    </tbody>
  </table>

  <!-- ==================== PAGE 2 ==================== -->
  <div class="page-break"></div>

  <!-- Section 3 -->
  <h2 class="section-title">3. التحاليل المستبعدة والمبررات العلمية والتقنية (Technical Feasibility & Cost-Benefit)</h2>
  
  <p style="margin: 0 0 4px 0; font-size: 8.2pt; color: #4A5568;">
    بناءً على المراجعة الفنية لظروف حفظ العينات وطبيعة نسيج المفاصل المتكلسة، نوصي باستبعاد المسارات التالية لتفادي مخاطر التلف المعملي والهدر المالي:
  </p>

  <table>
    <thead>
      <tr>
        <th style="width: 25%;">التحليل المستبعد</th>
        <th style="width: 22%;">المتطلبات الفنية الحرجة</th>
        <th style="width: 41%;">المبرر العلمي والتقني للاستبعاد</th>
        <th style="width: 12%;">القرار</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>DUSP1 mRNA</strong><br><span style="font-size: 7.2pt; color: #718096;">بواسطة RT-qPCR</span></td>
        <td>تجميد فوري بنيتروجين سائل (-196°C) وسحق العظام المتكلسة مجمدة</td>
        <td>عزل الـ RNA من نسيج عظمي منزوع التكلس معرض بدرجة عالية للتكسر <span class="en">(Degradation)</span> أثناء النقل؛ علاوة على أن DUSP1 ليس مساراً سببياً مثبتاً لـ PEA بل مجرد ناتج استجابة متأخر.</td>
        <td><span class="tag-excluded">استبعاد مبرر</span></td>
      </tr>
      <tr>
        <td><strong>Phospho-p38 MAPK</strong><br><span style="font-size: 7.2pt; color: #718096;">بواسطة الـ ELISA</span></td>
        <td>حفظ الفسفرة بمثبطات فوسفاتيز وسلسلة تبريد فائقة مستمرة</td>
        <td>الفسفرة سريعة التلاشي وتتأثر بالنقل؛ كما أن الكيتات التجارية العالمية المعتمدة موثقة للإنسان والفأر وليست متحققة للجرذ، وتتطلب تكلفة استيرادية باهظة دون عائد يقيني.</td>
        <td><span class="tag-excluded">استبعاد مبرر</span></td>
      </tr>
    </tbody>
  </table>

  <div class="callout callout-warning" style="margin-bottom: 8px;">
    <div class="callout-title">💡 الرؤية المنهجية البديلة الأكثر ثباتاً ومصداقية:</div>
    الاعتماد على <strong>بلوكات البرافين (FFPE)</strong> لقياس الهستوباثولوجي وصبغة <strong>NF-κB p65 IHC</strong> يعطي دلالة مكانية <span class="en">(Spatial Localization)</span> تفوق متجانس الأنسجة، وتتميز بثبات فيزيائي تام لا يتأثر بالحرارة أو النقل، مما يضمن قبول النتائج دولياً بأعلى موثوقية.
  </div>

  <!-- Section 4 -->
  <h2 class="section-title">4. تكامل نتائج التجربة الاستطلاعية (Pilot Study Integration)</h2>
  
  <div class="card" style="margin-bottom: 8px;">
    <p style="margin: 0 0 4px 0;"><strong>أثمرت التجربة الاستطلاعية عن مؤشرات دقيقة وفرت الأساس المنهجي لاعتماد جرعات الدراسة الرئيسية:</strong></p>
    <ul style="font-size: 8.2pt;">
      <li><strong>إثبات نجاح النموذج جهازيّاً:</strong> قفز العدد الإجمالي لكرات الدم البيضاء (TLC) بنسبة <strong>+77.6%</strong> (من 10.25 إلى 18.20 × 10³/µL) وتضاعفت اللمفاويات، وارتفع الـ ESR (+866%) والـ CRP (9 أضعاف)، مما يثبت إحداث التهاب روماتيزمي جهازي حقيقي.</li>
      <li><strong>البصمة الحركية للستيرويد (Demargination):</strong> أظهرت التوليفات انقلاب النسبة نحو سيادة العدلات وهبوط اللمفاويات، وهو التوقيع الفسيولوجي الكلاسيكي الذي يؤكد الامتصاص الحيوي للبريدنيزولون بجرعته المنخفضة (5 مجم/كجم).</li>
      <li><strong>التبرير المنهجي للجرعات:</strong> ثبات جرعة الكورتيزون (5 مجم) مع التراجع المتدرج لـ TLC والـ CRP والسيتوكينات فقط عند رفع PEA إلى 100 و 200 مجم برر اعتماد هاتين الجرعتين للدراسة الكبرى الموسعة.</li>
    </ul>
  </div>

  <!-- Section 5 -->
  <h2 class="section-title">5. خطة التنفيذ الميدانية المباشرة (Immediate Execution Roadmap)</h2>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 6px;">
    <div class="card" style="margin-bottom: 0;">
      <h3 class="subsection-title">المرحلة الأولى: العينات النسيجية</h3>
      <ul style="font-size: 8pt;">
        <li>حصر وتجهيز بلوكات البرافين (FFPE) لمفاصل الركبة لجميع المجموعات (N=90).</li>
        <li>التعاقد مع معمل باثولوجي لعمل صباغة H&E مع كروت تقييم مُعمّاة <span class="en">(Blinded Scoring)</span> بواسطة أستاذ باثولوجي مستقل.</li>
        <li>صبغ شرائح Safranin-O لتقييم الغضروف المفصلي.</li>
        <li>إجراء صباغة NF-κB p65 بالـ IHC وقياس الانتقال النووي.</li>
      </ul>
    </div>

    <div class="card" style="margin-bottom: 0;">
      <h3 class="subsection-title">المرحلة الثانية: التحاليل الكيميائية والسيروم</h3>
      <ul style="font-size: 8pt;">
        <li>استكمال كيتات السيروم الناقصة للـ ELISA (السيتوكينات والأجسام المضادة ACPA).</li>
        <li>تشغيل كيتات الإجهاد التأكسدي (MDA و GSH) والبروفايل الأيضي (السكر، والدهون، وإنزيمات الكبد).</li>
        <li>إجراء التحليل الإحصائي الكامل (ANOVA متبوعاً بـ Tukey's post-hoc) وحساب مؤشرات الـ NLR الفردية.</li>
        <li>صياغة مسودة البحث للنشر في إحدى مجلات الـ Q1 المرموقة.</li>
      </ul>
    </div>
  </div>

  <!-- Signatures -->
  <div class="sig-section">
    <div class="sig-grid">
      <div>
        <p style="margin: 0;"><strong>مقدمه لسيادتكم:</strong></p>
        <p style="margin: 18px 0 0 0;">المعيد / رفعت إبراهيم رفعت<br><span style="font-size: 7.5pt; color: #718096;">قسم الأدوية والسموم — كلية الصيدلة</span></p>
      </div>
      <div>
        <p style="margin: 0; text-align: left;"><strong>اعتماد السادة الأساتذة المشرفين:</strong></p>
        <p style="margin: 18px 0 0 0; text-align: left;">
          ............................................................<br>
          <span style="font-size: 7.5pt; color: #718096;">لجنة الإشراف على رسالة الماجستير</span>
        </p>
      </div>
    </div>
  </div>

</body>
</html>
"""

def generate_pdf():
    output_dir = Path(r"D:\vault\my research\06 - Thesis Defense & Publishing")
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_path = output_dir / "Refaat-What-to-Assay-and-Novelty-Supervisor-Report.pdf"
    
    html_path = output_dir / "temp_supervisor_report.html"
    html_path.write_text(HTML_CONTENT, encoding="utf-8")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(html_path.as_uri(), wait_until="networkidle")
        page.pdf(
            path=str(pdf_path),
            format="A4",
            print_background=True,
            margin={"top": "10mm", "bottom": "10mm", "left": "10mm", "right": "10mm"}
        )
        browser.close()

    print(f"Successfully generated 2-page PDF: {pdf_path}")
    print(f"PDF size: {pdf_path.stat().st_size} bytes")

    if html_path.exists():
        html_path.unlink()

if __name__ == "__main__":
    generate_pdf()
