from PIL import Image
import os

img_path = r'C:\Users\user\OneDrive\Desktop\RHIZOMATA\core\static\core\assets\logo final@3x-8.png'
out_path = r'C:\Users\user\OneDrive\Desktop\RHIZOMATA\core\static\core\assets\logo final@3x-8.webp'

if os.path.exists(img_path):
    img = Image.open(img_path)
    img.save(out_path, 'WEBP', quality=85, method=6)
    print("Logo converted successfully.")
else:
    print("Logo not found.")

# Update index.html
html_path = r'C:\Users\user\OneDrive\Desktop\RHIZOMATA\core\templates\core\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('logo.svg', 'logo final@3x-8.webp')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html updated.")
