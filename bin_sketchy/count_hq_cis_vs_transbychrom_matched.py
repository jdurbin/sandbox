#!/usr/bin/env python3
import sys,pysam
from collections import Counter

def addContigSizes(contigsizes,filename):
    with open(filename) as fin:
        for line in fin:
            (name,length,offset,linebases,linewidth) = line.strip().split("\t")
            contigsizes[name] = int(length)

# Read in contig sizes so we can output them with the link stats...
patsizes = "/mnt/ebs/james/ref/hifiasm/human-HG002.pat.fa.gz.fai"
matsizes = "/mnt/ebs/james/ref/hifiasm/human-HG002.mat.fa.gz.fai"
contigsizes={}

addContigSizes(contigsizes,patsizes)
addContigSizes(contigsizes,matsizes)

bamInName = sys.argv[1]
bamIn = pysam.AlignmentFile(bamInName)

cisCount = Counter()
transMatchedCount = Counter()
transOtherCount = Counter()

for a in bamIn:        
    refname = a.reference_name
    nextrefname = a.next_reference_name
    
    if a.mapping_quality < 40: continue
    if refname==nextrefname: 
        cisCount.update([refname])
    else: 
        # Only count trans links between these two chromosomes...
        pairA="h1tg000017l"
        pairB="h2tg000010l"
        
        if (refname==pairA and nextrefname==pairB) or (refname==pairB and nextrefname==pairA):
            transMatchedCount.update([refname])
        else:
            transOtherCount.update([refname])

print("contigname\tcontigsize\tcislinks\ttranslinks")
for k,v in cisCount.items():
    if k in transCount:
        csize = contigsizes[k]
        transcnt = transCount[k]
        print(f"{k}\t{csize}\t{v}\t{transcnt}")
    


# contigCounts = Counter()
#for a in bamIn:
#    refname = a.reference_name
#    contigCounts.update([refname])