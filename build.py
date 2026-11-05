# Rebuild index.html from src.html, embedding assets/N.webp
import re, base64
s = open('src.html').read()
out = re.sub(r'\{\{img:(\d+)\}\}', lambda m: 'data:image/webp;base64,' + base64.b64encode(open(f'assets/{m.group(1)}.webp','rb').read()).decode(), s)
open('index.html','w').write(out)
