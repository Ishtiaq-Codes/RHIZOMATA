import os

filepath = r"C:\Users\user\OneDrive\Desktop\RHIZOMATA\core\templates\core\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("url('{% static 'core/assets/logo.png' %})", "url('{% static \"core/assets/logo.png\" %}')")
content = content.replace("src=\"{% static 'core/assets/cards.png\"", "src=\"{% static 'core/assets/cards.png' %}\"")
content = content.replace("src=\"{% static 'core/assets/board.png\"", "src=\"{% static 'core/assets/board.png' %}\"")
content = content.replace("src=\"{% static 'core/assets/components.png\"", "src=\"{% static 'core/assets/components.png' %}\"")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("fixed")
