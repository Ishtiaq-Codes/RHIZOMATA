import re

with open(r'C:\Users\user\OneDrive\Desktop\RHIZOMATA\core\templates\core\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

css = """
        /* --- Identity Cards Flip CSS --- */
        .identity-cards-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 2rem;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 1.5rem;
            perspective: 1500px;
        }

        @media (min-width: 640px) {
            .identity-cards-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (min-width: 1024px) {
            .identity-cards-grid {
                grid-template-columns: repeat(4, 1fr);
            }
        }

        .flip-container {
            width: 100%;
            aspect-ratio: 657 / 1123;
            cursor: pointer;
            perspective: 1500px;
        }

        .flipper {
            position: relative;
            width: 100%;
            height: 100%;
            transition: transform 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            transform-style: preserve-3d;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            border-radius: 14px;
        }

        .flip-container:hover .flipper {
            box-shadow: 0 15px 40px rgba(209, 104, 52, 0.2);
            transform: translateY(-5px);
        }

        .flip-container.flipped .flipper {
            transform: rotateY(180deg) translateY(-5px);
        }

        .front, .back {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            -webkit-backface-visibility: hidden;
            backface-visibility: hidden;
            border-radius: 14px;
            overflow: hidden;
        }

        .front {
            transform: rotateY(180deg);
        }

        .back {
            transform: rotateY(0deg);
        }

        .card-image {
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 14px;
            pointer-events: none;
        }
"""

content = content.replace("    </style>", css + "\n    </style>")

html = """
    <!-- =============================================
       IDENTITY CARDS SHOWCASE
  ============================================= -->
    <section id="identity-cards" aria-labelledby="identity-heading" style="background: var(--bg-dark); padding: 4rem 0 8rem 0; position: relative; z-index: 20;">
        <div class="max-w-7xl mx-auto">
            <div class="text-center mb-12">
                <span class="section-label reveal-up">The Elements</span>
                <h2 class="section-heading reveal-up" id="identity-heading" style="max-width:600px;margin:0 auto;">
                    Identity <span class="gradient-text">Cards</span>
                </h2>
                <p class="reveal-up" style="color: var(--text-muted); margin-top: 1rem; font-family: 'Inter', sans-serif;">Click a card to reveal its true identity.</p>
            </div>

            <div class="identity-cards-grid reveal-up">
                
                <!-- Air Card -->
                <div class="flip-container">
                    <div class="flipper">
                        <div class="back">
                            <img src="{% static 'core/assets/identity card back.webp' %}" class="card-image" loading="lazy" alt="Identity Card Back" />
                        </div>
                        <div class="front">
                            <img src="{% static 'core/assets/identity card front (air).webp' %}" class="card-image" loading="lazy" alt="Identity Card Air" />
                        </div>
                    </div>
                </div>

                <!-- Earth Card -->
                <div class="flip-container" style="transition-delay: 0.1s;">
                    <div class="flipper">
                        <div class="back">
                            <img src="{% static 'core/assets/identity card back.webp' %}" class="card-image" loading="lazy" alt="Identity Card Back" />
                        </div>
                        <div class="front">
                            <img src="{% static 'core/assets/identity card front (earth).webp' %}" class="card-image" loading="lazy" alt="Identity Card Earth" />
                        </div>
                    </div>
                </div>

                <!-- Fire Card -->
                <div class="flip-container" style="transition-delay: 0.2s;">
                    <div class="flipper">
                        <div class="back">
                            <img src="{% static 'core/assets/identity card back.webp' %}" class="card-image" loading="lazy" alt="Identity Card Back" />
                        </div>
                        <div class="front">
                            <img src="{% static 'core/assets/identity card front (fire).webp' %}" class="card-image" loading="lazy" alt="Identity Card Fire" />
                        </div>
                    </div>
                </div>

                <!-- Water Card -->
                <div class="flip-container" style="transition-delay: 0.3s;">
                    <div class="flipper">
                        <div class="back">
                            <img src="{% static 'core/assets/identity card back.webp' %}" class="card-image" loading="lazy" alt="Identity Card Back" />
                        </div>
                        <div class="front">
                            <img src="{% static 'core/assets/identity card front (water).webp' %}" class="card-image" loading="lazy" alt="Identity Card Water" />
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>
"""

# Insert right before the Board Showcase section
content = content.replace("    <!-- =============================================\\n       BOARD SHOWCASE SECTION", html + "\\n    <!-- =============================================\\n       BOARD SHOWCASE SECTION")

js = """
            /* --- Identity Cards Flip Logic --- */
            document.querySelectorAll('.flip-container').forEach(card => {
                card.addEventListener('click', function() {
                    this.classList.toggle('flipped');
                });
            });
"""

content = content.replace("        }());\\n    </script>", js + "\\n        }());\\n    </script>")

with open(r'C:\Users\user\OneDrive\Desktop\RHIZOMATA\core\templates\core\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done injecting Identity Cards code.")
