import json,subprocess,sys
# usage: up.py uuid:file ...
for arg in sys.argv[1:]:
    uu,f=arg.split(':',1)
    ct='image/png' if f.endswith('png') else 'image/jpeg'
    r=subprocess.run(['curl','-sS','-X','POST','-H','Content-Type: '+ct,'--data-binary','@'+f,f'https://mcp.figma.com/mcp/upload/{uu}/submit?scaleMode=FILL&currentPageId=0%3A1'],capture_output=True,text=True)
    print(f[-16:], r.stdout[:60])
