# Implement the histogram equalization technique 
# discussed in Section 3.3.1.

from PIL import Image, ImageDraw

# for each grey level r, count the corresponding s
def histogram_equalization(r, MN, n):
	L = 256
	sum = 0

	for i in range(r):
		sum += n[i]

	s = (L-1) * sum / MN

	return s

# count the frequency of each grey level
# and return an array 
def count_n(data, width, height):
	n = [0] * 256

	for i in range(width):
		for j in range(height):
			n[data[i,j]] += 1

	return n

# open an image and get its information
im = Image.open('Fig0222(a)(face).tif')
data = im.load()
width, height = im.size
MN =  width * height

# new two blank images for rewrite and downsampling
HEImage = Image.new('L',(width, height), 'white')

# count the frequency of each grey level
n = count_n(data, width, height)

# draw the new HE image
draw = ImageDraw.Draw(HEImage)

for i in range(width):
	for j in range(height):
			# for each pixel, find its corresponding grey level after HE
			p = histogram_equalization(data[i, j], MN, n)
			draw.point((i, j), p)

#save the output files
HEImage.save('HEImage_c.bmp', format='BMP')
