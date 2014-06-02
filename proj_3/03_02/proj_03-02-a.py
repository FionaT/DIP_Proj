# Write a computer program for computing 
# the histogram of an image.

from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np 

# open an image and get its information
im = Image.open('HEImage_c.bmp')
data = im.load()
width, height = im.size
p = [0] * ( width * height )
k = 0

for i in range(width):
	for j in range(height):
			# put the grey level of each pixel into an array
			p[k] = data[i, j]
			k += 1

# the_max is max(p) plus 2 because
# because each rect in the the histogram cover an interval of 1, here should plus 1
# and the numpy arrage method's second argument is the total number
# of the new array, not the max num, here should plus 1 too 
the_max = max(p) + 2
the_min = 0

# represents the edge of the histogram
bins = np.arange(the_min, the_max, 1)

plt.hist(p, bins, color='red')

plt.show()



