import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

v1 = np.random.rand(150,150)
v2 = np.random.rand(150)

fig = plt.figure()

# https://stackoverflow.com/questions/19407950/align-vertically-two-plots-in-matplotlib-provided-one-is-an-imshow-plot
#

# create a 2 X 2 grid 
#gs = grd.GridSpec(2, 2, height_ratios=[1,10], width_ratios=[6,1], wspace=0.1)
gs = gridspec.GridSpec(2, 2, height_ratios=[2,1], width_ratios=[1,1])

# image plot
ax = plt.subplot(gs[0:1,:],figsize=(14, 6))

p = ax.imshow(v1,interpolation='nearest',aspect='equal') # set the aspect ratio to auto to fill the space. 
plt.xlabel('Day')
plt.ylabel('Depth')
#plt.xlim(1,140)

# color bar in it's own axis
colorAx = plt.subplot(gs[1,1])
cb = plt.colorbar(p, cax = colorAx)
cb.set_label('RWU')

# line plot
ax2 = plt.subplot(gs[1,0])

#ax2.spines['right'].set_visible(False)
#ax2.spines['top'].set_visible(False)
#ax2.xaxis.set_ticks_position('bottom')
#ax2.yaxis.set_ticks_position('left')
#ax2.set_yticks([0,1])
x=np.arange(1,151,1)
ax2.plot(x,v2,'k',lw=0.5)
#plt.xlim(1,140)
#plt.ylim(0,1.1)

plt.show()