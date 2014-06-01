# Write a halftoning computer program for printing gray-scale images 
# based on the dot patterns just discussed. Your program must be able 
# to scale the size of an input image so that it does not exceed the 
# area available in a sheet of size 8.5 x 11 inches (21.6 x 27.9 cm). 
# Your program must also scale the gray levels of the input image to 
# span the full halftoning range.

from PIL import Image, ImageDraw

# open an image and get its information
im = Image.open('Fig0222(b)(cameraman).tif')
data = im.load()
width, height = im.size

# new two blank images for halftoning
halftoningImage = Image.new('L',(width * 3, height * 3), 'white')

# the color array represnets nine patterns
# corresponding to the question description
color = [[] * 9 ] * 10
color[0] = [0,0,0,0,0,0,0,0,0]
color[1] = [0,255,0,0,0,0,0,0,0]
color[2] = [0,255,0,0,0,0,0,0,255]
color[3] = [255,255,0,0,0,0,0,0,255]
color[4] = [255,255,0,0,0,0,255,0,255]
color[5] = [255,255,255,0,0,0,255,0,255]
color[6] = [255,255,255,0,0,255,255,0,255]
color[7] = [255,255,255,0,0,255,255,255,255]
color[8] = [255,255,255,255,0,255,255,255,255]
color[9] = [255,255,255,255,255,255,255,255,255]

# divide the grey level interval into 9 parts 
# which suit for the nine replacement patterns
d = 255/9

# draw the answer image
draw = ImageDraw.Draw(halftoningImage)

# for each pixel count its correspond pattern and
# draw the pattern in the image with new size
for i in range(width):
	for j in range(height):
			p = data[i, j]/d
			c = color[p]
			draw.point((i * 3, j * 3), c[0])
			draw.point((i * 3 + 1, j * 3), c[1])
			draw.point((i * 3 + 2, j * 3), c[2])
			draw.point((i * 3, j * 3 + 1), c[3])
			draw.point((i * 3 + 1, j * 3 + 1), c[4])
			draw.point((i * 3 + 2, j * 3 + 1), c[5])
			draw.point((i * 3, j * 3 + 2), c[6])
			draw.point((i * 3 + 1, j * 3 + 2), c[7])
			draw.point((i * 3 + 2, j * 3 + 2), c[8])

#save the output files
halftoningImage.save('halftoningImage_a.bmp', format='BMP')
