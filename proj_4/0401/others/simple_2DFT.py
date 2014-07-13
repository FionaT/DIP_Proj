#the simple 2DFT is for the 2*2 image
#with 4 fourier bases
#and 4 fourier coefficients

import numpy as np 

def count_angle(x, y, index):
	u = index[0]
	v = index[1]
	angle = 2 * np.pi * ((u * x / M) + (v * y / N))

	return angle

def count_energy(angle):
	R = np.cos(angle)

	return R

def count_base():
	Matrix = [[[ 0.0 for i in range(M)] for j in range(N)] for k in range(M * N)]
	#use the array index to represent u and v 's value
	index = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]

	for k in range(M * N):
		for i in range(M):
			for j in range(N):
				#print i, j, index[k]
				angle = count_angle(i, j, index[k])
				Matrix[k][i][j] = count_energy(angle)

	return Matrix

def count_Ck(x, base):
	result = [ 0.0 for i in range(M * N)]

	for i in range(M * N):
		for j in range(M):
			for k in range(N):
				result[i] += x[j][k] * base[i][j][k]

	for i in range(M * N):
		result[i] = round(result[i], 4)

	return result

def count_origin(base, Ck):
	result = [[ 0.0 for i in range(M)] for j in range(N)]

	for i in range(M * N):
		for j in range(M):
			for k in range(N):
				base[i][j][k] *= Ck[i]
				base[i][j][k] /= M * N
				result[j][k] += base[i][j][k]	

	for i in range(M):
		for j in range(N):
			result[i][j] = round(result[i][j], 4)

	print result	

#set the initial variables
#including the dimension of the image(matrix)
#and the grey level of each pixel(the z matrix)
M = N = 2
x = [ 0 for i in range(M)]
y = [ 0 for i in range(N)]
z = [[0.4, 0.6], [0.8, 0.2]]

#count the fourier base
base = count_base()

#count the coefficient of each fourier base
Ck = count_Ck(z, base)

#multiply the Ck and fourier base to compare with the origin value
#so as to verify the program
count_origin(base, Ck)




