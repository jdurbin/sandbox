import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

def plot1(ax):
    x = np.arange(0, 10, 0.05)
    y = np.sin(x)
    ax.plot(x,y)
    return ax

def plot2(ax,m):
    x = np.arange(0, 10, 0.01)
    y = np.sin(m*x)
    ax.plot(x,y)
    return  ax

def makeSubplots(f,subplotspec):
    gs00 = gridspec.GridSpecFromSubplotSpec(2,2, subplot_spec=subplotspec)

    ax1 = f.add_subplot(gs00[0,0])
    plot2(ax1,2)

    ax2 = f.add_subplot(gs00[0,1])
    plot2(ax2,4)

    ax3 = f.add_subplot(gs00[1,0])
    plot2(ax3,8)

    ax4 = f.add_subplot(gs00[1,1])
    plot2(ax4,16)

f = plt.figure()

# Top level gridspec 2x1, first plot will take up top row. 
gs0 = gridspec.GridSpec(ncols=1,nrows=2, figure=f)

axMain = plt.Subplot(f, gs0[1])
f.add_subplot(axMain)
plot1(axMain)

makeSubplots(f,gs0[0])

# ============ Handoff to someone else, who will fill in the bottom ==========
# plot(f,gs0[1])
#gs00 = gridspec.GridSpecFromSubplotSpec(2,2, subplot_spec=gs0[1])

#ax1 = plt.Subplot(f,gs00[0,0])
#f.add_subplot(ax1)
#plot2(ax1,2)

#ax2 = plt.Subplot(f,gs00[0,1])
#f.add_subplot(ax2)
#plot2(ax2,4)

#ax3 = plt.Subplot(f,gs00[1,0])
#f.add_subplot(ax3)
#plot2(ax3,8)

#ax4 = plt.Subplot(f,gs00[1,1])
#f.add_subplot(ax4)
#plot2(ax4,16)



plt.show()