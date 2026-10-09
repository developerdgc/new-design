"""Which WordPress site the build scripts target:
DGC_SITE=main -> digitalgrowthcatalyze.com, DGC_SITE=portfolio -> portfolio.digitalgrowthcatalyze.com (live portfolio, migrated from staging),
unset -> newportfolio staging."""
import os
_S = os.environ.get('DGC_SITE', '')
MAIN = _S == 'main'
SITE = {'main': 'https://digitalgrowthcatalyze.com', 'portfolio': 'https://portfolio.digitalgrowthcatalyze.com'}.get(_S, 'https://newportfolio.digitalgrowthcatalyze.com')
MEDIA = {'main': 'media-map-main.json', 'portfolio': 'media-map-portfolio.json'}.get(_S, 'media-map.json')
PAGES = {'main': 'pages-main.json', 'portfolio': 'pages-portfolio.json'}.get(_S, 'pages.json')
