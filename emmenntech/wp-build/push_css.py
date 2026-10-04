"""Push site.css into the Elementor kit custom CSS."""
import json, subprocess, os
css = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site.css')).read()
json.dump({"post_id": 6, "settings": {"custom_css": css}}, open('/tmp/kitcss.json', 'w'))
print(subprocess.run(["python3", "mcp.py", "elementor-update-page-settings", "@/tmp/kitcss.json"], capture_output=True, text=True).stdout[:160])
