# Use the program developed in Project 03-03 to implement high-boost filtering, 
# as given in Eq. (3.6-9). The averaging part of the process should be done using 
# the mask in Fig. 3.32(a).

from PIL import Image, ImageDraw

def get_origin():

	for i in range(width):
		for j in range(height):
			origin_image[i][j] = data[i, j]

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

def get_w(gaussian_mask_size):
	w = [0 for i in range(gaussian_mask_size * gaussian_mask_size)]
	e = 2.71828
	d = 5.0
	n = 0
	for i in range(-2, 3):
		for j in range(-2, 3):
			w[n] = e ** ( (-1) * (i * i + j * j) / (2 * d * d) )
			n += 1

	return w

def count_gaussian_pixel(i, j, enlarged_image, gaussian_mask_size, w, sum):
	result = 0.0
	mask_index = [ [0 for n in range(2)] for m in range(gaussian_mask_size * gaussian_mask_size)]
	start = -1 * (gaussian_mask_size / 2)
	end = gaussian_mask_size / 2 + 1
	dis = gaussian_mask_size / 2
	n = 0

	for x in range(start, end):
		for y in range(start, end):
			mask_index[n][0] = i + x + dis
			mask_index[n][1] = j + y + dis
			n += 1
	
	for x in range(gaussian_mask_size * gaussian_mask_size):
		result += enlarged_image[mask_index[x][0]][mask_index[x][1]] * w[x]

	result /= sum
	#print result
	#print mask_index

	return result

def gaussian_filter(gaussian_mask_size, origin_image):
	enlarged_image = enlarge_image(gaussian_mask_size / 2, origin_image)
	width = len(origin_image)
	height = len(origin_image[0])
	blured_image = [[255 for i in range(height)] for j in range(width)]
	w = get_w(gaussian_mask_size)
	
	sum = 0.0

	for i in range(len(w)):
		sum += w[i]

	for x in range(width):
		for y in range(height):
			blured_image[x][y] = count_gaussian_pixel(x, y, enlarged_image, gaussian_mask_size, w, sum)

	return blured_image

def gmask(origin_image, blured_image):
	width = len(origin_image)
	height = len(origin_image[0])
	gmasked_image = [[255 for i in range(height)] for j in range(width)]

	for x in range(width):
		for y in range(height):
			gmasked_image[x][y] = origin_image[x][y] - blured_image[x][y]
	
	return gmasked_image

def scal(gmasked_image):
	width = len(gmasked_image)
	height = len(gmasked_image[0])
	scaled_image = [[255 for i in range(height)] for j in range(width)]

	for x in range(width):
		for y in range(height):
			scaled_image[x][y] = ( gmasked_image[x][y] + 255 ) / 2

	return scaled_image

def unsharp_mask(origin_image, gmasked_image, k):
	width = len(origin_image)
	height = len(origin_image[0])
	unsharp_image = [[255 for i in range(height)] for j in range(width)]

	for x in range(width):
		for y in range(height):
			unsharp_image[x][y] = origin_image[x][y] + k * gmasked_image[x][y]

	return unsharp_image

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

# open an image and get its information
image_name = 'Fig0340(a)(dipxe_text)'
im = Image.open(image_name+'.tif')
data = im.load()
width, height = im.size
gaussian_mask_size = 5
origin_image = [[ 255 for i in range(height)] for j in range(width)]
k = 3

get_origin()

blured_image = gaussian_filter(gaussian_mask_size, origin_image)
gmasked_image = gmask(origin_image, blured_image)
scal_gmasked_image = scal(gmasked_image)
unsharp_masking_image = unsharp_mask(origin_image, gmasked_image, 1)
highboost_filter_image = unsharp_mask(origin_image, gmasked_image, k)

print_image(origin_image, 'origin_image')
print_image(blured_image, 'gaussian_blured_image')
print_image(scal_gmasked_image, 'scal_gmasked_image')
print_image(unsharp_masking_image, 'unsharp')
print_image(highboost_filter_image, 'highboost_filter_image')
