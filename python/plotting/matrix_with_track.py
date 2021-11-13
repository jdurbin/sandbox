import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np; np.random.seed(0)

Z = np.random.poisson(lam=6, size=(64,64))
x = np.mean(Z, axis=0)
y = np.mean(Z, axis=1)

fig, ax = plt.subplots()
ax.imshow(Z)

# create new axes on the right and on the top of the current axes.
divider = make_axes_locatable(ax)
axtop = divider.append_axes("top", size=1.2, pad=0.3, sharex=ax)
#axright = divider.append_axes("right", size=1.2, pad=0.4, sharey=ax)
#plot to the new axes
axtop.plot(np.arange(len(x)), x, marker="o", ms=1, mfc="k", mec="k")
#axright.plot(y, np.arange(len(y)), marker="o", ms=1, mfc="k", mec="k")
#adjust margins
#axright.margins(y=0)
axtop.margins(x=0)
plt.tight_layout()

plt.show()