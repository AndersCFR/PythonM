import sys
import os
from PIL import Image

# grab the first and second argument, in the comand line you write imegens/ new/
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#check is new/ exists, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop through imagenes
#convert images to png
#save the new imagenes on the new folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png','png')


