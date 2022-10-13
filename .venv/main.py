import random
import uuid
from PIL import Image, ImageDraw

run_id = uuid.uuid1()

print(f'processing run_id: {run_id}')

image = Image.new('RGBA', (2000, 2000))
width, height = image.size

number_of_squares = random.randint(10000, 500000)

#Rectangle starting position point
rectangle_x = 1000
rectangle_y = 0
counter = 0
draw_image = ImageDraw.Draw(image)
for i in range(number_of_squares):
    counter = counter + 1
    gap = random.randint(1, 10)
    

        
    rectangle_size = 50
    rectangle_width = rectangle_size
    rectangle_height = rectangle_size
    
    if rectangle_y + rectangle_height > 2000:
        rectangle_y = counter
        rectangle_x = 0
        
    
    if rectangle_x + rectangle_width > 2000 :
        rectangle_x = counter
        rectangle_y = 0
        
        
    rectangle_x = rectangle_x + gap
    rectangle_y = rectangle_y + gap

       
    rectangle_shape = [
        (rectangle_x, rectangle_y), 
        (rectangle_x + rectangle_width, rectangle_y + rectangle_height)]
    
    draw_image.rectangle(
        rectangle_shape,
        fill=(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    )
image.save(f'./.venv/output/squares/{run_id}.png')