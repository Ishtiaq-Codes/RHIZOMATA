import re

html_path = r'C:\Users\user\OneDrive\Desktop\RHIZOMATA\core\templates\core\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the letterboxing backgrounds and object-fit overrides
content = content.replace('style="background: #0a0e14;"', '')
content = content.replace('style="object-fit: contain;"', '')

# 2. Add aspect ratios to the specific cards
# We can find the Situation Cards section and replace the flip-container divs
# Air
content = content.replace(
    '<!-- Air -->\n                <div class="flip-container"',
    '<!-- Air -->\n                <div class="flip-container" style="aspect-ratio: 627/864;"'
)
# Water
content = content.replace(
    '<!-- Water -->\n                <div class="flip-container"',
    '<!-- Water -->\n                <div class="flip-container" style="aspect-ratio: 627/864;"'
)
# Earth
content = content.replace(
    '<!-- Earth -->\n                <div class="flip-container"',
    '<!-- Earth -->\n                <div class="flip-container" style="aspect-ratio: 627/864;"'
)
# Fire
content = content.replace(
    '<!-- Fire -->\n                <div class="flip-container"',
    '<!-- Fire -->\n                <div class="flip-container" style="aspect-ratio: 627/864;"'
)
# Context
content = content.replace(
    '<!-- Context -->\n                <div class="flip-container"',
    '<!-- Context -->\n                <div class="flip-container" style="aspect-ratio: 573/615;"'
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Situation and Context cards aspect ratios fixed.")
