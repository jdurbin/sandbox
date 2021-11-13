#!/usr/bin/env python3

from scipy.stats import binom
import matplotlib.pyplot as plt


#k = 1 # number of successes
#p = 0.985 # probability of non-infection
#n=70 # samples drawn with replacement from population of size N   N>>n approx is OK

#n=20
#for k in range(0,20,1):
#    prob = binom.pmf(k=k,n=n,p=0.5)
#    print("Probability see exactly ",k,"\t in ",n,"samples is ",round(prob,4))
#
#n=20
#for k in range(0,20,1):
#    prob = binom.cdf(k=k,n=n,p=0.5)
#    print("Probability see <= ",k,"\t in ",n,"samples is ",round(prob,4))
#

n=5000
for k in range(0,5000,10):
    prob = binom.pmf(k=k,n=n,p=0.015)
    print("Probability see ",k,"\t in ",n,"samples is ",round(prob,4))

print("\n\n")

n=5000
p=0.015
probs = []
for k in range(0,200,11):
    prob = binom.cdf(k=k,n=n,p=p)
    probs.append(prob)
    print("Probability see <= ",k,"\t in ",n,"samples is ",round(prob,4))
    
fig, ax = plt.subplots(1, 1)
ax.plot(probs)
#ax.plot(binom.pmf(probs,n, p))

plt.show()