# Read a BMP file (gray level image) from hard drive, display it  
# on the screen and rewrite it into BMP file back to hard drive.
# Reload the image again and do the down sampling (reduce the special 
# resolution) and quantization (reduce gray level resolution)

from PIL import Image, ImageDraw

# open an image and get its information
im = Image.open('bird.bmp')
data = im.getdata()
width = im.size[0]
height = im.size[1]

# new two blank images for rewrite and downsampling
rewriteImage = Image.new('L',(width, height), 'white')
downSamplingImage = Image.new('L',(width/2, height/2), 'white')
draw = ImageDraw.Draw(rewriteImage)
l = 64
# show the image
im.show()

# rewrite the image 
for i in range(width):
	for j in range(height):
			draw.point((i, j), data[(j*width)+i])

# down sampling
draw = ImageDraw.Draw(downSamplingImage)
for i in range(width):
	for j in range(height):
		if(j % 2 == 0 & i % 2 == 0):
			# reduce gray level by multipling 0.7 
			draw.point((i/2, j/2), (data[(j*width)+i]/l)*l)

#save the output files
rewriteImage.save('bird_rewrite.bmp', format='BMP')
downSamplingImage.save('bird_downSampling.bmp', format='BMP')
