import random
import uuid
from PIL import Image, ImageDraw

#Set run_id 
run_id = uuid.uuid1()
print(f'processing run_id: {run_id}')

#Set canvas size and colour mode
image = Image.new('RGBA', (2000, 2000))
width, height = image.size

#Specify canvas properties
x = width / 2 
y = 0
gap = 10
counter = 0
line_length = 0
max_length = 100
line_shape = [(0, 0),(0, 0)]
number_of_lines = 100
draw_image = ImageDraw.Draw(image)

#Drawing loop
for i in range(number_of_lines):
    
    
    if line_length >= max_length :
        
        while line_length > - max_length or line_length > max_length:
            gap = gap + 10
            line_length = line_length - 10
            
            line_shape = [
            (x , y + gap ), 
            (x + line_length , y + gap)]
            
            draw_image.line(
            line_shape,
            fill=(
            255,
            255,
            255
            )
            )
            
    elif line_length <= 0 :  
        
        while line_length < max_length or line_length < - max_length:   
            gap = gap + 10
            line_length = line_length + 10
            
            line_shape = [
            (x , y + gap), 
            (x + line_length , y + gap)]
            
            draw_image.line(
            line_shape,
            fill=(
            255,
            255,
            255
            )
            )
    

    
image.save(f'./.venv/output/lines2/{run_id}.png')