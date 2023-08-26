#!/usr/bin/env python3
"""
Scan through bedpe's, filter for things in sensible places, extract images from Hi-C matrices.
"""


import pandas
import pysam
import numpy
import scipy
import re
import skimage.transform

import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

import cooler
from multiprocessing import Pool


def load_bedpe(fname):
    data = pandas.read_csv(fname,
                           sep="\t",
                           names=("chrom1", "start1", "end1",
                                  "chrom2", "start2", "end2",
                                  "size","type","origin"))
    return data


def cooler_snapshot(tuple):
    matrix, calls, output_prefix, widen, i = tuple
    chrom1, start1, end1, chrom2, start2, end2, size,svtype,origin = calls.loc[i]

    #chrom1 = re.sub("chr", "", chrom1)
    #chrom2 = re.sub("chr", "", chrom2)

    start1 = max(0, start1 - widen) 
    end1 += widen
    start2 = max(0, start2 - widen)
    end2 += widen
    region1 = f"{chrom1}:{start1}-{end1}"
    region2 = f"{chrom2}:{start2}-{end2}"

    #print("Fetching", region1, region2)

    try:
        counts = matrix.fetch(region1, region2) + 1  # extract dense 2D matrix out of sparse matrix object
    except:
        print("Out of range, skipping", region1, region2)
        return None

    #print(counts.min(), counts.max(), counts.mean())

    #counts_scaled = skimage.transform.rescale(counts, scale=10, anti_aliasing=False)

    img_file_name = f"{output_prefix}.{region1}.{region2}.png"
    
    # image = matplotlib.image.createimage(numpy.log10(counts))
    # image_with_ticks = addTickMarks(image,chromosomesizes)
    # save(image_with_ticks)
    
    
    matplotlib.image.imsave(img_file_name,
                            numpy.log10(counts), vmin=0, vmax=1)
    print("Wrote", img_file_name)

    return counts


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-ref", required=False, default="/ref/hg38/GRCh38.p12.fa")
    parser.add_argument("-bedpe", required=False, default=None)
    parser.add_argument("-cool", required=True)
    parser.add_argument("-widen", default=1000000, type=int)
    parser.add_argument("-output_prefix", required=True)
    args = parser.parse_args()

    ref = pysam.FastaFile(args.ref)
    sv_calls = load_bedpe(args.bedpe)

    chrom_sizes = dict(zip(ref.references, ref.lengths))
    for key in list(chrom_sizes.keys()):
        k2 = re.sub("chr", "", key)
        chrom_sizes[k2] = chrom_sizes[key]

    csize1 = numpy.array([chrom_sizes[c] for c in sv_calls.chrom1])
    csize2 = numpy.array([chrom_sizes[c] for c in sv_calls.chrom2])

    a = sv_calls.start1 / csize1
    b = sv_calls.start2 / csize2
    non_telomeric_calls = ((a > 0.1) & (a < 0.9) & (b > 0.1) & (b < 0.9))

    cool = cooler.Cooler(args.cool)

    matrix = cool.matrix(balance=False)

    tuples = []
    for i in range(len(sv_calls)):
        tuple = (matrix, sv_calls, args.output_prefix, args.widen, i)
        tuples.append(tuple)

    list(map(cooler_snapshot, tuples))
