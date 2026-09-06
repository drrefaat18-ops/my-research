import concurrent.futures as cf
import json
import pathlib
import urllib.parse
import urllib.request

OUT = pathlib.Path(__file__).parent
PEA = '(palmitoylethanolamide OR palmidrol OR "N-palmitoylethanolamine" OR "palmitoyl ethanolamide")'
queries = {
 'exact_combo_title_abstract': 'TITLE_ABS:('+PEA+' AND prednisolone)',
 'prednisone_title_abstract': 'TITLE_ABS:('+PEA+' AND prednisone)',
 'combo_arthritis_full_index': PEA+' AND prednisolone AND (arthritis OR synovium OR synovial)',
 'pea_baricitinib_title_abstract': 'TITLE_ABS:('+PEA+' AND (baricitinib OR INCB028050))',
 'pea_tacrolimus_title_abstract': 'TITLE_ABS:('+PEA+' AND (tacrolimus OR FK506 OR FK-506))',
 'pea_dusp1_full_index': PEA+' AND (DUSP1 OR MKP1 OR "MKP-1" OR "MAP kinase phosphatase 1")',
 'pea_gilz_full_index': PEA+' AND (GILZ OR TSC22D3)',
 'pea_ferroptosis_full_index': PEA+' AND (ferroptosis OR GPX4 OR ACSL4)',
 'pea_mertk_full_index': PEA+' AND (MERTK OR efferocytosis OR GAS6)',
 'pred_dusp1_title_abstract': 'TITLE_ABS:(prednisolone AND (DUSP1 OR MKP1 OR "MKP-1"))',
 'tacro_dusp1_title_abstract': 'TITLE_ABS:((tacrolimus OR FK506 OR FK-506) AND (DUSP1 OR MKP1 OR "MKP-1"))',
 'bari_dusp1_full_index': '(baricitinib OR INCB028050) AND (DUSP1 OR MKP1 OR "MKP-1")',
}

def run(item):
 name,q=item
 # Bound publication date to the current research date; indexed content still has coverage limits.
 q+=' AND FIRST_PDATE:[1900-01-01 TO 2026-09-06]'
 url='https://www.ebi.ac.uk/europepmc/webservices/rest/search?'+urllib.parse.urlencode({'query':q,'format':'json','pageSize':1000,'resultType':'core'})
 try:
  with urllib.request.urlopen(url,timeout=45) as r: data=json.load(r)
  return name,{'query':q,'url':url,'hitCount':data['hitCount'],'results':data['resultList']['result']}
 except Exception as e:return name,{'query':q,'error':str(e)}

with cf.ThreadPoolExecutor(max_workers=3) as pool: results=dict(pool.map(run,queries.items()))
(OUT/'europepmc-search-ledger.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
for key,row in results.items():
 print(key,row.get('hitCount',row.get('error')))
 for x in row.get('results',[])[:6]: print(' ',x.get('id'),x.get('pubYear'),x.get('title'))
