#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

# Read sequence dictionary for HLA
seqFile = "data/S2_callseqs.fa"
seqdict = SeqIO.to_dict(SeqIO.parse(open(seqFile),'fasta'))

#target = "HLA:HLA00602" # >HLA:HLA00602 DQA1*01:02:01:01 6484 bp
#chrStart=32628178 # DQA1
#chrEnd=32637531

target = "HLA:HLA00010" # >HLA:HLA00010 A*02:05:01:01 3517 bpa
chrStart = 29941259
chrEnd = 29945884

hlaseq = seqdict[target]
# print("hla seq: ",len(hlaseq))

# Read chromosome 6
chr6Name= "data/chr6_hg38.fa"
chr6Dict = SeqIO.to_dict(SeqIO.parse(open(chr6Name),'fasta'))
chr6seq = chr6Dict['chr6']

# Pull out region of chromosome6 
hlaref = chr6seq[chrStart:chrEnd]
#print("hlaref: ",len(hlaref))

# Align that region to big HLA sequence
alignmentsA1 = pairwise2.align.localxs(hlaref.seq,hlaseq.seq,-5,-1)

alignstring = format_alignment(*alignmentsA1[0])
(ref,matches,target,score,blank) = alignstring.split("\n")
(refstart,refseq) = ref.strip().split(" ")
(targetstart,targetseq) = target.strip().split(" ") 
prefix = max(len(refstart),len(targetstart))
refstart=int(refstart)
targetstart=int(targetstart)

matchseq = matches[prefix+1:]
targetseq = target[prefix+1:]
#print("refstart: ",refstart,"\ttargetstart: ",targetstart)
#print("prefix: ",prefix)
#print("===========================")
index = 0
genomiccoord=refstart-1
for r,m,t in zip(refseq,matchseq,targetseq):  
    if m == "|":
        index+=1
        genomiccoord+=1
    elif m==".":
        index+=1
        genomiccoord+=1
    elif t == "-":
        index+=1
        genomiccoord+=1
    elif t == "-":
        # do nothing... an insertion in the query doesn't advance 
        # the reference index
        pass
    
    # Rotate symbols for more readable output
    if m=="|": m="-"
    if t=="-": t="||"
    if r=="-": r="||"
    #print(f"{index}\t{genomiccoord+chrStart}\t{r} {m} {t}")  
    if r.upper() != t.upper(): 
        if r != "-" and r != "||" and t != "-" and t != "||":
            print(f"chr6 \t{genomiccoord+chrStart}\t.\t{r}\t{t}\t{30.0}\tPASS\t.\tGT:GQ:DP:AD:VAF:PL:PS\t1/1:6:2:0,2:1:28,4,0:.")  



# chr6    160356  .       G       T       29.9    PASS    .       GT:GQ:DP:AD:VAF:PL:PS   1/1:6:2:0,2:1:28,4,0:.
#chr6    177748  .       T       C       33.3    PASS    .       GT:GQ:DP:AD:VAF:PL:PS   1/1:6:2:0,2:1:32,4,0:.
#chr6    242762  .       A       G       30.7    PASS    .       GT:GQ:DP:AD:PQ:PD:PS    1|0:31:6:4,2:100:6:242762
