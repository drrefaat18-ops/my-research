from h import *
PEA='(palmitoylethanolamide OR "palmitoyl ethanolamide" OR palmitoylethanolamine OR "N-palmitoylethanolamine")'
qs={
 'EPMC_delta':f'{PEA} AND (arthritis OR glucocorticoid* OR prednisolone OR Freund OR corticosteroid*) AND FIRST_IDATE:[2026-09-25 TO 2026-12-31]',
 'EPMC_PPR':f'{PEA} AND (arthritis OR glucocorticoid* OR prednisolone OR Freund OR corticosteroid* OR dexamethasone) AND SRC:PPR',
 'EPMC_OS_title_abs':f'(TITLE_ABS:palmitoylethanolamide OR TITLE_ABS:"palmitoyl ethanolamide") AND (TITLE_ABS:malondialdehyde OR TITLE_ABS:glutathione OR TITLE_ABS:"superoxide dismutase" OR TITLE_ABS:catalase OR TITLE_ABS:"oxidative stress" OR TITLE_ABS:Nrf2) AND (TITLE_ABS:arthritis OR TITLE_ABS:Freund OR TITLE_ABS:adjuvant OR TITLE_ABS:synovial OR TITLE_ABS:synovitis)',
 'EPMC_OS_fulltext_CFA':f'(TITLE_ABS:palmitoylethanolamide OR TITLE_ABS:"palmitoyl ethanolamide") AND (malondialdehyde OR "superoxide dismutase") AND ("Freund\'s adjuvant" OR "adjuvant-induced arthritis" OR "adjuvant arthritis")',
 'EPMC_mech_fulltext':f'(TITLE_ABS:palmitoylethanolamide OR TITLE_ABS:"palmitoyl ethanolamide") AND ("p38 MAPK" OR "TLR4" OR "NF-κB p65" OR "NF-kB p65") AND ("adjuvant-induced arthritis" OR "adjuvant arthritis" OR "Freund\'s adjuvant" OR "collagen-induced arthritis")',
 'EPMC_GC_fulltext_arth':f'(TITLE_ABS:palmitoylethanolamide OR TITLE_ABS:"palmitoyl ethanolamide") AND (prednisolone OR prednisone OR methylprednisolone) AND (arthritis)',
 'EPMC_pred_TA':f'TITLE_ABS:{PEA} AND (TITLE_ABS:prednisolone OR TITLE_ABS:prednisone OR TITLE_ABS:dexamethasone OR TITLE_ABS:glucocorticoid OR TITLE_ABS:corticosteroid OR TITLE_ABS:"steroid-sparing")',
 'EPMC_JAK_fulltext':f'(TITLE_ABS:palmitoylethanolamide OR TITLE_ABS:"palmitoyl ethanolamide") AND (baricitinib OR tofacitinib OR tacrolimus) AND (arthritis)',
 'EPMC_GCsparing_fulltext':f'palmitoylethanolamide AND ("steroid-sparing" OR "glucocorticoid-sparing" OR "corticosteroid-sparing")',
}
res={}
for k,q in qs.items():
    n,out=epmc(q); res[k]={'q':q,'n':n,'rec':out}
    print('=====',k,n)
    for o in out[:80]: print(' ',o[0],o[1],o[2],o[4],(o[5] or '')[:130],'|',(o[6] or '')[:30])
    time.sleep(1)
save('epmc.json',res)
