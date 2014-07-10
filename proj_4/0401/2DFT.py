from PIL import Image, ImageDraw
from pylab import *
import numpy as np 

def count_angle(x, y, index, M, N):
	u = index[0]
	v = index[1]
	angle = 2 * np.pi * ((u * x / M) + (v * y / N))

	return angle

def count_energy(angle):
	R = np.cos(angle)

	return R

def count_base(M, N):
	
	Matrix = [[[ 0 for i in range(M)] for j in range(N)] for k in range(M * N)]

	index = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]

	for k in range(M * N):
		for i in range(M):
			for j in range(N):
				#print i, j, index[k]
				angle = count_angle(i, j, index[k], M, N)

				Matrix[k][i][j] = count_energy(angle)

	print Matrix


M = N = 2

x = [ 0 for i in range(M)]
y = [ 0 for i in range(N)]
z = [[0.4, 0.6], [0.8, 0.2]]

count_base(M, N)
