#!/usr/bin/env python3 
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

mu = 0
variance1 = 20000**2
variance2 = 2000**2
sigma1 = math.sqrt(variance1)
sigma2 = math.sqrt(variance2)

x = np.linspace(mu - 3*sigma1, mu + 3*sigma1, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma1))

x2 = np.linspace(mu - 3*sigma2, mu + 3*sigma2,100)
#x2 = [i for i in x2]
plt.plot(x2, stats.norm.pdf(x2, mu, sigma2))


plt.xlim((-50000,50000))
frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticklabels([])
plt.show()