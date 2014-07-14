from PIL import Image, ImageDraw
import numpy as np 

def count_energy(pixel):
	r = round(pixel.real, 4)
	i = round(pixel.imag, 4)

	return np.sqrt(r * r + i * i)

def F(u, v, float_M, float_N, data):
	result = 0.0

	for x in range(M):
		for y in range(N):
			angle = round(2 * np.pi * (u * x / float_M + v * y / float_N), 4)
			e_part = np.exp(-1j * angle)
			result += data[x, y] * e_part

	return result

def inverse_F(x, y, float_M, float_N, pixel):
	result = 0.0

	for u in range(M):
		for v in range(N):
			angle = round(2 * np.pi * (u * x / float_M + v * y / float_N), 4)
			e_part = np.exp(1j * angle)
			#e_part = complex(np.cos(angle), np.sin(angle))
			result += pixel[u][v] * e_part

	return result

image_name = 'sample4'
image_type = '.bmp'
im = Image.open(image_name + image_type)
data = im.load()
M, N = im.size
float_M = round(M, 4)
float_N = round(N, 4)
pixel = [[0.0 for i in range(N)] for j in range(M)]

for u in range(M):
	for v in range(N):
		pixel[u][v] =  F(u, v, float_M, float_N, data)

'''
for x in range(M):
	for y in range(N):
		pixel[x][y] =  inverse_F(x, y, float_M, float_N, pixel)
'''
resultImage = Image.new('L',(M, N), 'white')
draw = ImageDraw.Draw(resultImage)

for i in range(M):
	for j in range(N):

			draw.point((i, j), count_energy(pixel[i][j]))

#save the output files
resultImage.save(image_name + '_experiment_1.bmp', format='BMP')
