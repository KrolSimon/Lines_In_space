import uuid
import math
from PIL import Image, ImageDraw
import random

run_id = uuid.uuid1()
print(f'processing run_id: {run_id}')


image = Image.new('RGBA', (2000, 2000))
draw = ImageDraw.Draw(image)
width, height = image.size
line_shape = [(0, 0),(0, 0)]
count = random.randint(100,500)
def buildTriangle(x, y, v, h):
    h = x + h
    v = y + v
    line_shape = [(x,y),(x,h)]
    draw.line(
        line_shape,
        fill=(
        random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255)
        )
        )
    line_shape = [(x,y),(v, y)]
    draw.line(
        line_shape,
        fill=(
        random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255)
        )
        )
    line_shape = [(x,h),(v,y)]
    draw.line(
        line_shape,
        fill=(
        random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255)
        )
        )
for i in range(count):
    v = random.randint(-500,500)
    h = random.randint(-500,0)
    x = random.randint(0,2000)
    y = random.randint(0,2000)
    buildTriangle(x,y,v,h)
    
image.save(f'./.venv/output/triangles/{run_id}.png')