#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from Bio import SeqIO

# chr16	21835086	21836107	chr16	21836107	21837222

fasta_file = sys.argv[1]  # Input fasta file

seqdict = SeqIO.to_dict(SeqIO.parse(open(fasta_file),'fasta'))

print("name\tsize")
for seqName,seq in seqdict.items():
    print(f"{seqName}\t{len(seq):,}")