#!/usr/bin/env python
import sys
import pysam
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-b",help="bam file")
args = parser.parse_args()

bamfile = pysam.AlignmentFile(args.b,'rb')

print("name\talen\tisread2\tis_supplementary")
for a in bamfile.fetch(until_eof=True):
    if a.is_duplicate: continue
    
    name = a.query_name
    alen = a.reference_length
    if a.is_read2: read = "read2"
    else: read = "read1"
        
    if a.is_supplementary: supp = "SUPP"
    else: supp="PRIM"
    
    cigstats = a.get_cigar_stats()
    cmatch = cigstats[0][0]
    cins=cigstats[0][1]
    cdel=cigstats[0][2]
    
    print(f"{name}\t{alen}\t{read}\t{supp}\t{a.mapping_quality}\t{cmatch}\t{cins}\t{cdel}")
