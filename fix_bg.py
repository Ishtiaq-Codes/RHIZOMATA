from PIL import Image
import os

img_path = r'C:\Users\user\OneDrive\Desktop\RHIZOMATA\core\static\core\assets\logo final@3x-8.png'
out_path = r'C:\Users\user\OneDrive\Desktop\RHIZOMATA\core\static\core\assets\logo final@3x-8.webp'

if not os.path.exists(img_path):
    print(f"Error: Could not find {img_path}")
    exit(1)

# Open image and convert to RGBA
img = Image.open(img_path).convert("RGBA")
pixels = img.load()

width, height = img.size

# Assume the top-left pixel is the background color
bg_color = pixels[0, 0]

# Tolerance for background matching (0-255)
# A small tolerance helps if the background isn't perfectly uniform
tolerance = 15

# Iterate through pixels and make the background color transparent
for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        # Check if the pixel matches the background color within tolerance
        if (abs(r - bg_color[0]) <= tolerance and
            abs(g - bg_color[1]) <= tolerance and
            abs(b - bg_color[2]) <= tolerance):
            pixels[x, y] = (r, g, b, 0) # Set alpha to 0 (transparent)

# Save the updated image as WEBP
img.save(out_path, 'WEBP', quality=90, method=6)
print(f"Successfully processed image. Background color {bg_color} made transparent.")
