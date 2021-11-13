#!/usr/bin/env python3

import matplotlib
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np


lengths = defaultdict(list)
lib_count = defaultdict(int)

lib="good"
lengths[lib].append(20)
lengths[lib].append(30)
lengths[lib].append(100)
lengths[lib].append(330)
lengths[lib].append(10)
lengths[lib].append(40)
lengths[lib].append(45)
lengths[lib].append(60)
lengths[lib].append(22)
lengths[lib].append(10)
lib_count[lib]+=10

lib="good"
lengths[lib].append(21)
lengths[lib].append(33)
lengths[lib].append(109)
lengths[lib].append(320)
lengths[lib].append(14)
lengths[lib].append(32)
lengths[lib].append(33)
lengths[lib].append(51)
lengths[lib].append(72)
lengths[lib].append(60)
lib_count[lib]+=10


lib="bad"
lengths[lib].append(12)
lengths[lib].append(13)
lengths[lib].append(24)
lengths[lib].append(300)
lengths[lib].append(7)
lengths[lib].append(35)
lengths[lib].append(25)
lengths[lib].append(45)
lengths[lib].append(19)
lengths[lib].append(8)
lib_count[lib]+=10

libs = sorted(lengths.keys())
print(libs)

for lib in libs:
    lengths[lib] = np.array(lengths[lib])
    lens = lengths[lib][lengths[lib] != 0]
    length_cdf = np.linspace(0, 1, len(lens))
    plt.plot(sorted(lens), length_cdf, "-")
        
    
plt.xscale("log")
plt.ylabel("Fraction of aligned fragments")
plt.xlabel("Pair size")
plt.title(f"Cumulative distribution (cis-chromosomal pairs only)")
plt.grid(linewidth=0.25)
plt.show()
#plt.savefig(f"{args.output_prefix}_size_cdf_cisonly.{args.output_image_format}")
plt.close()
