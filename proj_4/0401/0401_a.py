#the simple 2DFT is for the 2*2 image
#with 4 fourier bases
#and 4 fourier coefficients
from PIL import Image, ImageDraw
import numpy as np 

def f(u, v):
	result = data[u, v]

	if(u == 0 and v == 0):
		return result
	else:
		result = round(result, 4)
		result = result / (u + v) 

		return result
	

im = Image.open('sample4.bmp')
data = im.load()
M, N = im.size
float_M = round(M, 4)
float_N = round(N, 4)

ans = [[0.0 for i in range(N)] for j in range(M)]

for u in range(M):
	for v in range(N):
		ans[u][v] = f(u, v)
		print ans[u][v]

resultImage = Image.new('L',(M, N), 'white')
draw = ImageDraw.Draw(resultImage)

for i in range(M):
	for j in range(N):
			draw.point((i, j), ans[i][j])

#save the output files
resultImage.save('ans_0401_a.bmp', format='BMP')
