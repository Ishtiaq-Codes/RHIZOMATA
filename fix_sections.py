import re

with open(r'C:\Users\user\OneDrive\Desktop\RHIZOMATA\core\templates\core\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('\r\n', '\n')

# 1. Update Philosophy Section
old_philosophy = '''<h2 class="concept-heading reveal-up">The Philosophy of Play</h2>
                    <p class="concept-text reveal-up">
                        Each card you hold is a fragment of a larger living tapestry. Every decision ripples outward,
                        reshaping the shared world around you. Play is not merely competitive — it is
                        <strong>meditative, narrative, and deeply symbolic</strong>.
                    </p>'''

new_philosophy = '''<h2 class="concept-heading reveal-up">Destiny is not given.<br>It is chosen.</h2>
                    <p class="concept-text reveal-up" style="font-size: 1.1rem; line-height: 1.8;">
                        Most games use chance — dice, card draws, random events — as the primary engine of excitement. Rhizomata proposes a different approach: <strong>all consequences are visible before every choice is made.</strong><br><br>
                        There are no hidden reveals, no dice, no luck in the result of any decision. The tension is not informational. It is moral. Every person is a hostage to what they have earned.
                    </p>'''
content = content.replace(old_philosophy, new_philosophy)

# 2. Remove the old #features section completely
features_pattern = re.compile(r'<!-- =============================================\n\s*FEATURE CARDS\n\s*============================================= -->\n\s*<section id="features".*?</section>', re.DOTALL)
content = re.sub(features_pattern, '', content)


# 3. HTML for Situation Cards
situation_cards_html = """
    <!-- =============================================
       SITUATION CARDS SHOWCASE
  ============================================= -->
    <section id="situation-cards" aria-labelledby="situation-heading" style="background: var(--bg-dark); padding: 4rem 0 8rem 0; position: relative; z-index: 19;">
        <div class="max-w-7xl mx-auto">
            <div class="text-center" style="margin-bottom: 3.5rem;">
                <span class="section-label reveal-up">The Dilemmas</span>
                <h2 class="section-heading reveal-up" id="situation-heading" style="max-width:600px;margin:0 auto;">
                    Situation <span class="gradient-text">Cards</span>
                </h2>
                <p class="reveal-up" style="color: var(--text-muted); margin-top: 1rem; margin-bottom: 1rem; font-family: 'Inter', sans-serif;">60 unique moral decisions. Both options display their full consequences before you decide.<br>Click to face your fate.</p>
            </div>

            <div class="identity-cards-grid reveal-up">
                
                <!-- Air -->
                <div class="flip-container" style="transition-delay: 0.1s;">
                    <div class="flipper">
                        <div class="back" style="background: #0a0e14;">
                            <img src="{% static 'core/assets/air situation card back.webp' %}" class="card-image" style="object-fit: contain;" loading="lazy" alt="Air Situation Card Back" />
                        </div>
                        <div class="front" style="background: #0a0e14;">
                            <img src="{% static 'core/assets/air stiuation card front.webp' %}" class="card-image" style="object-fit: contain;" loading="lazy" alt="Air Situation Card Front" />
                        </div>
                    </div>
                </div>

                <!-- Earth -->
                <div class="flip-container" style="transition-delay: 0.2s;">
                    <div class="flipper">
                        <div class="back" style="background: #0a0e14;">
                            <img src="{% static 'core/assets/earth situation card back.webp' %}" class="card-image" style="object-fit: contain;" loading="lazy" alt="Earth Situation Card Back" />
                        </div>
                        <div class="front" style="background: #0a0e14;">
                            <img src="{% static 'core/assets/earth situation card front.webp' %}" class="card-image" style="object-fit: contain;" loading="lazy" alt="Earth Situation Card Front" />
                        </div>
                    </div>
                </div>

                <!-- Fire -->
                <div class="flip-container" style="transition-delay: 0.3s;">
                    <div class="flipper">
                        <div class="back" style="background: #0a0e14;">
                            <img src="{% static 'core/assets/fire situation card back.webp' %}" class="card-image" style="object-fit: contain;" loading="lazy" alt="Fire Situation Card Back" />
                        </div>
                        <div class="front" style="background: #0a0e14;">
                            <img src="{% static 'core/assets/fire situation card front.webp' %}" class="card-image" style="object-fit: contain;" loading="lazy" alt="Fire Situation Card Front" />
                        </div>
                    </div>
                </div>

                <!-- Water -->
                <div class="flip-container" style="transition-delay: 0.4s;">
                    <div class="flipper">
                        <div class="back" style="background: #0a0e14;">
                            <img src="{% static 'core/assets/water situation card back.webp' %}" class="card-image" style="object-fit: contain;" loading="lazy" alt="Water Situation Card Back" />
                        </div>
                        <div class="front" style="background: #0a0e14;">
                            <img src="{% static 'core/assets/water situation card front.webp' %}" class="card-image" style="object-fit: contain;" loading="lazy" alt="Water Situation Card Front" />
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- =============================================
       CONTEXT CARD SHOWCASE
  ============================================= -->
    <section id="context-card" aria-labelledby="context-heading" style="background: var(--bg-dark); padding: 4rem 0 8rem 0; position: relative; z-index: 18;">
        <div class="max-w-7xl mx-auto">
            <div class="text-center" style="margin-bottom: 3.5rem;">
                <span class="section-label reveal-up">The Frame</span>
                <h2 class="section-heading reveal-up" id="context-heading" style="max-width:600px;margin:0 auto;">
                    Context <span class="gradient-text">Cards</span>
                </h2>
                <p class="reveal-up" style="color: var(--text-muted); margin-top: 1rem; margin-bottom: 1rem; font-family: 'Inter', sans-serif;">42 unique context modifiers that alter the stakes of your situation.<br>A single scenario shifts depending on the context.</p>
            </div>

            <div class="reveal-up" style="display: flex; justify-content: center;">
                <div class="flip-container" style="max-width: 360px; aspect-ratio: 573 / 615;">
                    <div class="flipper">
                        <div class="back">
                            <img src="{% static 'core/assets/context card back.webp' %}" class="card-image" loading="lazy" alt="Context Card Back" />
                        </div>
                        <div class="front">
                            <img src="{% static 'core/assets/context card front.webp' %}" class="card-image" loading="lazy" alt="Context Card Front" />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

# Insert Situation and Context right before Board Showcase
content = re.sub(r'<!-- =============================================\n\s*BOARD SHOWCASE SECTION', situation_cards_html + '\n    <!-- =============================================\n       BOARD SHOWCASE SECTION', content)

# 4. Update the Board Showcase Section
old_board = '''Four Realms.<br /><span class="gradient-text">One Shared Destiny.</span>
                </h2>
                <p class="reveal-up"
                    style="font-family:'Inter',sans-serif;font-size:0.98rem;color:var(--text-muted);max-width:520px;margin:1.5rem auto 0;line-height:1.85;">
                    The board is a living map of elemental conflict and alliance. Each quadrant breathes with its own
                    art, its own rules, its own rhythm.
                </p>
            </div>

            <!-- Board Image -->
            <div class="flex justify-center reveal-scale">
                <div class="board-img-wrap">
                    <!-- image removed -->
                </div>
            </div>'''

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

content = content.replace(old_board, new_board)

# Remove the old #components section completely
components_pattern = re.compile(r'<!-- =============================================\n\s*COMPONENTS SECTION\n\s*============================================= -->\n\s*<section id="components".*?</section>', re.DOTALL)
content = re.sub(components_pattern, '', content)

with open(r'C:\Users\user\OneDrive\Desktop\RHIZOMATA\core\templates\core\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected new sections successfully.")
