import random
import uuid
from PIL import Image, ImageDraw

run_id = uuid.uuid1()

print(f'processing run_id: {run_id}')

image = Image.new('RGBA', (2000, 2000))
width, height = image.size

number_of_lines = 1000000

#Rectangle starting position point
x = 0
y = 0
gap = 0
counter = 1
line_length = height
draw_image = ImageDraw.Draw(image)
for i in range(number_of_lines):
    
    counter = counter + 1 
    line_length = line_length - 100
    
    if line_length == 0:
        line_length = 2000

         
    line_shape = [
        (x + gap + counter * 2, y), 
        (x + gap + counter * 2 , y + line_length)]
    
    gap = 1 + gap
    draw_image.line(
        line_shape,
        fill=(
            255,
            255,
            255
        )
    )
image.save(f'./.venv/output/lines/{run_id}.png')