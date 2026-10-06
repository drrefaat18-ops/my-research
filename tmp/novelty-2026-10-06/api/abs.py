from h import *
ids=sys.argv[1]
r=get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi',{'db':'pubmed','id':ids,'rettype':'abstract','retmode':'text'})
open('abs_'+ids.replace(',','_')[:60]+'.txt','w',encoding='utf-8').write(r.text)
print(r.text)
