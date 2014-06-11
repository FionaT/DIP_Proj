# Write program to perform spatial filtering of an 
# image (see Section 3.4 regarding implementation). 
# You can fix the size of the spatial mask at 3 x 3, 
# but the coefficients need to be variables that can 
# be input into your program. This project is generic, 
# in the sense that it will be used in other projects
# to follow.

from PIL import Image, ImageDraw

# count the new grey level in position(i,j)
def laplacian_enhancement(i, j):
	result = extend_data[i][j]
	result = result * 5 - extend_data[i - 1][j] - extend_data[i][j - 1] - extend_data[i + 1][j] - extend_data[i][j + 1]

	return result

def extend_image():
	# draw the new HE image
	extendImage = Image.new('L',(extend_width, extend_height), 'white')
	draw = ImageDraw.Draw(extendImage)	

	for i in range(width):
		for j in range(height):
			extend_data[i + extend_len][j + extend_len] = data[i, j] 

	extend_data[0][0] = data[0, 0]
	extend_data[0][extend_height - 1] = data[0, height - 1]
	extend_data[extend_width - 1][0] = data[ width - 1, 0]
	extend_data[extend_width - 1][extend_height - 1] = data[ width - 1, height - 1]

	
	for i in range(width):
		extend_data[i + 1][0] = data[i, 0]
		extend_data[i + 1][extend_height - 1] = data[i, height - 1]

	for i in range(height):
		extend_data[0][i + 1] = data[0, i]
		extend_data[extend_width - 1][i + 1] = data[width - 1, i]

	for i in range(extend_width):
		for j in range(extend_height):
			draw.point((i,j), extend_data[i][j])

	filename = 'extend_image_fractured_spine.bmp'
	extendImage.save(filename, format='BMP')

	return 0

# open an image and get its information
im = Image.open('Fig0308(a)(fractured_spine).tif')
data = im.load()
width, height = im.size

extend_len = (3 - 1)/2
extend_width = extend_len * 2 + width
extend_height = extend_len * 2 + height
extend_data = [[ 255 for i in range(extend_height)] for j in range(extend_width)] 

# new a blank images for laplacian enhancement
resultImage = Image.new('L',(width, height), 'white')

extend_image()

# draw the laplacian enhancement image
draw = ImageDraw.Draw(resultImage)

for i in range(width):
	for j in range(height):
		p = laplacian_enhancement(i + 1, j + 1)
		draw.point((i, j), p)

#save the output files
filename = 'lacplacement_image_fractured_spine.bmp'
resultImage.save(filename, format='BMP')
