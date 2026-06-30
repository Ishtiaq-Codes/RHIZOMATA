import re

filepath = r"C:\Users\user\OneDrive\Desktop\RHIZOMATA\core\templates\core\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix nav-logo-icon
nav_block_start = "        /* Crop into just the icon portion of logo.png (removes empty dark space) */"
nav_block_end = """        /* =============================================
       FEATURE CARD — REAL IMAGE BACKGROUNDS
    ============================================= */"""

correct_nav_css = """        /* Crop into just the icon portion of logo.png (removes empty dark space) */
        .nav-logo-icon {
            width: 52px;
            height: 52px;
            flex-shrink: 0;
            background: url('{% static "core/assets/logo.svg" %}') center/contain no-repeat;
            transition: transform 0.3s ease;
        }

        .nav-logo-wrap:hover .nav-logo-icon {
            transform: scale(1.08);
        }

"""

# We need to find the start and end and replace
start_idx = content.find(nav_block_start)
end_idx = content.find(nav_block_end)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + correct_nav_css + content[end_idx:]
else:
    print("Could not find nav logo block")

# Fix footer-logo-icon
footer_block_start = "        /* Footer logo image */"
footer_block_end = "    </style>"

correct_footer_css = """        /* Footer logo image */
        .footer-logo-wrap {
            display: flex;
            align-items: center;
            gap: 0.7rem;
        }

        .footer-logo-icon {
            width: 42px;
            height: 42px;
            flex-shrink: 0;
            background: url('{% static "core/assets/logo.svg" %}') center/contain no-repeat;
            opacity: 0.9;
        }
"""

f_start_idx = content.find(footer_block_start)
f_end_idx = content.find(footer_block_end)

if f_start_idx != -1 and f_end_idx != -1:
    content = content[:f_start_idx] + correct_footer_css + content[f_end_idx:]
else:
    print("Could not find footer logo block")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed CSS parsing errors")
