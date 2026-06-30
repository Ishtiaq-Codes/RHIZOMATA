import re

filepath = r"C:\Users\user\OneDrive\Desktop\RHIZOMATA\core\templates\core\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace nav-logo-icon CSS
nav_logo_old = """        .nav-logo-icon {
            width: 52px;
            height: 52px;
            flex-shrink: 0;
            background: url('{% static "core/assets/logo.png" %}') no-repeat 50% 49%;
            background-size: 580%;
            filter: drop-shadow(0 0 10px rgba(209, 104, 52, 0.55)) drop-shadow(0 0 4px rgba(101, 65, 108, 0.4));
            transition: filter 0.3s ease, transform 0.3s ease;
        }

        .nav-logo-wrap:hover .nav-logo-icon {
            filter: drop-shadow(0 0 16px rgba(209, 104, 52, 0.8)) drop-shadow(0 0 6px rgba(30, 138, 168, 0.5));
            transform: scale(1.08);
        }"""

nav_logo_new = """        .nav-logo-icon {
            width: 52px;
            height: 52px;
            flex-shrink: 0;
            background: url('{% static "core/assets/logo.svg" %}') center/contain no-repeat;
            transition: transform 0.3s ease;
        }

        .nav-logo-wrap:hover .nav-logo-icon {
            transform: scale(1.08);
        }"""

# Replace footer-logo-icon CSS
footer_logo_old = """        .footer-logo-icon {
            width: 42px;
            height: 42px;
            flex-shrink: 0;
            background: url('{% static "core/assets/logo.png" %}') no-repeat 50% 49%;
            background-size: 580%;
            opacity: 0.9;
            filter: drop-shadow(0 0 8px rgba(209, 104, 52, 0.4));
        }"""

footer_logo_new = """        .footer-logo-icon {
            width: 42px;
            height: 42px;
            flex-shrink: 0;
            background: url('{% static "core/assets/logo.svg" %}') center/contain no-repeat;
            opacity: 0.9;
        }"""

content = content.replace(nav_logo_old, nav_logo_new)
content = content.replace(footer_logo_old, footer_logo_new)

# In case the 50% 49% was different, let's use regex
content = re.sub(r'\.nav-logo-icon\s*\{[^}]+\}', nav_logo_new.split('\n\n')[0], content)
content = re.sub(r'\.nav-logo-wrap:hover \.nav-logo-icon\s*\{[^}]+\}', nav_logo_new.split('\n\n')[1], content)
content = re.sub(r'\.footer-logo-icon\s*\{[^}]+\}', footer_logo_new, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated logo")
