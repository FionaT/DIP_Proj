from PIL import Image, ImageDraw
import numpy as np 


def real_filter(a):
	print a

def F(u, v):
	result = 0.0

	for x in range(M):
		for y in range(N):
			angle = 2 * np.pi * (u * x / float_M + v * y / float_N)
			e_part = 1 / complex(np.cos(angle), np.sin(angle) )
			result += data[x, y] * e_part

	#result = np.sqrt(result.real * result.real + result.imag * result.imag)

	return result

im = Image.open('sample4.bmp')
data = im.load()
M, N = im.size
float_M = round(M, 4)
float_N = round(N, 4)

ans = [[0.0 for i in range(N)] for j in range(M)]

for u in range(M):
	for v in range(N):
		ans[u][v] = F(u, v)
'''
resultImage0 = Image.new('L',(M, N), 'white')
draw = ImageDraw.Draw(resultImage0)

for i in range(M):
	for j in range(N):
			draw.point((i, j), ans[i][j])

#save the output files
resultImage0.save('0401_b_0.bmp', format='BMP')
'''
for u in range(M):
	for v in range(N):
		ans[u][v] = real_filter(ans[u][v])
'''
resultImage1 = Image.new('L',(M, N), 'white')
draw = ImageDraw.Draw(resultImage1)

for i in range(M):
	for j in range(N):
			draw.point((i, j), ans[i][j])

#save the output files
resultImage1.save('0401_b_1.bmp', format='BMP')
'''
