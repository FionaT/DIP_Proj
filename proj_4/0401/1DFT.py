from PIL import Image, ImageDraw
from pylab import *
import numpy as np 

def f(x):
	y = [0] * len(x)
	A = 10
	K = 5

	for i in range(len(x)):
		if(x[i] <= K):
			y[i] = A
		else:
			y[i] = 0

	return y

def count_angle(x, k, T):
	return np.pi * k * 2 * x / T

def count_complex_number(angle):
	#result = complex(np.cos(angle),np.sin(angle))
	#return result
	R = np.cos(angle)
	I = np.sin(angle)
	C = complex(R, I)
	#print C
	return C

def find_base(N):
	T = N
	base = [[ 0.0 for i in range(N) ] for j in range(N) ] 

	for i in range(N):
		for j in range(N):
			k = i
			x = j
			angle = count_angle(x, k, T)
			base[i][j] = count_complex_number(angle)

	return base

def find_Ck(base, x):
	N = len(x)
	C = [ 0.0 for i in range(N) ]

	for i in range(N):
		for j in range(N):
			C[i] += base[i][j] * x[j]

	return C

def count_energy(c):
	return np.sqrt(c.real * c.real + c.imag * c.imag)

def DFT(x, y):
	N = len(x)
	base = [[ 0.0 for i in range(N) ] for j in range(N) ] 
	C = [ 0.0 for i in range(N) ]
	result = [ 0.0 for i in range(N) ]

	base = find_base(N)
	C = find_Ck(base, x)

	for i in range(N):
		for j in range(N):
			result[i] += C[j] * base[j][i]
	
	for i in range(N):
		result[i] = count_energy(result[i])


	for i in range(N):
		C[i] = count_energy(C[i])

	return C


M = 20
# x range from 0 to 9, there are 10 points
x = np.linspace(0, M, M)
y = f(x)

print x
print y

result = DFT(x, y)

xlim(0,M)
ylim(0,30)

plot(x, result)
show()



