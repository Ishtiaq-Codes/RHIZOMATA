import re
import os

filepath = r"C:\Users\user\OneDrive\Desktop\RHIZOMATA\core\templates\core\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure load static is there
if "{% load static %}" not in content:
    content = "{% load static %}\n" + content

# We have lines like: background: url('assets/logo.png')
# We want: background: url("{% static 'core/assets/logo.png' %}")

# Also replace <img src="assets/..." to <img src="{% static 'core/assets/...' %}"
def replace_asset(match):
    path = match.group(1) # e.g. assets/logo.png
    return f"\"{{% static 'core/{path}' %}}\""

def replace_asset_css(match):
    path = match.group(1) # e.g. assets/logo.png
    return f"url('{{% static \"core/{path}\" %}}')"

content = re.sub(r'url\([\'"]?(assets/[^\'"]+)[\'"]?\)', replace_asset_css, content)
content = re.sub(r'src=[\'"]?(assets/[^\'"]+)[\'"]?', lambda m: f"src=\"{{% static 'core/{m.group(1)}' %}}\"", content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
