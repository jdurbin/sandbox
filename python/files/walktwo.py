#!/usr/bin/env python3

import sys

fname1 = sys.argv[1]
fname2 = sys.argv[2]
f1 = open(fname1,"r")
f2 = open(fname2,"r")

for line1 in f1:
    for line2 in f2:
        name1 = line1.strip()
        name2 = line2.strip()
        if name1==name2:
            print(f"{name1} MATCHES {name2}")
        else:
            print(f"{name1} NE {name2}")
        break
f1.close()
f2.close()