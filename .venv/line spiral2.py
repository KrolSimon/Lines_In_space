import uuid
import math
from PIL import Image, ImageDraw


run_id = uuid.uuid1()
print(f'processing run_id: {run_id}')

x = 1000
y = 1000
image = Image.new('RGBA', (2000, 2000))
draw = ImageDraw.Draw(image)
width, height = image.size
line_shape = [(0, 0),(0, 0)]
hypotenuse = 500
count = 1
for i in range(100): 
    adjacent = hypotenuse * math.cos(count)
    opposite = hypotenuse * math.sin(count)
    count = count + 10
    line_shape = [(x,y),(x + opposite, y + adjacent + hypotenuse)]
    draw.line(
        line_shape,
        fill=(
        255,
        255,
        255
        )
        )
    
image.save(f'./.venv/output/linespiral2/{run_id}.png')

    