#!/usr/bin/env python3

import pyranges as pr
import pandas as pd
import numpy as np

genesdf = pd.read_csv("final_gene_list.bed",sep="\t",names=["Chromosome","Start","End","Strand","id","Gene","required"])
genesranges = pr.PyRanges(genesdf)


             Chromosome     Start       End Strand         id          Gene required
0                  chr6  29941260  29945884      +       3105         HLA-A    Set17
1                  chr6  31353872  31357188      -       3106         HLA-B    Set17
2                  chr6  31268749  31272130      -       3107         HLA-C    Set17


Chromosome  Start   End nul1    nul2    strand  Gene    required id
chr6    29941260        29945884        .       .       +         HLA-A Set17   3105
chr6    31353872        31357188        .       .       -         HLA-B Set17   3106
chr6    31268749        31272130        .       .       -         HLA-C Set17   3107

