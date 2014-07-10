import numpy as np 
from pylab import *

def count(x):
	y = [0] * len(x)

	for i in range(len(x)):
		print x[i]
		y[i] = x[i] * x[i] + 2 * x[i] + 70

	return y


x = np.linspace(0, 50, 50)
y = count(x)


line, = plt.plot(x, y, '--', linewidth=2)

plot(x, y)
show()

