#!/usr/bin/env python3

import sys

fname = sys.argv[1]


with open(fname) as fin:
    heading = fin.readline()
    for line in fin:
        (Chromosome,Start,End,dmin,dmax,depthcount,samples,avgdepth) = line.strip().split("\t")
        dmin = int(dmin)
        if dmin < 100:
            print(f"{Chromosome}\t{Start}\t{End}\t{dmin}\t{dmax}\t{depthcount}\t{samples}\t{avgdepth}")
        