# Use the program developed in Project 03-03 to implement high-boost filtering, 
# as given in Eq. (3.6-9). The averaging part of the process should be done using 
# the mask in Fig. 3.32(a).

from PIL import Image, ImageDraw

def get_origin():

	for i in range(width):
		for j in range(height):
			origin_image[i][j] = data[i, j]

def enlarge_image():
	extendImage = Image.new('L',(extend_width, extend_height), 'white')
	draw = ImageDraw.Draw(extendImage)	

	for i in range(width):
		for j in range(height):
			extend_image[i + 1][j + 1] = data[i, j] 

	extend_image[0][0] = data[0, 0]
	extend_image[0][extend_height - 1] = data[0, height - 1]
	extend_image[extend_width - 1][0] = data[ width - 1, 0]
	extend_image[extend_width - 1][extend_height - 1] = data[ width - 1, height - 1]

	for i in range(width):
		extend_image[i + 1][0] = data[i, 0]
		extend_image[i + 1][extend_height - 1] = data[i, height - 1]

	for i in range(height):
		extend_image[0][i + 1] = data[0, i]
		extend_image[extend_width - 1][i + 1] = data[width - 1, i]

	for i in range(extend_width):
		for j in range(extend_height):
			draw.point((i,j), extend_image[i][j])

	filename = image_name + '_extend.bmp'
	extendImage.save(filename, format='BMP')

def blur(i, j):

	result = extend_image[i - 1][j - 1] + extend_image[i - 1][j] + extend_image[i - 1][j + 1] + extend_image[i][j - 1] + extend_image[i][j] + extend_image[i][j + 1] + extend_image[i + 1][j - 1] + extend_image[i + 1][j] + extend_image[i + 1][j + 1]
	result = result / 9

	return result

def blur_image():
	blurImage = Image.new('L',(width, height), 'white')
	draw = ImageDraw.Draw(blurImage)	

	for i in range(width):
		for j in range(height):
			blured_image[i][j] = blur(i + 1, j + 1)
			draw.point((i, j), blured_image[i][j])

	filename = filename = image_name + '_blur.bmp'
	blurImage.save(filename, format='BMP')

def count_gmask():
	maskImage = Image.new('L',(width, height), 'white')
	draw = ImageDraw.Draw(maskImage)	

	for i in range(width):
		for j in range(height):
			masked_image[i][j] = origin_image[i][j] - blured_image[i][j]
			draw.point((i, j), masked_image[i][j])

	filename = image_name + '_gmask.bmp'
	maskImage.save(filename, format='BMP')	

def unsharp_masking(k):
	unsharpImage = Image.new('L',(width, height), 'white')
	draw = ImageDraw.Draw(unsharpImage)	

	for i in range(width):
		for j in range(height):
			unsharp_image[i][j] = masked_image[i][j] * k + origin_image[i][j]
			draw.point((i, j), unsharp_image[i][j])

	filename = image_name + '_unsharp_k='+str(k)+'.bmp'
	unsharpImage.save(filename, format='BMP')	

# open an image and get its information
image_name = 'Fig0219(rose1024)'
im = Image.open(image_name+'.tif')
data = im.load()
width, height = im.size
extend_width = 2 + width
extend_height = 2 + height
origin_image = [[ 255 for i in range(height)] for j in range(width)]
extend_image = [[ 255 for i in range(extend_height)] for j in range(extend_width)] 
blured_image = [[ 255 for i in range(height)] for j in range(width)]
masked_image = [[ 255 for i in range(height)] for j in range(width)]
unsharp_image = [[ 255 for i in range(height)] for j in range(width)]
k = 3

get_origin()
enlarge_image()
blur_image()
count_gmask()
unsharp_masking(k)

