from h import *
oa=[('fulltext.search','palmitoylethanolamide prednisolone'),
    ('fulltext.search','palmitoylethanolamide prednisolone arthritis'),
    ('fulltext.search','palmitoylethanolamide glucocorticoid arthritis'),
    ('fulltext.search','palmitoylethanolamide "adjuvant-induced arthritis"'),
    ('fulltext.search','palmitoylethanolamide "adjuvant arthritis"'),
    ('fulltext.search','palmitoylethanolamide baricitinib'),
    ('fulltext.search','palmitoylethanolamide tofacitinib'),
    ('fulltext.search','palmitoylethanolamide tacrolimus arthritis'),
    ('fulltext.search','palmitoylethanolamide malondialdehyde arthritis'),
    ('fulltext.search','palmitoylethanolamide "Freund" malondialdehyde'),
    ('title_and_abstract.search','palmitoylethanolamide (arthritis OR Freund)'),
    ]
res={}
for f,q in oa:
    p={'filter':f'{f}:{q}','per-page':200,'select':'id,doi,title,publication_year,ids,primary_location'}
    r=get('https://api.openalex.org/works',p)
    key=f+':'+q
    if r.status_code!=200: print('=====',key,'HTTP',r.status_code,r.text[:200]); res[key]={'status':r.status_code}; continue
    j=r.json(); n=j['meta']['count']; rec=j['results']
    res[key]={'n':n,'rec':[(x['id'],x.get('doi'),x.get('publication_year'),x.get('title'),(x.get('ids') or {}).get('pmid')) for x in rec]}
    print('=====',key,n)
    for x in res[key]['rec']: print(' ',x[2],(x[3] or '')[:130],'|',x[1],x[4])
    time.sleep(1)
save('openalex.json',res)
