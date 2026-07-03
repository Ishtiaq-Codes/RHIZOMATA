import re

with open(r'C:\Users\user\OneDrive\Desktop\RHIZOMATA\core\templates\core\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the entire text column and the visual column
old_section = re.search(r'<!-- Text -->.*?<!-- Visual.*?</div>\s*</div>\s*</div>', content, re.DOTALL)

if old_section:
    new_section = """<!-- Text -->
                <div style="max-width: 600px;">
                    <span class="section-label reveal-up">The Philosophy</span>
                    <h2 class="section-heading reveal-up" id="concept-heading">
                        Destiny is not given.<br />
                        <span class="gradient-text">It is chosen.</span>
                    </h2>
                    <div class="concept-divider reveal-up" aria-hidden="true"></div>

                    <p class="concept-text reveal-up" style="font-size: 1.1rem; line-height: 1.8;">
                        Most games use chance — dice, card draws, random events — as the primary engine of excitement. <strong>Rhizomata</strong> proposes a different approach: <strong>all consequences are visible before every choice is made.</strong>
                    </p>
                    <br />
                    <p class="concept-text reveal-up" style="font-size: 1.1rem; line-height: 1.8;">
                        There are no hidden reveals, no dice, no luck in the result of any decision. The tension is not informational. It is moral. Every person is a hostage to what they have earned.
                    </p>

                    <p class="concept-author reveal-up" style="margin-top:2.5rem; color: var(--color-orange);">— Created by Amna Noor</p>
                </div>

                <!-- The right side is intentionally left empty so the animated node diagram (SVG) can take center stage as the background aesthetic. -->
            </div>"""
    
    content = content.replace(old_section.group(0), new_section)
    
    with open(r'C:\Users\user\OneDrive\Desktop\RHIZOMATA\core\templates\core\index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Concept section updated.")
else:
    print("Could not find the concept section.")
