# write an enlarge function to expand the area of images

from PIL import Image, ImageDraw

# the function takes two arguments
# the first argument is the enlarge size
# the second argument is the 2 * 2 array of the original image
# the function return the 2 * 2 array of the enlarged image
def enlarge_image(s, origin_image):
	width = len(origin_image)
	height = len(origin_image[0])
	enlarged_width = 2 * s + width
	enlarged_height = 2 * s + height
	enlarged_image = [[255 for i in range(enlarged_height)] for j in range(enlarged_width)]
	
	for x in range(width):
		for y in range(height):
			enlarged_image[x + s][y + s] = origin_image[x][y]

	for x in range(width):
		for y in range(s):
			enlarged_image[x + s][y] = origin_image[x][y]
			enlarged_image[x + s][enlarged_height - y - 1] = origin_image[x][height - y - 1]

	for x in range(s):
		for y in range(height):
			enlarged_image[x][y + s] = origin_image[x][y]
			enlarged_image[enlarged_width - x - 1][y + s] = origin_image[width - x - 1][y]

	for x in range(s):
		for y in range(s):
			enlarged_image[x][y] = origin_image[x][y]
			enlarged_image[x][enlarged_height - y - 1] = origin_image[x][height - y - 1]
			enlarged_image[enlarged_width - x - 1][y] =  origin_image[width - x - 1][y]
			enlarged_image[enlarged_width - x - 1][enlarged_height - y - 1] = origin_image[width - x - 1][height - y - 1]

	return enlarged_image

# function to print the image so as to see the enlarge function's output image
def print_image(image_array, image_print_name):
	width = len(image_array)
	height = len(image_array[0])

	printImage = Image.new('L',(width, height), 'white')
	draw = ImageDraw.Draw(printImage)	

	for i in range(width):
		for j in range(height):
			draw.point((i, j), image_array[i][j])

	filename = image_print_name + '.bmp'
	printImage.save(filename, format='BMP')		


image_name = 'bird'
image_type = 'tif'
im = Image.open(image_name + '.' + image_type)
data = im.load()
enlarge_size = 100
origin_image = [[255 for i in range(im.size[1])] for j in range(im.size[0])]
result = [[]]

for i in range(im.size[0]):
	for j in range(im.size[1]):
		origin_image[i][j] = data[i, j]

result = enlarge_image(enlarge_size, origin_image)

image_print_name = image_name + '_print'
print_image(result, image_print_name)

