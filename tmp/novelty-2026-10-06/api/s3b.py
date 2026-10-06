from h import *
qs={'PM_CFA':'(palmitoylethanolamide OR "palmitoyl ethanolamide" OR palmitoylethanolamine OR "N-palmitoylethanolamine" OR ALIAmide* OR "N-acylethanolamine acid amidase" OR NAAA) AND (Freund OR "adjuvant arthritis" OR "adjuvant-induced" OR "adjuvant induced" OR CFA OR "collagen-induced" OR "rheumatoid arthritis" OR "monoarthritis" OR "polyarthritis")',
 'PM_arthritis_all':'(palmitoylethanolamide OR "palmitoyl ethanolamide" OR palmitoylethanolamine) AND (arthritis OR arthritic OR synovitis OR synovial)'}
res={}
for k,q in qs.items():
    n,out=pubmed(q); res[k]={'q':q,'n':n,'rec':out}
    print('=====',k,n)
    for o in out: print(' ',o[0],o[1][:4],o[2][:140],'|',o[3])
save('pubmed_b.json',res)
