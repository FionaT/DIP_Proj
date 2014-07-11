#p228 fig4.4
#draw the figure of |F(u)|

from PIL import Image, ImageDraw
from pylab import *
import numpy as np 

def f(x):
	if(x >= -W/2 and x <= W/2):
		y = A
	else:
		y = 0

	return y

def F(u, t):
	result = 0.0

	for i in range(len(t)):
		angle = 2 * np.pi * u * t[i] / (M + 1)
		R = np.cos(angle)
		I = np.sin(angle)
		C = complex(R, I)
		e_part = 1 / C
		result += f(t[i]) * e_part

		result = np.sqrt(result.real * result.real + result.imag * result.imag)


	return result

#the number of points
M = 60
#the hight of the line in origin pic
A = 12
#the width of the 12-height line
W = 10

t = np.linspace(-M/2, M/2, M + 1)
u = np.linspace(-M/2, M/2, M + 1)
ans = [0 for i in range(M + 1)] 

for i in range(len(u)):
	ans[i] = F(u[i], t)

xlim(-40, 40)
ylim(0, 200)

plot(u, ans)
show()

