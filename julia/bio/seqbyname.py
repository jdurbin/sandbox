#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from Bio import SeqIO

fasta_file = "data/hla_gen.fa"

seqdict = SeqIO.to_dict(SeqIO.parse(open(fasta_file),'fasta'))

print(seqdict["HLA:HLA16652_A*01:01:01:09_3340_bp"])