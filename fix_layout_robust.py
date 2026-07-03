import re

with open(r'C:\Users\user\OneDrive\Desktop\RHIZOMATA\core\templates\core\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Philosophy Section
# In origin/main, the philosophy section text is there. Let's just replace the exact tags.
content = re.sub(
    r'<h2 class="concept-heading reveal-up">The Philosophy of Play</h2>\s*<p class="concept-text reveal-up">.*?</p>',
    '''<h2 class="concept-heading reveal-up">Destiny is not given.<br>It is chosen.</h2>
                    <p class="concept-text reveal-up" style="font-size: 1.1rem; line-height: 1.8;">
                        Most games use chance — dice, card draws, random events — as the primary engine of excitement. Rhizomata proposes a different approach: <strong>all consequences are visible before every choice is made.</strong><br><br>
                        There are no hidden reveals, no dice, no luck in the result of any decision. The tension is not informational. It is moral. Every person is a hostage to what they have earned.
                    </p>''',
    content,
    flags=re.DOTALL
)

# 2. Remove the #features section completely
content = re.sub(r'<!-- =============================================\s*FEATURE CARDS\s*============================================= -->\s*<section id="features".*?</section>', '', content, flags=re.DOTALL)

# 3. Update the Board Showcase Section
# Replace the text inside it and the image
new_board = '''The Arena.<br /><span class="gradient-text">Your Path to Becoming.</span>
                </h2>
                <p class="reveal-up"
                    style="font-family:'Inter',sans-serif;font-size:1.05rem;color:var(--text-muted);max-width:700px;margin:1.5rem auto 0;line-height:1.85;">
                    Every player controls two pawns simultaneously: a <strong>Stability Pawn</strong> moving ahead for grounded, restrained choices — and an <strong>Ambition Pawn</strong> moving ahead for bold, risky choices. What happens on the board reflects the character you are becoming.
                </p>
            </div>

            <!-- Board Image -->
            <div class="flex justify-center reveal-scale">
                <div style="max-width: 900px; width: 100%; border-radius: 12px; overflow: hidden; box-shadow: 0 20px 60px rgba(0,0,0,0.6);">
                    <img src="{% static 'core/assets/game board.webp' %}" alt="Rhizomata Game Board" style="width: 100%; height: auto; display: block;" loading="lazy" />
                </div>
            </div>'''

content = re.sub(
    r'Four Realms\.<br /><span class="gradient-text">One Shared Destiny\.</span>\s*</h2>\s*<p class="reveal-up"[\s\S]*?</p>\s*</div>\s*<!-- Board Image -->\s*<div class="flex justify-center reveal-scale">\s*<div class="board-img-wrap">.*?</div>\s*</div>',
    new_board,
    content,
    flags=re.DOTALL
)

# 4. Remove the #components section completely
content = re.sub(r'<!-- =============================================\s*COMPONENTS SECTION\s*============================================= -->\s*<section id="components".*?</section>', '', content, flags=re.DOTALL)

with open(r'C:\Users\user\OneDrive\Desktop\RHIZOMATA\core\templates\core\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed the corrupted layout successfully.")
