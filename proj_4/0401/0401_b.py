# the simple 2DFT is for the 2*2 image
# with 4 fourier bases
# and 4 fourier coefficients
from PIL import Image, ImageDraw
import numpy as np 

def count_energy(pixel):
	r = pixel.real
	i = pixel.imag

	return r


def real_filter(pixel, coeff):
	result = complex(pixel.real * coeff, pixel.imag * coeff)

	return result

def F(u, v, float_M, float_N):
	result = 0.0

	for x in range(M):
		for y in range(N):
			angle = 2 * np.pi * (u * x / float_M + v * y / float_N)
			e_part = np.exp(-1j * angle)
			#e_part = complex(np.cos(angle), np.sin(angle))
			result += data[x, y] * e_part

	return result

def f(u, v):
	result = data[u, v]
	result = (-1)**(u + v) * result

	return result

# get the image's information	
image_name = 'sample2'
image_type = '.bmp'
im = Image.open(image_name + image_type)
data = im.load()
M, N = im.size
float_M = round(M, 4)
float_N = round(N, 4)
pixel = [[0.0 for i in range(N)] for j in range(M)]

# multiply the input image by (-1)**(x+y) to center the transform for filtering
for u in range(M):
	for v in range(N):
		pixel[u][v] = f(u, v)

# do the fourier transform for the pixel in (u, v)
for u in range(M):
	for v in range(N):
		pixel[u][v] = F(u, v, float_M, float_N)

coeff = 0.9

# Multiply the resulting (complex) array by a real filter function 
for u in range(M):
	for v in range(N):
		pixel[u][v] = real_filter(pixel[u][v], coeff)

resultImage = Image.new('L',(M, N), 'white')
draw = ImageDraw.Draw(resultImage)

for i in range(M):
	for j in range(N):
			draw.point((i, j), count_energy(pixel[i][j]))

#save the output files
resultImage.save(image_name + '_result_b.bmp', format='BMP')
