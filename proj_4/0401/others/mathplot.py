import matplotlib.pyplot as plt
import numpy as np 

n = [1,1,1,2,2,3,4]

the_max = max(n) + 2
the_min = 0

print the_max

bins = np.arange(the_min, the_max, 1)

print bins

plt.hist(n, bins)

plt.show()

