#!/usr/bin/env python3

from collections import Counter



names = ['bob','mary','bob','bob','alice','bob']

c = Counter()

for name in names:
    # Expects input to be an iterable
    c.update([name])
    
print(c)


pcount = Counter()
pairs=[('bob','mary'),('bob','alice'),('bob','alice'),('bob','alice')]
for pair in pairs:
    pcount.update([pair])
    
print(pcount)

for key,value in pcount.items():
    print(f"{key[0]}\t{key[1]}\t{value}")