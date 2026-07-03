import re
import os

templates_dir = r'C:\Users\user\OneDrive\Desktop\RHIZOMATA\core\templates\core'
index_path = os.path.join(templates_dir, 'index.html')
base_path = os.path.join(templates_dir, 'base.html')

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Extract Top Part (Head, Nav, Mobile Menu)
top_match = re.search(r'(.*?<!-- Mobile Menu -->.*?</div>)\s*<!-- =============================================\s*HERO SECTION', html, re.DOTALL)
top_content = top_match.group(1) if top_match else ""

# 2. Extract Bottom Part (Footer, Scripts)
bottom_match = re.search(r'(<!-- =============================================\s*FOOTER.*?</html>)', html, re.DOTALL)
bottom_content = bottom_match.group(1) if bottom_match else ""

# 3. Extract Middle Part (The actual page content: Hero, Concept, Board Showcase, Cards, Final CTA)
middle_match = re.search(r'(<!-- =============================================\s*HERO SECTION.*?</section>)\s*<!-- =============================================\s*FOOTER', html, re.DOTALL)
middle_content = middle_match.group(1) if middle_match else ""

if top_content and bottom_content and middle_content:
    # Build base.html
    base_html = top_content + "\n\n    <main>\n        {% block content %}\n        {% endblock %}\n    </main>\n\n    " + bottom_content
    
    # Update Nav Links in base.html
    base_html = base_html.replace('href="#concept"', 'href="{% url \'how_to_play\' %}"')
    base_html = base_html.replace('href="#features"', 'href="{% url \'preview\' %}"')
    base_html = base_html.replace('href="#final-cta"', 'href="{% url \'order\' %}"')
    
    # Build new index.html
    new_index_html = "{% extends 'core/base.html' %}\n{% load static %}\n\n{% block content %}\n" + middle_content + "\n{% endblock %}"
    
    with open(base_path, 'w', encoding='utf-8') as f:
        f.write(base_html)
        
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_index_html)
        
    print("Refactoring successful!")
else:
    print("Failed to match sections.")
    if not top_content: print("Top missing")
    if not middle_content: print("Middle missing")
    if not bottom_content: print("Bottom missing")
