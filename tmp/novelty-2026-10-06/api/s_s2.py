from h import *
F='title,year,externalIds,venue'
rel=[('rel','palmitoylethanolamide prednisolone'),('rel','palmitoylethanolamide dexamethasone'),('rel','palmitoylethanolamide rheumatoid arthritis'),('rel','palmitoylethanolamide adjuvant arthritis'),('rel','palmitoylethanolamide glucocorticoid sparing'),('rel','palmitoylethanolamide oxidative stress arthritis')]
bulk=[('bulk','palmitoylethanolamide + (prednisolone | dexamethasone | glucocorticoid | corticosteroid)'),('bulk','palmitoylethanolamide + (arthritis | Freund | synovitis)'),('bulk','palmitoylethanolamide + (baricitinib | tofacitinib | tacrolimus)')]
res={}
for kind,q in rel+bulk:
    url='https://api.semanticscholar.org/graph/v1/paper/search'+('/bulk' if kind=='bulk' else '')
    p={'query':q,'fields':F}
    if kind=='rel': p['limit']=100
    r=get(url,p,tries=6,wait=6)
    key=kind+':'+q
    if r.status_code!=200:
        print('=====',key,'HTTP',r.status_code,r.text[:200]); res[key]={'status':r.status_code}; time.sleep(8); continue
    j=r.json(); data=j.get('data',[])
    res[key]={'status':200,'total':j.get('total'),'rec':data}
    print('=====',key,'total',j.get('total'),'got',len(data))
    for d in data: print(' ',d.get('year'),(d.get('title') or '')[:130],'|',(d.get('externalIds') or {}).get('PubMed'),(d.get('externalIds') or {}).get('DOI'))
    time.sleep(5)
save('s2.json',res)
