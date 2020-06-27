from PIL import Image, ImageFilter

img = Image.open('./original.jpg')
new_img = img.resize((400,400))
new_img.save('resizedimage.jpg')

#this mwthod respects the relations
img.thumbnail((400,200))
img.save('otherimage.jpg')
