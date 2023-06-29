import random
import uuid
from PIL import Image, ImageDraw

run_id = uuid.uuid1()

print(f'processing run_id: {run_id}')

image = Image.new('RGBA', (2000, 2000))
width, height = image.size

number_of_squares = random.randint(1000, 5000)

#Rectangle starting position point
rectangle_x = 0
rectangle_y = 0
counter = 0
gap = 10
draw_image = ImageDraw.Draw(image)
for i in range(number_of_squares):
    counter = counter + 1
    gap_size = random.randint(1, 10)
    gap = gap + gap_size
    rectangle = random.randint(10,100)
    rectangle_x = rectangle_x + random.randint(1,10)
    rectangle_y = random.randint(0,2000)
    rectangle_shape = [
        (rectangle_x + gap, rectangle_y), 
        (rectangle_x + rectangle, rectangle_y + rectangle)]
    
    draw_image.rectangle(
        rectangle_shape,
        fill=(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    )
image.save(f'./.venv/output/squares/{run_id}.png')