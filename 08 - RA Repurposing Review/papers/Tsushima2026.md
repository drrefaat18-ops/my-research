# Risk of urinary tract infection with SGLT2 inhibitor initiation in patients with immune‐mediated inflammatory diseases and type 2 diabetes: A target trial emulation using a Japanese hospital‐based claims database

**Authors:** Tsushima Hiroshi, Yajima Nobuyuki, Nomiyama Takashi, Sakai Ryoko, Noma Hisashi, Katagiri Akira, Tamura Naoto  
**Journal:** Journal of Diabetes Investigation (2026)  
**DOI:** 10.1111/jdi.70343  
**PDF:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13398639/


## Abstract


### ABSTRACT


#### Aims/Introduction

To evaluate whether sodium‐glucose cotransporter 2 inhibitor (SGLT2i) initiation is associated with the risk of urinary tract infection (UTI), with upper UTI and genital infection assessed as secondary outcomes, compared with metformin in patients with immune‐mediated inflammatory diseases (IMIDs) and type 2 diabetes.


#### Materials and Methods

We conducted a target trial emulation using an active‐comparator, new‐user design with a Japanese hospital‐based claims database from 2014 to 2024. Adults with IMIDs and type 2 diabetes who newly initiated an SGLT2i or metformin were included. The primary outcome was UTI; secondary outcomes were upper UTI and genital infection. Hazard ratios (HRs) were estimated using inverse probability of treatment weighting and weighted Cox proportional hazards models. Prespecified subgroup and interaction analyses further evaluated heterogeneity in UTI risk according to concomitant immunosuppressive therapies.


#### Results

We analyzed 1,845 SGLT2i initiators and 1,499 metformin initiators (mean age 71.8 years; 55.4% female). Compared with metformin initiation, SGLT2i initiation was not associated with increased risks of UTI (HR 1.14, 95% confidence interval [CI] 0.84–1.55) or upper UTI (HR 1.28, 95% CI 0.71–2.31). Results for UTI were broadly similar across categories of concomitant immunosuppressive therapies, and interaction analyses showed no evidence of effect modification across these strata, including glucocorticoid dose. The risk of genital infection was higher with SGLT2i initiation (HR 2.31, 95% CI 1.16–4.63).


#### Conclusions

Among patients with IMIDs and type 2 diabetes, SGLT2i initiation was not associated with increased risks of UTI or upper UTI compared with metformin, although the risk of genital infection was higher.


## INTRODUCTION

Inflammatory rheumatic and musculoskeletal diseases are frequently complicated by cardiometabolic comorbidities, including type 2 diabetes (T2D). In rheumatology care, glycemic management is challenging because systemic inflammation and glucocorticoids can worsen insulin resistance and precipitate hyperglycemia 1 , 2 . Given the excess cardiovascular and renal morbidity in these conditions, systematic management of modifiable risk factors, including glycemic control, is recommended 3 .

Sodium‐glucose cotransporter 2 inhibitors (SGLT2is) lower blood glucose by inhibiting glucose reabsorption from the tubular lumen 4 . Randomized controlled trials have established their efficacy and safety in T2D 5 , 6 , 7 , 8 , 9 , 10 , and evidence for cardiorenal protection has expanded their role to include heart failure management 11 . However, as SGLT2 increases urinary glucose excretion, there are concerns regarding urinary tract infection (UTI), especially after the US Food and Drug Administration revised labels of SGLT2i for warnings on serious UTI 12 . Evidence on UTI risk is inconsistent across studies, and effects may differ by patient characteristics and clinical context 13 , 14 , 15 . Recent studies have demonstrated potential benefits of SGLT2i in immune‐mediated inflammatory diseases (IMIDs). SGLT2i may attenuate inflammatory and fibrosis‐related pathways, including reductions in circulating biomarkers 16 . Additionally, recent large observational studies have assessed SGLT2i safety in specific IMID settings, examining UTI risk in rheumatoid arthritis and cardiorenal and other safety outcomes in systemic lupus erythematosus (SLE) with comorbid T2D 17 , 18 . However, evidence remains limited for UTI risk across a broader spectrum of IMIDs and for clinically relevant effect modification by treatment intensity, including glucocorticoid dose and concomitant immunosuppressive regimens.

We evaluated whether initiation of an SGLT2i is associated with an increased risk of UTI, upper UTI, or genital infection among patients with IMIDs and comorbid T2D across a broad spectrum of IMIDs and clinically relevant immunosuppressive regimens. Because patients with IMIDs are typically underrepresented in SGLT2i randomized trials, and a dedicated trial comparing SGLT2i and metformin initiation across diverse IMIDs and immunosuppressive regimens would be difficult to conduct at scale, we emulated a hypothetical target trial using observational data. Using the JMDC hospital‐based claims database, we emulated this comparison with an active‐comparator, new‐user design and propensity score‐based weighting.


## MATERIALS AND METHODS


### Study design and data source

This retrospective cohort study employed an active‐comparator, new‐user design 19 , using the JMDC hospital‐based claims database (JMDC Inc., Tokyo, Japan) covering the period from April 1, 2014, to January 31, 2024. We conducted a target trial emulation using observational data 20 . The target trial specification and its emulation are summarized in Table S1 following the TARGET statements 21 . The JMDC hospital‐based claims database is a nationwide Japanese database that provides anonymized longitudinal patient‐level records, including demographics and clinical information such as International Classification of Diseases, 10th Revision (ICD‐10)‐coded diagnoses, procedures, prescriptions, laboratory tests, and measures of healthcare utilization 22 .


### Participants

We included patients with IMIDs and comorbid T2D who were newly initiated on an SGLT2i or metformin during the study period. Metformin was selected as the active‐comparator because it does not increase urinary glucose excretion and has not been associated with an increased risk of UTI. In Japan, metformin and SGLT2i are commonly co‐prescribed, and fixed‐dose combinations with dipeptidyl peptidase‐4 (DPP‐4) inhibitors are available, supporting metformin as an appropriate reference drug for comparative safety evaluation.

Patients were excluded if they had no diagnosis of diabetes; had type 1 diabetes, hemodialysis, organ transplantation, or a history of UTI; had received systemic antibiotics within the prior 3 months; or were not receiving immunosuppressive or immunomodulatory therapy. We required at least 3 months of observable prescription history before the index date. To identify new users, we excluded patients with any prior use of SGLT2i or metformin during the available pre‐index prescription history.

The disease, medication, and procedure codes used for cohort definitions are provided in Tables S2–S4.


### Exposure

The main source of exposure was the initiation of SGLT2i in new users, and comparison groups comprised patients who received newly initiated metformin therapy (Table S3).

The index date (time zero) was defined as the date of initiation of the first study drug (SGLT2i or metformin). New users were operationally defined as patients with at least 3 months of observable prescription history before the index date, including a 3‐month washout period with no prescription for the index drug.


### Outcomes

The primary outcome was UTI. The secondary outcomes were upper UTI (as a marker of more severe infection) and genital infection. For UTI outcomes, events were defined on the date of systemic antibiotic prescription, with an ICD‐10‐coded UTI diagnosis recorded on that date or within the subsequent 30 days (Tables S2, S3). UTI captured both upper and lower UTI, whereas the upper UTI was analyzed separately as a secondary outcome. To reduce misclassification, sulfamethoxazole‐trimethoprim, which is commonly used for pneumocystis pneumonia prophylaxis, was excluded from the antibiotic definition. Genital infection was defined as an ICD‐10‐coded diagnosis of genital infection (Table S2).

We used an intention‐to‐treat (ITT) approach for all outcomes 23 . Patients were classified according to the index drug and remained in that group throughout follow‐up, regardless of subsequent treatment changes, including discontinuation of the index drug, switching, or initiation of the comparator drug. Follow‐up continued from the index date until the earliest outcome occurrence, the end of available observation (the last day of the final observable month), or 1,095 days (3 years). Concomitant use of other antidiabetic agents was permitted in both groups.


### Data collection

We collected data on baseline demographic and clinical characteristics, including age, sex, IMID diagnosis, glycosylated hemoglobin (HbA1c) level, treatment‐related variables, and comorbidities. The baseline covariates were assessed using data recorded prior to the index date unless otherwise specified.

Treatment‐related variables included the use of antidiabetic drugs, immunosuppressive agents and immunomodulators, biologics, and targeted synthetic disease‐modifying antirheumatic drugs (b/tsDMARDs), and glucocorticoids. The use of these medications was identified during the 3 months before the index date, except for rituximab, which was identified during the 6 months before the index date because of its prolonged biological effect. The HbA1c level was defined as the measurement closest to the index date within the prior 3 months. The glucocorticoid dose (mg/day) was defined as the maximum prednisolone‐equivalent daily dose during the month prior to the index date. If no glucocorticoid prescription was recorded in the most recent month, we used the maximum dose recorded during the prior 3 months. Patients with glucocorticoid use for <7 days during the prior 3 months were classified as non‐users.


### Covariates

We constructed a directed acyclic graph (DAG) based on prior knowledge and clinical reasoning to guide covariate selection. The DAG was used to identify a minimally sufficient adjustment set by blocking backdoor paths between the exposure (initiation of SGLT2i vs. metformin) and outcome (UTI). In addition, we included strong prognostic factors for UTI to improve precision (Figure S1).

The adjustment variables were age, sex, HbA1c level, kidney disease, heart disease, malignancy, glucocorticoid dose (prednisolone equivalent), immunosuppressive agents, b/tsDMARDs, and diabetes‐related complications. Additional prognostic factors included urinary tract disease, cerebral vascular disease, peripheral vascular disease, and fracture.


### Statistical analysis

Data were summarized as frequencies (percentages) for categorical variables and means (standard deviations) for continuous variables. Missing HbA1c level values were handled using multiple imputation by chained equations with 100 imputations 24 . The imputation model included baseline covariates used in the propensity score model, treatment group, the outcome event indicator, and the Nelson–Aalen cumulative hazard estimate as auxiliary variables to incorporate survival outcome information into the imputation process 25 . Estimates were combined across imputations using Rubin's rules 26 .

To adjust for confounding, we estimated propensity scores within each imputed dataset and applied stabilized inverse probability of treatment weights (IPTW) to estimate the average treatment effect 27 , 28 , 29 . Propensity score overlaps before and after weighting was visually assessed (Figure S2A,B). Covariate balance after weighting was assessed using standardized mean differences, with values <0.1 indicating adequate balance (Table S5).

Time‐to‐event outcomes were analyzed under an ITT approach using IPTW‐weighted Cox proportional hazards models with robust variance estimation to obtain hazard ratios (HRs) and 95% confidence intervals (CIs). IPTW‐weighted Kaplan–Meier curves were used to visualize the cumulative incidence of UTI, upper UTI, and genital infection. Prespecified subgroup analyses were conducted by age (<70 vs. ≥70 years), sex, IMID type (rheumatoid arthritis, polymyalgia rheumatica, SLE, and vasculitis), use of immunosuppressive medications, use of b/tsDMARDs, and glucocorticoid dose (0, ≤5, >5–10, >10–20, and >20 mg/day prednisolone equivalent). Effect modification for UTI and upper UTI was further assessed using interaction terms between the treatment group and key variables (glucocorticoid use, immunosuppressive agents, and b/tsDMARDs). Significance level was set at P < 0.05. All analyses were conducted using R version 4.4.2 (R Foundation for Statistical Computing, Vienna, Austria).


### Sensitivity analysis

To address potential informative censoring due to the end of available observation in the per‐protocol analysis, we applied inverse probability of censoring weighting (IPCW). For IPCW estimation, the follow‐up period was divided into 90‐day intervals. Stabilized IPCW weights were then estimated using pooled logistic regression models for censoring, with follow‐up time modeled using natural cubic splines. The final analysis weights were calculated as the product of the IPTW and IPCW weights. We used weighted Cox proportional hazards models with robust variance estimation clustered by patient to estimate the HRs. To account for missing data, analyses were performed across multiple imputed datasets, and the results were pooled using Rubin's rules.


### Ethical considerations

All procedures were conducted in accordance with the ethical standards of the committee responsible for human experimentation (institutional and national) and the Helsinki Declaration of 1964 and later versions. This study was approved by the Institutional Review Board of Juntendo University (authorization number: E25‐0009). The requirement for written informed consent was waived owing to the anonymized nature of the JMDC database.


## RESULTS


### Patient characteristics

A total of 8,701,138 individuals were assessed, of whom 787,737 had a diagnosis code for an IMID. After applying the eligibility criteria, we identified 1,845 new users of SGLT2i and 1,499 new users of metformin (Figure 1). The mean age was 72.3 years in the SGLT2i group and 71.1 years in the metformin group; the proportions of male patients were 46.3% and 42.6%, respectively. The mean HbA1c level was lower in the SGLT2i group than in the metformin group (7.23% vs. 7.87%), although the values were missing in 82.8% of patients. Rheumatoid arthritis was the most common IMID in both groups (65.0% vs. 68.2%), followed by polymyalgia rheumatica (14.0% vs. 17.7%) and SLE (12.1% vs. 7.5%). Before weighting, the SGLT2i group demonstrated a higher prevalence of kidney disease (37.1% vs. 15.0%), heart disease (57.5% vs. 34.0%), and vascular disease (27.7% vs. 17.9%) than the metformin group did. DPP‐4 inhibitors were the most common concomitant antidiabetic drugs in both groups (45.5% vs. 58.5%). Among SGLT2i initiators, dapagliflozin (39.6%) and empagliflozin (34.6%) were most frequently prescribed. Use of immunosuppressive agents (36.1% vs. 41.1%) and b/tsDMARDs (15.2% vs. 13.1%) was similar between the groups, and among glucocorticoid users, the mean prednisolone‐equivalent dose was 8.98 mg/day in the SGLT2i group and 10.03 mg/day in the metformin group (Table 1). No baseline covariates other than HbA1c level had missing values. After IPTW, all covariates included in the propensity score model were well balanced, with absolute standardized mean differences <0.1 (Table S5).

> **Figure 1** Selection process flowchart for new users of SGLT2i and metformin among patients with immune‐mediated inflammatory diseases. Flowchart showing cohort selection from the JMDC hospital‐based claims database. Of 8,701,138 individuals, 787,737 had immune‐mediated inflammatory diseases. After excluding non‐users of SGLT2i and metformin and patients meeting prespecified exclusion criteria, the final cohort comprised 1,845 new users of SGLT2i and 1,499 new users of metformin. SGLT2i, sodium‐glucose cotransporter 2 inhibitor; UTI, urinary tract infection.

> **Table 1** Baseline characteristics of the study population

The median follow‐up was 621 days (interquartile range [IQR], 244–1,095) in the metformin group and 481 days (IQR, 183–864) in the SGLT2i group. The follow‐up ended due to administrative censoring at 1,095 days in 431 metformin initiators (28.8%) and 330 SGLT2i initiators (17.9%). Follow‐up ended due to the end of available observation in 952 metformin initiators (63.5%) and 1,383 SGLT2i initiators (75.0%).


### UTI after SGLT2i versus metformin initiation (primary outcome)

UTI occurred in 132 of 1,845 patients (7.2%) in the SGLT2i group and 116 of 1,499 patients (7.7%) in the metformin group. In the IPTW‐adjusted analysis, the weighted incidence rates were 48.8 and 42.2 per 1,000 person‐years in the SGLT2i and metformin groups, respectively. In IPTW‐weighted Cox proportional hazards models, UTI risk did not differ significantly between the groups (HR 1.14, 95% CI 0.84–1.55; P = 0.393; Figure 2A).

> **Figure 2** Kaplan–Meier curves adjusted using propensity score‐based weighting. Occurrence of (A) UTI, (B) upper UTI in SGLT2i, and (C) genital infections in the SGLT2i and metformin groups. (A) Alt text: Kaplan–Meier plot of UTI‐free survival comparing SGLT2i and metformin over 1,095 days. The curves largely overlap during follow‐up, and the adjusted hazard ratio is 1.14 (95% CI 0.84–1.55; P = 0.39). Numbers at risk are displayed below. (B) Kaplan–Meier plot of upper UTI‐free survival comparing SGLT2i and metformin over 1,095 days. The curves largely overlap during follow‐up, and the adjusted hazard ratio is 1.28 (95% CI 0.71–2.31; P = 0.42). Numbers at risk are displayed below. (C) Kaplan–Meier plot of genital infection‐free survival comparing SGLT2i and metformin over 1,095 days. The SGLT2i group shows lower genital infection‐free survival during follow‐up, and the adjusted hazard ratio is 2.31 (95% CI 1.16–4.63; P = 0.02). Numbers at risk are displayed below. CI, confidence interval; GI, genital infection; HR, hazard ratio; SGLT2i, sodium‐glucose cotransporter 2 inhibitor; UTI, urinary tract infection.


### Upper UTI and genital infection after SGLT2i versus metformin initiation (secondary outcomes)

Upper UTI occurred in 34 of 1,845 patients (1.8%) in the SGLT2i group and 25 of 1,499 patients (1.7%) in the metformin group. In the IPTW‐adjusted analysis, the weighted incidence rates were 12.6 and 9.8 per 1,000 person‐years in the SGLT2i and metformin groups, respectively. In IPTW‐weighted Cox proportional hazards models, upper UTI risk did not differ significantly between the groups (HR 1.28, 95% CI 0.71–2.31, P = 0.416; Figure 2B). Genital infection occurred in 27 of 1,845 patients (1.5%) in the SGLT2i group and 13 of 1,499 patients (0.9%) in the metformin group. In the IPTW‐adjusted analysis, the weighted incidence rates were 9.6 and 4.1 per 1,000 person‐years in the SGLT2i and metformin groups, respectively. In IPTW‐weighted Cox proportional hazards models, genital infection risk was higher in the SGLT2i group than in the metformin group (HR 2.31, 95% CI 1.16–4.63, P = 0.023; Figure 2C).


### Subgroup analysis

In the prespecified subgroup analyses of UTI, the HRs for SGLT2i versus metformin were generally consistent across patient demographics and treatment characteristics (Figure 3A). The point estimate was higher in male patients (HR 1.73, 95% CI 1.02–2.95) than in female patients (HR 0.92, 95% CI 0.64–1.34), although the CIs were wide across the subgroups. No clear trend was observed across the glucocorticoid dose categories.

> **Figure 3** Subgroup analyses of infection risk (forest plots): The HRs for (A) UTI and (B) upper UTI in the SGLT2i and metformin groups. (A) Forest plot showing subgroup analyses of UTI risk for SGLT2i versus metformin by age, sex, disease type, medication use, and glucocorticoid dose. Most HRs are close to 1.0, and most CIs cross 1.0. The point estimate is higher in male patients than in female patients, and no clear trend is observed across glucocorticoid dose categories. (B) Forest plot showing subgroup analyses of upper UTI risk for SGLT2i versus metformin by age, sex, disease type, medication use, and glucocorticoid dose. HRs are generally close to 1.0, and all CIs cross 1.0. CIs are wide in several subgroups, indicating limited precision. CI, confidence interval; HR, hazard ratio; PMR, polymyalgia rheumatica; PSL, prednisolone; RA, rheumatoid arthritis; SGLT2i, sodium‐glucose cotransporter 2 inhibitor; SLE, systemic lupus erythematosus; tsDMARD, targeted synthetic disease‐modifying antirheumatic drug; UTI, urinary tract infection.

For upper UTI, the HRs did not differ significantly across the subgroups (Figure 3B). By sex, the HR was 1.03 (95% CI 0.50–2.16) in female patients and 1.84 (95% CI 0.66–5.14) in male patients, with wide CIs.


### Effect modification of SGLT2i‐associated UTI risk by concomitant immunosuppressive therapy

For UTI, there was no evidence of interaction between SGLT2i and glucocorticoid use (interaction HR 1.07, 95% CI 0.49–2.34, P = 0.857), immunosuppressive agent use (interaction HR 1.03, 95% CI 0.55–1.94, P = 0.922), or b/tsDMARD use (interaction HR 0.55, 95% CI 0.19–1.57, P = 0.264). For upper UTI, no evidence of interaction was observed for glucocorticoid use (interaction HR 0.75, 95% CI 0.15–3.75, P = 0.731), immunosuppressive agent use (interaction HR 1.33, 95% CI 0.34–5.19, P = 0.680), or b/tsDMARD use (interaction HR 0.70, 95% CI 0.09–5.58, P = 0.740; Table 2).

> **Table 2** Interaction analysis: effect modification of the association between SGLT2i initiation and UTI risk by concomitant immunosuppressive therapy


### Sensitivity analysis

In the per‐protocol analysis, the median follow‐up was 186 days (IQR, 64–500) in the metformin group and 218 days (IQR, 75–531) in the SGLT2i group. In crude analyses, UTI risk was similar between the groups (HR 0.88, 95% CI 0.64–1.20). In the IPTW×IPCW‐weighted Cox models, UTI risk did not differ between the groups (HR 1.01, 95% CI 0.65–1.57), and the weighted incidence rates were similar (50.1 vs. 49.2 per 1,000 person‐years) (Figure S3).


## DISCUSSION


### Summary of results

In this study of patients with IMIDs and comorbid T2D, initiation of an SGLT2i was not associated with a higher risk of UTI, compared with metformin initiation, in IPTW‐adjusted analyses (HR 1.14, 95% CI 0.84–1.55). Risk of upper UTI also did not differ significantly between the groups (HR 1.28, 95% CI 0.71–2.31). In contrast, SGLT2i initiation was associated with an increased risk of genital infection (HR 2.31, 95% CI 1.16–4.63), compared with metformin initiation. Subgroup analyses suggested potential heterogeneity, with a higher UTI risk estimate in male patients than in female patients (HR 1.73, 95% CI 1.02–2.95). However, interaction analyses did not provide statistical evidence of effect modification by concomitant immunosuppressive therapies.


### Comparison with existing studies

Evidence regarding the association between SGLT2i use and UTI risk in patients with diabetes remains mixed 30 , 31 , 32 , 33 . Whether these findings extend to patients with IMIDs is uncertain because infection susceptibility may be shaped by disease‐related immune dysfunction and concomitant immunosuppressive therapies 34 , 35 . In our IMID‐focused cohort with comorbid T2D, initiation of SGLT2i was not associated with a higher UTI risk compared with metformin initiation.

Likewise, among patients with rheumatoid arthritis and T2D, SGLT2i initiation was not associated with an increased risk of UTI in an ITT analysis 17 . A large study among patients with SLE and T2D similarly found no significant difference in UTI risk, but a higher risk of genital infections, among patients initiating SGLT2i versus DPP‐4 inhibitors 18 . These studies suggest that genital infections are consistently increased after SGLT2i initiation, whereas a clear increase in UTI risk has not been observed in immunocompromised IMID populations.

In the subgroup analyses for UTI, the HR was higher among male patients than female patients. Although UTIs are generally more common in female individuals than in male individuals in the general population 36 , differential diagnostic and prescription thresholds for suspected UTI may influence claims‐based outcome ascertainment, particularly in men. This finding is consistent with prior reports suggesting a higher risk of UTI or complicated UTI among older male individuals treated with SGLT2i, potentially reflecting underlying voiding dysfunction, such as benign prostatic hyperplasia 37 . Nevertheless, evidence for a male‐specific increase is not consistent across studies, and residual confounding remains possible.

Regarding glucocorticoid exposure, we found no clear dose–response pattern for UTI risk. Glucocorticoids can induce hyperglycemia and immunosuppression, which could increase susceptibility to infection among patients treated with SGLT2i. However, estimates in higher‐dose categories were imprecise because of limited event numbers, particularly for upper UTI.


### Clinical implications

From a clinical perspective, initiating SGLT2i may be a glucose‐lowering option for patients with IMIDs and comorbid T2D without an apparent increase in overall UTI risk, compared with initiating metformin. This is relevant rheumatologically, where cardiometabolic comorbidity is common, and selection of antidiabetic therapy must balance glycemic control with infection concerns. At the same time, genital infections were more frequent after SGLT2i initiation, underscoring the importance of counseling on genital hygiene and early symptom recognition.

These results should not be interpreted as an absence of risk in all patients. The higher UTI risk estimate observed among men and the imprecision of estimates in certain strata, particularly for upper UTI and higher glucocorticoid categories, support a practical approach to risk mitigation. In practice, assessment of baseline UTI risk, patient education regarding early symptoms of infection, and prompt clinical review when symptoms occur may be reasonable when initiating SGLT2i in immunocompromised patients.

Overall, these findings are reassuring regarding the overall UTI risk with SGLT2i initiation in IMID patients with T2D. They also highlight the value of close collaboration between rheumatology and diabetes care teams to support individualized treatment decisions and monitoring in higher‐risk patients.


### Strengths and limitations

Our study has several strengths. First, JMDC hospital‐based database captures clinical information from participating medical institutions, including laboratory test results 22 . This is valuable because insurance‐based databases may have incomplete capture among older adults who transition to the Late‐Stage Elderly Healthcare System at the age of 75 years 38 . Availability of the HbA1c level data enabled adjustment for glycemic control, a clinically relevant marker related to diabetes severity. Second, we emulated a treatment‐initiation contrast using an active‐comparator new‐user design with IPTW. Covariates were selected using a prespecified DAG, and balance after weighting was achieved. Third, we strengthened outcome validity by excluding patients with prior UTI and recent systemic antibiotic use. We defined UTI using diagnostic codes in combination with systemic antibiotic prescriptions and excluded sulfamethoxazole‐trimethoprim to reduce misclassification related to pneumocystis prophylaxis. Follow‐up for up to 3 years allowed assessment of short‐ and longer‐term infection outcomes. Fourth, prior evidence on urogenital infection risk in IMIDs has largely been derived from disease‐specific studies, particularly those focusing on rheumatoid arthritis and SLE 17 , 18 . This leaves an important gap in understanding whether the risk profile is similar across different IMIDs. In addition, concomitant immunosuppressive therapies may modify infection risk, yet this potential heterogeneity has not been adequately examined in a broader IMID population. To our knowledge, no previous study has evaluated urogenital infection risk across multiple IMIDs while also assessing heterogeneity according to concomitant immunosuppressive therapies. Our study addresses this gap by providing evidence from a clinically relevant population that reflects both disease diversity and variation in treatment context.

Despite these strengths, this study has some limitations. First, because treatment was not randomized, residual confounding may have remained owing to factors not captured in the database, including lifestyle factors and detailed measures of IMID activity and severity. To mitigate this, we used an active‐comparator new‐user design, adjusted for a prespecified set of confounders informed by a DAG, and achieved good covariate balance after weighting. Second, outcome incidence may have been underestimated because the JMDC hospital‐based database does not capture care received at non‐participating institutions, and events managed elsewhere may not have been recorded. However, because both treatment groups were drawn from the same data source under an active‐comparator design, incomplete capture is likely to affect both groups similarly, limiting bias in relative effect estimates. In addition, this database is not restricted by insurer enrollment and includes a broad age range, including many older adults at increased risk of both diabetes‐related complications and infections, and provides access to laboratory data, making it suitable for the present study population. Third, although we defined UTI using diagnostic codes in combination with systemic antibiotic prescriptions to improve specificity, some degree of outcome misclassification is still possible in claims‐based research. To improve outcome validity, we used a definition informed by prior studies 32 and excluded sulfamethoxazole‐trimethoprim, which is frequently prescribed for Pneumocystis prophylaxis in this population. Fourth, the HbA1c level values were missing in a large proportion of patients. Because it is an important factor for infection risk, we retained it using multiple imputation with 100 imputations to support stable estimates. Finally, subgroup analyses were limited by small event numbers in some strata, particularly for upper UTI and higher glucocorticoid dose categories, resulting in wide CIs. However, at least within our subgroup analyses, we did not observe a clear dose‐related trend across glucocorticoid dose categories. These subgroup findings should therefore be interpreted cautiously and confirmed in larger cohorts.


### Conclusion

Using a Japanese hospital‐based database with laboratory data, we did not observe a clear increase in UTI risk with SGLT2i initiation compared with metformin initiation among patients with IMIDs and comorbid T2D. However, genital infections were more frequent with SGLT2i initiation than with metformin initiation. Subgroup findings were exploratory and warrant confirmation in larger studies.


## FUNDING

This work was supported by the Japan Society for the Promotion of Science (JSPS) KAKENHI (Grant Number JP24K21148).


## DISCLOSURE

H.T. served as a paid instructor for Nippon Kayaku Co., Ltd., Nippon Shinyaku Co., Ltd., Ayumi Pharmaceutical Co., Ltd., Asahi Kasei Pharma Co., Ltd., Astellas Pharma Inc., and AstraZeneca K.K.; and received honoraria from AstraZeneca K.K., Eisai Co., Ltd., Eli Lilly Japan K.K., AbbVie Inc., Chugai Pharmaceutical Co., Ltd., GlaxoSmithKline K.K., Astellas Pharma Inc., Nippon Boehringer Ingelheim Co., Ltd., Kissei Pharmaceutical Co., Ltd., Taisho Pharmaceutical Co., Ltd., and Asahi Kasei Pharma Co., Ltd. T.N. received speaker honoraria from Sumitomo Pharma Co., Ltd., Novo Nordisk Pharma Ltd., Mitsubishi Tanabe Pharma Corporation, Bayer Yakuhin, Ltd., and Eli Lilly Japan K.K., and received research grants from LifeScan Japan, Inc. and Kowa Company, Ltd. R.S. received consulting fees from Chugai Pharmaceutical Co., Ltd. and Nippon Kayaku Co., Ltd., and research funding from Chugai Pharmaceutical Co., Ltd. and Pfizer Japan Inc. A.K. received honoraria from AbbVie Inc., Eli Lilly Japan K.K., Asahi Kasei Pharma Co., Ltd., Chugai Pharmaceutical Co., Ltd., and Otsuka Pharmaceutical Co., Ltd. H.N. received a research grant from GlaxoSmithKline K.K. and consulting fees from GlaxoSmithKline K.K., Sony Group Corporation, and Kowa Company, Ltd., outside the submitted work. N.T. received speaker honoraria from AstraZeneca K.K., AbbVie Inc., Eli Lilly Japan K.K., GlaxoSmithKline K.K., Kissei Pharmaceutical Co., Ltd., UCB Japan Co., Ltd., and Otsuka Pharmaceutical Co., Ltd., and received research grants from Asahi Kasei Pharma Co., Ltd., Ayumi Pharmaceutical Co., Ltd., Bristol Myers Squibb K.K., Cell Exosome Therapeutics Co., Ltd., Nippon Boehringer Ingelheim Co., Ltd., Taisho Pharmaceutical Co., Ltd., and Chugai Pharmaceutical Co., Ltd. N.Y. declares no conflicts of interest.

Approval of the research protocol: All procedures were conducted in accordance with the ethical standards of the committee responsible for human experimentation (institutional and national) and the Helsinki Declaration of 1964 and later versions. This study was approved by the Institutional Review Board of Juntendo University (authorization number: E25‐0009). The requirement for written informed consent was waived owing to the anonymized nature of the JMDC database.

Informed consent: N/A.

Registry and the registration no. of the study/trial: N/A.

Animal studies: N/A.


## Supporting information
