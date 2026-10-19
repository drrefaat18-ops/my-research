# Use of Clinical Trial Characteristics to Estimate Costs of New Drug Development

**Authors:** Mulcahy Andrew, Rennane Stephanie, Schwam Daniel, Dickerson Reid, Baker Lawrence, Shetty Kanaka  
**Journal:** JAMA Network Open (2025)  
**DOI:** 10.1001/jamanetworkopen.2024.53275  
**PDF:** https://pmc.ncbi.nlm.nih.gov/articles/PMC11704977/


## Abstract


### Key Points


#### Question

What is the estimated cost to develop a new drug and how do research and development (R&D) costs vary across firms?


#### Findings

This economic evaluation examining 268 US-traded drug developers found that, in 2019, 20 firms accounted for 80.8% of R&D activity (measured as clinical trial patient-months) and had 27.4% lower mean and 26.7% lower median costs per patient-month vs other firms. Median and mean costs per 2019 new approved drug were $708 million and $1.31 billion, respectively, after cost of capital and discontinuation adjustments.


#### Meaning

These findings suggest that R&D costs per new drug are highly skewed, so both median and mean costs should be considered.


## Introduction

Remarkable developments in medicine, including COVID-19 treatments and cures for hepatitis C, result from investments in drug research and development (R&D). These successes have played out through a vigorous debate on the extent to which US drug price regulation—for example, Medicare negotiation1 for older, single-source drugs introduced by the Inflation Reduction Act (IRA)—might decrease R&D investments. The pharmaceutical industry argues lower prices will have catastrophic effects on R&D.2 Some prior studies have reported associations between price regulation and lower domestic R&D investment in other countries.3,4 The CBO’s score of the IRA projected lower Medicare prices would result in fewer new drugs over 30 years, but only by 1%.5 Others point to the adverse effects of high drug prices on patient access, finances, and health6,7 and maintain that companies would still bring important new drugs to market even at lower prices.8

These arguments relate to broader questions on the socially optimal level of R&D.9,10,11 While most agree that greater expected monetary returns incentivize R&D,12,13,14 the disagreement in pharmaceuticals focuses on whether the current equilibrium, where US prices for brand-name drugs are more than 200% those in other countries,15 leads to the optimal level and targeting of R&D investments.

Despite the centrality of drug-level R&D cost estimates to these debates, data are rarely disclosed by industry,16 and policymakers must rely on estimates from researchers. One oft-cited study estimates a mean R&D cost per self-originated new molecular entity (NME) at $2.8 billion (in 2018 $ US),17 while other recent estimates are lower ($879 million to $1.7 billion).18,19,20 This range reflects differences in setting and methodology,19 often driven by data availability considerations, and often stemming from ambiguity in the seemingly straightforward terms new drug, R&D, and cost. For new drug, studies differ in covering costs from discovery through an initial regulatory approval or beyond, eg, through subsequent approvals and postmarketing trials, with further distinctions for estimates in specific therapeutic area (eg, oncology21) or for certain drug candidates (eg, self-originated new drugs17). For R&D, many prior studies focus on clinical development rather than R&D broadly, quantifying clinical research activity by counts of trials by phase22 or enrolled patients. Studies vary in their handling of preclinical research and overhead (if included at all).20 On cost, studies often report direct costs and costs after adjustments for the cost of capital and discontinued development, with postadjustment costs often several times larger than direct costs. The source of cost information is also an important differentiator: some studies17 use proprietary, self-reported industry costs that cannot be validated.23,24 Many use cost data from a narrow sets of firms17,21 or drugs21 or rely on cost inputs and assumptions from analysts and vendors,20 raising important transparency and generalizability concerns.

Our study uses a novel approach to estimate R&D costs for new drugs, mitigating several of these challenges. To better account for variation in clinical research intensity and the full scope of R&D costs, we first estimate costs per patient-month using 6-year, firm-wide R&D cost and activity data from 268 drug developers. We apply these estimates to data on the number and timing of patient-months in clinical trials from the start of development through regulatory approval for a cohort of 38 NMEs approved by the US Food and Drug Administration (FDA) in 2019. Finally, we describe variation in estimates across the cohort of new drugs. While mean per-drug R&D costs are commonly reported and cited,17,20 we report medians and means to better characterize the underlying skewed distribution.


## Methods

This economic evaluation was determined to not involve human participants by the RAND Corporation institutional review board. This study is reported following the Consolidated Health Economic Evaluation Reporting Standards (CHEERS) reporting guideline, as applicable.25


### Data on Firm-Level R&D Spending and Patient-Months

We used 3 main data sources. We used the S&P Capital IQ Database to identify the largest 200 publicly traded pharmaceutical firms engaging in novel drug R&D development26 in terms of either assets or market capitalization, resulting in a combined 268 firms.26 For these firms, we abstracted 2014 to 2019 annual R&D expenses from publicly available US Securities and Exchange Commission (SEC) filings (in 2019 $ US)27 (eAppendix 1 in Supplement 1).

We used Citeline’s Trialtrove database, which consolidates and standardizes clinical trial data from ClinicalTrials.gov and other sources.28 For each phase 1 to 4 trial, Trialtrove notes the drugs and indications studied, sponsors, enrollment, key dates, and status (eg, ongoing, completed, and terminated). We used this database to derive firm-year counts of (1) patient-months, which aggregate trial-level enrolled patients across all of the firm’s clinical trials during the year, and (2) the number of new trials beginning in each year. eAppendix 1 in Supplement 1 describes our approach to identify relevant trials, impute missing data, distribute patient-months over the duration of trials, and allocate shared R&D activities to sponsors and products. After aggregation, we excluded company-year observations without R&D expenses (40 firm-years), without trials (131 firm-years), or with fewer than 100 patient-months in 1 or more years (67 firm-years, including 4 firms entirely) for a total of 264 study firms and 1311 firm-years. We assess the impact of these and other exclusion criteria in the eAppendix 2 in Supplement 1.


### Estimating Costs Per Patient-Month

To obtain a cost per patient-month, we estimated linear regressions of log-transformed, firm-year–level R&D expenses on the log-transformed patient-months counts, year-fixed effects, and a constant. We present unweighted and weighted results, using patient-month count weights to approximate industry-wide associations between patient-months and costs. Models included robust SEs adjusted for correlations within firm. We used coefficients estimated from these models to calculate the mean weighted and unweighted marginal cost per incremental patient-month.

To assess heterogeneity in this association, we present results for subsamples of firms, including a stable 2014 to 2019 panel, the top 20 firms by 2019 R&D expenditures, all firms outside the top 20, and firms with 10-K vs 20-F annual SEC filings. Separately, we estimated costs per patient-months with different trial-level inclusion criteria. Finally, we estimated other model specifications as robustness checks, including (1) adding counts of annual new trials starts to account for fixed initial costs, (2) using by-phase log-transformed patient-months, (3) omitting phase 2 trials, and (4) using separate log-transforming patient-month counts for oncology vs nononcology trials. Further details are provided in the eAppendix 2 in Supplement 1).


### Estimating R&D Costs Per New Drug

We extracted all trials with start dates prior to each drug’s initial FDA approval for a cohort of 38 NMEs approved by the FDA in 2019 (eAppendix 3 in Supplement 1). We did not restrict trials to those studying the initial approved indication. As in our estimate of costs per patient-month, we proportionally allocated patient-months for trials involving more than 1 drug or sponsor. To estimate the direct costs of drug R&D, we multiplied patient-months aggregated across applicable trials for each drug by our estimated cost per patient-month adjusted for inflation.

Firms face risks of foregone investments and discontinued R&D efforts; to account for these additional costs, we applied previously published cost of capital rates (8.1% annually29) and estimates of discontinuation rates by therapeutic area and phase30 in sequence to direct costs. In sensitivity analyses, we calculated R&D costs per new drug assuming alternative cost of capital rates, including trials still in progress at the time the drug was approved by the FDA, and under different attribution assumptions for trials with more than 1 drug or sponsor.

P values were 2-sided, and statistical significance was set at P ≤ .05. Analyses were conducted using Stata version 17 (StataCorp). Data were analyzed from January 2022 to July 2024.


## Results


### R&D Spending and Patient-Month Descriptive Statistics

Among 268 developers contributing 1311 firm-years of data, R&D spending and patient-months were concentrated in a handful of firms: in 2019, the top 20 firms accounted for 74.4% of R&D spending and 80.8% of total patient-months (Table). Mean annual R&D spending among the top 20 firms was approximately 30 times the mean among other firms in 2019 ($4.7 billion vs $140 million). The difference in total patient-month means was even larger (approximately 50-fold), suggesting potential economies of scale or a different mix of R&D activity at larger firms.

> **Table.** Firm Sample and Firm-Year Descriptive Statistics

In the stable panel of firms , mean R&D expenses remained relatively flat, as did patient-months over the same period, with no statistically significant differences (Table). Across all firms, mean R&D expense and patient-months decreased over time, driven by greater representation of smaller firms in 2018 (the year we used to define our sample) (Table).

Figure 1 plots the associations between R&D expenses and trial patient-months which form the basis for our main regression estimates. We compared 2019 R&D expense vs 2019 patient-months in levels with 2 quadratic best-fit trends, 1 weighted by patient-months and the other unweighted (Figure 1A). Then we calculated the same association with log-transformed R&D expense and patient-months to address the right-skew in both variables (Figure 1B). While the 20 largest firms remained outliers, the association between patient-months and R&D spending is generally linear, albeit with decreasing variance as log patient-months increased.

> **Figure 1.** Research and Development (R&D) Spending Per Patient-Month in 2019Figures include data from 248 companies with 2019 R&D expenses more than $0 and with more than 100 allocated patient-months in 2019.


### Estimating the Association Between R&D Costs and Patient-Months

In our main regression, we estimated coefficients on log patient-months (ie, elasticities) of 0.92 and 0.62 for weighted and unweighted models, respectively (P < .001 for both; weighted r2 = 0.85; unweighted: r2 = 0.63). In other words, for every 1% increase in patient-months, we found an associated 0.92% increase in R&D expense. The magnitude of estimated costs per patient-month varied when estimating models on a stable panel firms contributing data in all 6 years, for the top 20 firms by R&D expenditures, for all firm-years outside the top 20 firms, and for US-based firms filing only 10-K (vs 20-F) annual reports to the SEC (eAppendix 2 in Supplement 1). However, there were 3 consistent findings. First, we found a strong association between log patient-months and log R&D expenditure, with coefficients ranging from 0.69 (the largest 20 firms) to 0.95 (stable panel of firms; P < .001 in all analyses). Second, while firm-level fixed R&D costs were consistently significant, their magnitudes were small compared with total firm-year R&D expenses (<$500 000). Third, we found little variation in inflation-adjusted R&D costs over time. eAppendix 2 in Supplement 1 presents results from other model specifications, including those including separate terms for oncology and other patient-months.

These results demonstrate a significant association between R&D costs and total patient-months. They also suggest that variable costs captured by patient-months comprise most total firm-level R&D spending, rather than firm fixed costs (which would not be captured by patient-months). Together, these 2 findings suggest that patient-months are a valid unit by which to measure R&D activity.

Figure 2 illustrates the distribution of the marginal increase in R&D spending from an additional patient-month for each firm-year in our data. The mean (SD) incremental cost per patient-month was $6475 ($1014) when weighting by firm-level patient-months and $9615 ($1662) without weighting (Figure 2). Estimated costs remained relatively constant over time but varied considerably by firm size. Mean (SD) weighted costs were $6176 ($562) for the top 20 firms by R&D spending and $8501 ($980) (37.6% higher) for smaller firms. Split differently, mean (SD) costs were $6289 ($713) in the largest fifth of firms vs $11 405 ($833) (81% higher) in the smallest fifth of firms, providing additional evidence of economies of scale in larger R&D operations at the firm or trial level.

> **Figure 2.** Estimated Marginal Research and Development Cost Per Patient-MonthLines indicate the mean estimated expense per patient-month adjusting for correlation within firm over time; boxes, 95% CIs; whiskers, range of marginal effects across firm-quarter-years. All results except the unweighted total are weighted by firm-year patient-months.


### Estimated R&D Costs Per New Drug

We found highly variable and skewed costs per new drug approval after aggregating estimated R&D costs per patient-month across clinical trials for a cohort of 38 new drugs approved by the FDA in 2019 (Figure 3; eAppendix 4 in Supplement 1). For these drugs, the median (IQR) total R&D expense, reflecting all clinical trials and including adjustments for inflation, capitalization, and discontinued products,

==was approximately half of the mean expense, at $708 million ($247 million to $1.42 billion) vs mean (SD) $1.31 ($1.92) billion== ^mulcahy2025-1

. Adjustments for discontinued products and to a lesser extent for the cost of capital led to substantially higher R&D costs: across all drugs, the median (IQR) direct R&D costs were $150 ($67.6-$453) million, compared with $193 ($91.5-$610) million adjusting for cost of capital and $708 million adjusting for both cost of capital and discontinued products (with correspondingly increasing mean [SD] costs of $369 [$684] million vs $525 million [$1.02 billion]; and $1.31 billion, respectively).

> **Figure 3.** Estimated Research and Development (R&D) Costs Per New Drug Approved in 2019 (Millions)Blue circles (and whiskers) indicate the mean (with 95% CI) total estimated R&D cost for the relevant cohort of new drugs approved by the US Food and Drug Administration in 2019. Orange squares (and whiskers) indicate the median cost (and IQR).

Excluding oncology drugs only modestly changed estimated means and medians, with the exception of lower median costs adjusting for discontinued products, given the relatively lower transition probabilities for oncology vs other drugs (Figure 3). Excluding just 2 drugs—1 oncology drug studied in many indications in parallel prior to approval (alpelisib) and an osteoporosis drug with uncommonly high clinical trial enrollment (romosozumab)—decreased mean adjusted R&D costs by one-quarter ($1.31 billion to $950 million, vs a <10% decrease for the median).

Figure 4 decomposes estimated R&D costs for each of the 38 new drugs into direct cost, cost of capital, and discontinued product adjustment components and adds 2 additional components excluded from the main results due to concerns they would unreasonably inflate cost estimates: one for in-progress trials begun prior to but completed after FDA approval, and the other attributing 100% of the cost of trials testing multiple drugs and with multiple sponsors to the new drug itself. Including both these costs where applicable as an upper bound estimate increased the median (IQR) cost of developing a new drug to $1.06 billion ($361 million to $1.75 billion) and mean (SD) cost to $1.72 ($2.13) billion. Separately, when using lower (6%) and higher (11%) cost of capital assumptions compared with 8.1% in our main approach, we found that the mean R&D cost per new drug ranged from $1.18 to $1.51 billion (compared with $1.31 billion at 8.1%) and that median costs per new drug ranged from $642 to $809 million (compared with $708 million at 8.1%) (eAppendix 5 in Supplement 1).

> **Figure 4.** Estimated Research and Development (R&D) Costs Per New Drug Approved in 2019Tabular, drug-level results are provided in eAppendix 4 in Supplement 1.


## Discussion

In this economic evaluation using a novel approach and after cost of capital and discontinued product adjustments, we estimated a median R&D cost of $708 million across a cohort of 38 drugs, with a considerably higher mean cost ($1.31 billion) driven by a small number of high-cost outliers. Mean R&D costs were 26% lower when excluding just 2 drugs. Reliable R&D cost estimates are essential to assessing the appropriateness of incentives for innovation (like government-granted monopolies from patents and regulatory exclusivity) and returns to drug developers. Given these highly skewed costs per new drug, median, rather than often-used mean, expenses may better reflect the typical case for the purposes of policy discussion.

Our work makes a methodological contribution in demonstrating a new way to estimate R&D costs per new drug. Our approach allocates all of firms’ R&D costs reported annually to the SEC, including early research, fixed, overhead, and marketing-focused R&D costs often omitted or imputed by assumption in other studies, onto a similarly broad firm-level total of annual patient-months. Cost per patient-month estimates serve as a flexible building block with application to other drug cohorts and in approximating R&D costs for government-sponsored development programs. While encompassing a wider set of R&D costs compared with most other studies, our mean and median per-drug R&D costs are within the range of other studies published over the past 20 years (with means from $539 million to $2.8 billion).16,17

Our study helps scope but does not directly address difficult distinctions between investments in R&D needed to bring a new drug to market, expand regulatory approval to additional patient populations and indications, and support marketing claims, lifecycle management, and other industry objectives. While the FDA’s Data Analysis and Search Host database (eg, as used by Sertkaya et al20) enumerates trials used by the agency to support regulatory approvals, these data are not publicly available. We ultimately opted for an inclusive approach in building our estimates by incorporating clinical trials for additional indications beyond than those initially (or ever) approved by the FDA, for academic collaborations, and for trials completed late into regulatory review. We included an even broader scope of trials and costs in sensitivity analyses. For a given drug, parallel development programs for multiple indications and populations are common, often with an initial, narrower indication qualifying for Orphan Drug Act tax and exclusivity benefits. Further investigation and policy discussion focusing on incentives for R&D investments to support early discovery and development by privately held firms, initial regulatory approval, broadening indications, and other purposes (eg, to support marketing claims) are crucial.


### Limitations

As with prior studies, there are important limitations of our data, methods, and assumptions. While our sample is large compared with prior studies, it excludes privately held companies and some larger drug companies not traded in the US (eg, Roche). Private, often venture capital–funded companies account for an increasing share of early-stage development,31 meaning our results may not be representative of total industry R&D costs. However, compared with 2019 global R&D spending, our sample covers approximately two-thirds of all industry spending; closely approximates spending by the top 10 largest firms, 9 of which are in our sample32; and includes many small companies and those without currently marketed products.

Our sample composition also changed over time, with smaller firms less likely to be included in earlier years. Given that most patient-months in our sample were captured by the top firms by R&D spending, any bias would likely not substantively affect our results, particularly when weighted. Nevertheless, we conducted a robustness check using a stable panel of firms.

We relied on companies’ reported differentiation between R&D expenses and costs of in-process R&D for acquired or in-licensed products. Acquisition and licensing expenses reflect both in-process development and assumptions on the future returns from R&D investments, which are difficult to disentangle empirically. Estimated R&D costs are not net of government subsidies, tax credits, or other incentives.

Other limitations relate to the Trialtrove data and our patient-month measure of R&D activity. First, some trials may be missing from the database, biasing estimates of R&D expense per patient-month upward. However, in comparisons between the scope of clinical trials included in Trialtrove and FDA review documents for a subset of 20 drugs, Trialtrove had as many or more trials listed in each case (eAppendix 6 in Supplement 1). Second, our patient-month measure uniformly spreads costs for patients across the entire study duration, without adjusting for changing enrollment or intensity of treatment over time. We caution against comparing estimated costs per patient-month to costs per month of active treatment. We aggregated patient-months by phase and for oncology trials separately in robustness checks.

Additionally, when estimating R&D expenses per new drug, we included all trials completed prior to the drug’s initial FDA approval date, including those for indications not covered by the approval. As a sensitivity analysis, we estimated costs including in progress trials that were ongoing at the time of FDA approval. Furthermore, we excluded phase 4 clinical trials, which the FDA sometimes requires as a condition of approval, as prior studies found only a fraction of these trials are actually completed.33


## Conclusions

This economic evaluation found a median (IQR) R&D cost of $708 million ($247 million to $1.42 billion) and a mean (SD) R&D cost of $1.31 billion ($150 million) across 38 new drugs approved by the FDA in 2019, after cost of capital and development program discontinuation adjustments, with substantially lower unadjusted direct costs (mean, $369 million; median, $150 million). Policymakers and researchers should consider median R&D costs and other nonparametric descriptive statistics describing the distribution of drug-level R&D costs alongside the more often used means when considering the typical R&D costs per new drug.
