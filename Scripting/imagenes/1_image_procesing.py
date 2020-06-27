from PIL import Image, ImageFilter

img = Image.open('./imagenes/original (1).jpg')

#getting information
print(img)
print(img.format)
print(img.size)
print(img.mode)
#print(dir(img))

# adding filters to the image
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png",'png')

#changing colors
gray_image = img.convert('L')
gray_image.save("grey.png",'png')

#rotating images
crookes = img.rotate(180)
#opening to show
gray_image.show()
#resizing
resize = img.resize((300,300))
resize.show()

#taking a region from an image
box = (100,100,400,400)
region = img.crop(box)
region.show()


