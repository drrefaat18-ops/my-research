from h import *
qs=['palmitoylethanolamide prednisolone','palmitoylethanolamide glucocorticoid arthritis','palmitoylethanolamide adjuvant-induced arthritis','palmitoylethanolamide baricitinib','palmitoylethanolamide tofacitinib','palmitoylethanolamide tacrolimus','palmitoylethanolamide Freund adjuvant arthritis rats oxidative stress','palmitoylethanolamide dexamethasone']
res={}
for q in qs:
    r=get('https://api.crossref.org/works',{'query.bibliographic':q,'rows':40,'select':'DOI,title,issued,container-title,type'})
    if r.status_code!=200: print('=====',q,'HTTP',r.status_code); continue
    m=r.json()['message']; it=m['items']
    res[q]={'n':m['total-results'],'rec':it}
    print('=====',q,m['total-results'])
    for x in it:
        t=(x.get('title') or [''])[0]
        y=(x.get('issued',{}).get('date-parts') or [[None]])[0][0]
        print(' ',y,t[:120],'|',x['DOI'])
    time.sleep(1)
save('crossref.json',res)
