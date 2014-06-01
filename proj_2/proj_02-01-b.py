# Write a program to generate a test pattern image consisting 
# of a gray scale wedge of size 256 x 256, whose first column 
# is all 0's, the next column is all 1's, and so on, with the 
# last column being 255's. 
# Print this image using your gray-scale printing program.

from PIL import Image, ImageDraw

width = height = 256

# new two blank images
halftoningImage = Image.new('L',(width, height), 'white')

draw = ImageDraw.Draw(halftoningImage)

for i in range(width):
	for j in range(height):
			draw.point((i, j), i)

#save the output files
halftoningImage.save('halftoningImage_b.bmp', format='BMP')
