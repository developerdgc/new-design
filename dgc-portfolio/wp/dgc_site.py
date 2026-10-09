"""Which WordPress site the build scripts target: DGC_SITE=main -> digitalgrowthcatalyze.com, else the portfolio staging site."""
import os
MAIN = os.environ.get('DGC_SITE') == 'main'
SITE = 'https://digitalgrowthcatalyze.com' if MAIN else 'https://newportfolio.digitalgrowthcatalyze.com'
MEDIA = 'media-map-main.json' if MAIN else 'media-map.json'
PAGES = 'pages-main.json' if MAIN else 'pages.json'
