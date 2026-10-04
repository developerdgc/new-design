#!/bin/bash
# snap.sh <page-key> <width> <outprefix>  -> screenshots of the preview, split into 4000px chunks
cd "$(dirname "$0")"
ID=$(python3 -c "import json;print(json.load(open('pages.json'))['$1'])")
URL=$(python3 mcp.py elementor-create-preview-link "{\"post_id\":$ID}" | python3 -c "import json,sys;print(json.load(sys.stdin)['url'])")
NODE_PATH=$(npm root -g) timeout 500 node shot.js "$URL" /tmp/$3.png $2 1 2>&1 | tail -1
H=$(identify -format %h /tmp/$3.png); W=$2; CH=$(( W<700 ? 2600 : 4000 )); n=$(( (H+CH-1)/CH ))
rm -f /tmp/$3_*.jpg; for i in $(seq 0 $((n-1))); do convert /tmp/$3.png -crop ${W}x${CH}+0+$((i*CH)) -resize $([ $W -lt 700 ] && echo 60 || echo 45)% /tmp/$3_$i.jpg; done; ls /tmp/$3_*.jpg | tr '\n' ' '
