from h import *
import re
H={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36'}
def g(name,url,params=None):
    try:
        r=requests.get(url,params=params,headers=H,timeout=60)
        open('reg_'+name+'.html','w',encoding='utf-8').write(r.text)
        print('=====',name,r.status_code,len(r.text),r.url[:150])
        return r
    except Exception as e:
        print('=====',name,'ERR',e)
# CT.gov v2
for q in ['palmitoylethanolamide AND (arthritis OR rheumatoid OR corticosteroid OR prednisone OR prednisolone OR glucocorticoid)']:
    r=get('https://clinicaltrials.gov/api/v2/studies',{'query.term':q,'pageSize':100,'fields':'NCTId,BriefTitle,Condition,InterventionName,StartDate'})
    j=r.json(); print('===== CTgov',len(j.get('studies',[])))
    for s in j.get('studies',[]):
        p=s['protocolSection']; print(' ',p['identificationModule']['nctId'],p['identificationModule']['briefTitle'][:120],'|',p.get('conditionsModule',{}).get('conditions'))
g('isrctn','https://www.isrctn.com/api/query/format/default',{'q':'palmitoylethanolamide','limit':100})
g('euctr','https://www.clinicaltrialsregister.eu/ctr-search/search',{'query':'palmitoylethanolamide'})
g('anzctr','https://www.anzctr.org.au/TrialSearch.aspx',{'searchTxt':'palmitoylethanolamide','isBasic':'True'})
g('ictrp','https://trialsearch.who.int/Default.aspx',{'SearchAll':'palmitoylethanolamide'})
g('pactr','https://pactr.samrc.ac.za/Search.aspx')
g('chictr','https://www.chictr.org.cn/searchprojEN.html',{'title':'palmitoylethanolamide'})
g('irct','https://irct.behdasht.gov.ir/search/result',{'query':'palmitoylethanolamide'})
