import sys
from PIL import Image
images=[]
for arg in sys.argv[1:]:
    images.append(Image.open(arg))

images[0].save(
    "man.gif",
    save_all=True,
    append_images=[images[1]],
    duration=300,
    loop=0
)