from playwright.sync_api import sync_playwright
from pathlib import Path
import json, os
p=Path(__file__).resolve().parents[1];out=p/'test-output';results=[];out.mkdir(exist_ok=True)
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path=os.environ.get('CHROME_PATH','/usr/bin/google-chrome'),headless=True,args=['--no-sandbox','--allow-file-access-from-files'])
 for stem in ['index','tech-lab','tech-editorial','farm-market','farm-wholesale']:
  for width in [390,768,1440]:
   page=b.new_page(viewport={'width':width,'height':1000},reduced_motion='reduce');errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
   page.goto((p/'examples'/f'{stem}.html').as_uri());page.screenshot(path=str(out/f'{stem}-{width}-full.png'),full_page=True)
   r=page.evaluate('''() => ({overflow:document.documentElement.scrollWidth>innerWidth,h1:document.querySelectorAll('h1').length,title:document.title,brokenImages:[...document.images].filter(i=>!i.complete||!i.naturalWidth).length,links:[...document.querySelectorAll('a')].map(a=>({href:a.getAttribute('href'),text:a.textContent.trim()})),reduce:getComputedStyle(document.documentElement).scrollBehavior})''')
   bad=[]
   for a in r['links']:
    href=a['href']
    if href.startswith('#') and len(href)>1:
     if not page.locator(href).count():bad.append(href)
    elif not href.startswith(('#','http','mailto:')):
     if not (p/'examples'/href.split('#')[0]).resolve().exists():bad.append(href)
   page.keyboard.press('Tab');focus=page.evaluate('''()=>{const e=document.activeElement;return {tag:e.tagName,outline:getComputedStyle(e).outlineStyle}}''')
   results.append({'page':stem,'width':width,'overflow':r['overflow'],'h1':r['h1'],'brokenImages':r['brokenImages'],'badLinks':bad,'errors':errors,'reducedMotionScrollBehavior':r['reduce'],'firstTabFocus':focus});page.close()
 b.close()
(out/'checks.json').write_text(json.dumps(results,indent=2));print(json.dumps(results,indent=2))
