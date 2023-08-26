#!/usr/bin/env bash 

# Simple bash script to answer some frequently asked questions about a bam file
# namely:
#
# What reference was used?   
# What bwa command? 
# Is the bam file sorted? 
# What is the size of reads that went into this alignment? 

samtools view -H $1 | grep bwa | head -n 1
samtools view -H $1 | grep SO
#samtools view PC-HLA-EG4.bam | cut -f 10 | awk '{print "Read Length:\t" length($1)} NR==10{exit}'
echo "First 20 Read Lengths: "
samtools view $1 | cut -f 10 | awk '{printf "%s ",length($1)} NR==20{exit}'
echo ""