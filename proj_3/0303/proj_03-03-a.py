# Write program to perform spatial filtering of an 
# image (see Section 3.4 regarding implementation). 
# You can fix the size of the spatial mask at 3 x 3, 
# but the coefficients need to be variables that can 
# be input into your program. This project is generic, 
# in the sense that it will be used in other projects
# to follow.

from PIL import Image, ImageDraw

# count the new grey level in position(i,j)
def spatial_filtering(i, j):
	# create a s*s array to represent the pixels that have
	# influence on position(i,j)'s new grey level
	array = [[(0,0)] * s ] * s
	average = 0

	# count the coordinate of the s*s pixels
	for a in range(s):
		for b in range(s):
			x = i + dis[a]
			y = j + dis[b]

			# if the pixel's position is out of the image's range
			# set it to the boundary's value
			if(x < 0):
				x = 0
			if(y < 0):
				y = 0
			if(x >= width):
				x = width - 1
			if(y >= height):
				y = height - 1

			# keep the array for better understanding, it can be deleted	
			array[a][b] = ( x, y )
			#count the average of the s*s pixels' grey level
			average += data[array[a][b]]

	average = average / (s * s)

	#return average
	return average

# open an image and get its information
im = Image.open('Fig0219(rose1024).tif')
data = im.load()
width, height = im.size
MN =  width * height

# new two blank images for rewrite and downsampling
resultImage = Image.new('L',(width, height), 'white')

# count the frequency of each grey level
s = input('please input size: ')
dis = [0] * s

for c in range(s):
		dis[c] =  c - (s / 2)

# draw the new HE image
draw = ImageDraw.Draw(resultImage)

#width = height = 10
for i in range(width):
	for j in range(height):
			# for each pixel, find its corresponding grey level after HE
			p = spatial_filtering(i, j)
			draw.point((i, j), p)

filename = 'SFImage_rose_blursize=' + str(s) + '.bmp'

#save the output files
resultImage.save(filename, format='BMP')
