#!/usr/bin/env python3

import matplotlib
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np


a=[1,1,1,3,4,5,15,12,13,18,20,23,45,77,50,30,123,465,876,223]

print("a=",a)
x = np.sort(a)
print("x=",x)
y = np.arange(len(x))
#y = np.linspace(0,1,len(x))

print("y=",y)
y = y/float(len(x))
print("y=",y)
plt.plot(x, y)

plt.show()



#y= [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
# y= [0.   0.05 0.1  0.15 0.2  0.25 0.3  0.35 0.4  0.45 0.5  0.55 0.6  0.65 0.7  0.75 0.8  0.85 0.9  0.95]

#y= [0.         0.05263158 0.10526316 0.15789474 0.21052632 0.26315789
# 0.31578947 0.36842105 0.42105263 0.47368421 0.52631579 0.57894737
# 0.63157895 0.68421053 0.73684211 0.78947368 0.84210526 0.89473684
# 0.94736842 1.        ]