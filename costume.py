import sys

from PIL import Image

if len(sys.argv) != 3:
    sys.exit("Usage: python costume.py image1 image2")

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
"costume1.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)