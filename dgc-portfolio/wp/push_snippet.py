"""Push the interactions snippet (repo copy is the source of truth) to post 132."""
import json, shutil, urllib.request
from mcp import AUTH
from dgc_site import SITE
SRC = '/home/user/new-design/dgc-portfolio/wp/dgc-interactions.html'
s = open(SRC).read(); shutil.copy(SRC, 'dgc-interactions.html')
r = urllib.request.Request(SITE + '/wp-json/wp/v2/elementor_snippet/132', json.dumps({'meta': {'_elementor_code': s}}).encode(), {'Authorization': AUTH, 'Content-Type': 'application/json'}, method='POST')
print('snippet', SITE, urllib.request.urlopen(r).status, len(s))
