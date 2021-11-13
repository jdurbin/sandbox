#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import gridspec



fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
image = np.random.poisson(10., (100, 80))
i = ax.imshow(image, interpolation='nearest')
fig.colorbar(i)  # note that colorbar is a method of the figure, not the axes

plt.show()

#fig.savefig("fig.png")
