# Print book Figs. 2.22(a) through (c) using your gray-scale 
# printing program. Do your results agree with the conclusions 
# arrived at in the text in pgs. 64-65 and Fig. 2.23? Explain. 
# You can download the required figures from the book web site.

'''Here i dont use the fig in book, and use the lena pic instead'''

from PIL import Image, ImageDraw

# the program is similar as 02-01-a
im = Image.open('Fig0222(a)(face).tif')
data = im.load()
width, height = im.size

halftoningImage = Image.new('L',(width * 3, height * 3), 'white')

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

d = 255/9

draw = ImageDraw.Draw(halftoningImage)

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
halftoningImage.save('halftoningImage_lena.bmp', format='BMP')
