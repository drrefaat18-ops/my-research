from h import *
qs={'PM_delta':('(palmitoylethanolamide OR palmitoylethanolamide[tw] OR "palmitoyl ethanolamide" OR PEA[ti]) AND (arthritis OR glucocorticoid* OR prednisolone OR Freund OR corticosteroid* OR dexamethasone)',{'datetype':'edat','mindate':'2026/09/25','maxdate':'2026/12/31'}),
 'PM_delta_broad':('palmitoylethanolamide OR "palmitoyl ethanolamide" OR palmitoylethanolamine',{'datetype':'edat','mindate':'2026/09/25','maxdate':'2026/12/31'}),
 'PM_OS':('(palmitoylethanolamide OR "palmitoyl ethanolamide" OR palmitoylethanolamine) AND (malondialdehyde OR glutathione OR "superoxide dismutase" OR catalase OR "oxidative stress" OR Nrf2 OR antioxidant*) AND (arthritis OR Freund OR adjuvant OR synovi* OR joint OR osteoarthritis)',None),
 'PM_mech':('(palmitoylethanolamide OR "palmitoyl ethanolamide" OR palmitoylethanolamine) AND ("NF-kappaB" OR "NF-kB" OR "NF-κB" OR p65 OR "p38" OR MAPK OR TLR4 OR "toll-like receptor 4") AND (arthritis OR Freund OR adjuvant OR synovi* OR "CFA")',None),
 'PM_GC':('(palmitoylethanolamide OR "palmitoyl ethanolamide" OR palmitoylethanolamine) AND (prednisolone OR prednisone OR dexamethasone OR methylprednisolone OR glucocorticoid* OR corticosteroid* OR steroid-sparing OR "steroid sparing")',None),
 'PM_JAK':('(palmitoylethanolamide OR "palmitoyl ethanolamide") AND (baricitinib OR tofacitinib OR upadacitinib OR "JAK inhibitor" OR tacrolimus OR cyclosporin* OR ciclosporin OR calcineurin)',None),
}
res={}
for k,(q,ex) in qs.items():
    n,out=pubmed(q,ex); res[k]={'q':q,'extra':ex,'n':n,'rec':out}
    print('=====',k,n)
    for o in out: print(' ',o[0],o[1][:4],o[2][:150],'|',o[3])
    time.sleep(0.5)
save('pubmed.json',res)
