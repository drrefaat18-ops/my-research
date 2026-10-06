import re,html,sys,subprocess,time,urllib.parse
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
def run(q,pages=2):
    print("\n=====",q)
    for p in range(pages):
        url="https://scholar.google.com/scholar?hl=en&num=20&start=%d&q=%s"%(p*20,urllib.parse.quote_plus(q))
        t=subprocess.run(["curl","-s","-m","40","-A",UA,url],capture_output=True).stdout.decode('utf-8','ignore')
        if 'unusual traffic' in t or 'gs_captcha' in t: print("CAPTCHA"); return
        if p==0:
            m=re.search(r'About ([\d,]+) results|([\d,]+) results?',t); print('count', m.group(0) if m else '?')
        blocks=re.findall(r'<div class="gs_ri">(.*?)</div></div>',t,re.S)
        for b in blocks:
            h=re.search(r'<h3 class="gs_rt"[^>]*>(.*?)</h3>',b,re.S); a=re.search(r'<div class="gs_a">(.*?)</div>',b,re.S)
            l=re.search(r'<a [^>]*href="([^"]+)"',h.group(1)) if h else None
            print(' -',html.unescape(re.sub('<[^>]+>','',h.group(1) if h else ''))[:150],'||',html.unescape(re.sub('<[^>]+>','',a.group(1) if a else ''))[:110],'||',(l.group(1) if l else '')[:120])
        time.sleep(4)
for q in sys.argv[1:]: run(q); time.sleep(5)
