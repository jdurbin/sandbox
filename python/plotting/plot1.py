#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import gridspec


def plot1(ax):
    x = np.arange(0, 10, 0.2)
    y = np.sin(x)
    ax.plot(x,y)

    return ax

def plot2(ax):
    x = np.arange(0, 10, 0.2)
    y = np.sin(2*x)
    ax.plot(x,y)

    return  ax

def plot3(ax):
    ax.add_subplot("121")
    x = np.arange(0, 10, 0.2)
    y = np.sin(x)
    ax.plot(y,x)

    return ax


# plot it
#fig = plt.figure(figsize=(8, 6)) 

#ax0 = plt.subplot(gs[0])
#ax0.plot(x, y)
#ax1 = plt.subplot(gs[1])
#ax1.plot(y, x)

#plt.tight_layout()
#plt.savefig('grid_figure.pdf')

gs = gridspec.GridSpec(ncols=2, nrows=2, width_ratios=[1,1], height_ratios=[5,5], 
        hspace=0.0, wspace=0.0, left=0, right=1, top=1, bottom=0)

f0,ax0 = plt.subplots()
ax0 = f0.add_subplot(gs[0,:]) # ax1 takes up entire top part. 
plot1(ax0,f0)

ax1 = f0.add_subplot(gs[1,0])
plot2(ax1,f0)

ax2 = f0.add_subplot(gs[1,1])
plot3(ax2,f0)

#f1,ax1 = plot2()

plt.show()


#anno_opts = dict(xy=(0.5, 0.5), xycoords='axes fraction',
#                 va='center', ha='center')
#fig3.add_subplot(spec3[0, 0]).annotate('GridSpec[0, 0]', **anno_opts)