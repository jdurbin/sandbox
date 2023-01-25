#!/usr/bin/env python

seq="ATGCGATATCGTAGGCGTCGATGGAGAGCTAGATCGATCGATCTAAATCCCGATCGATTCCGAGCGCGATCAAAGCGCGATAGGCTAGCTAAAGCTAGCA"

rev=seq[::-1]

rev=rev.replace("A","X")
rev=rev.replace("T","A")
rev=rev.replace("X","T")
rev=rev.replace("C","X")
rev=rev.replace("G","C")
rev=rev.replace("X","G")

Kmer=31
M=7
L=len(seq)

for i in range(0, L-Kmer+1):

        sub_f=seq[i:i+Kmer]
        sub_r=rev[L-Kmer-i:L-i]

        min="ZZZZZZZZZZZZZ"
        for j in range(0, Kmer-M+1):
                sub2=sub_f[j:j+M]
                if sub2 < min:
                        min=sub2
                sub2=sub_r[j:j+M]
                if sub2 < min:
                        min=sub2

        print sub_f,min