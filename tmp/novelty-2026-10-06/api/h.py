import requests, json, time, sys, urllib.parse
UA={'User-Agent':'novelty-search/1.0 (mailto:drrefaat18@gmail.com)'}
def get(url, params=None, tries=5, wait=4):
    for i in range(tries):
        try:
            r=requests.get(url,params=params,headers=UA,timeout=60)
        except Exception as e:
            print('ERR',e); time.sleep(wait); continue
        if r.status_code==429 or r.status_code>=500:
            print('HTTP',r.status_code,'retry',i); time.sleep(wait*(i+1)); continue
        return r
    return r
def save(name,obj):
    json.dump(obj,open(name,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
def pubmed(q, extra=None):
    p={'db':'pubmed','term':q,'retmax':200,'retmode':'json'}
    if extra: p.update(extra)
    r=get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi',p).json()
    ids=r['esearchresult']['idlist']; n=r['esearchresult']['count']
    out=[]
    if ids:
        s=get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi',{'db':'pubmed','id':','.join(ids),'retmode':'json'}).json()['result']
        for i in ids:
            d=s.get(i,{}); out.append((i,d.get('pubdate',''),d.get('title',''),d.get('source','')))
    return n,out
def epmc(q, size=200):
    r=get('https://www.ebi.ac.uk/europepmc/webservices/rest/search',{'query':q,'format':'json','pageSize':size,'resultType':'lite'}).json()
    out=[(x.get('id'),x.get('source'),x.get('pmid',''),x.get('doi',''),x.get('pubYear'),x.get('title'),x.get('journalTitle','')) for x in r.get('resultList',{}).get('result',[])]
    return r.get('hitCount'),out
