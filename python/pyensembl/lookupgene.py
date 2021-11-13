#!/usr/bin/env python

from pyensembl import EnsemblRelease

# Ensembl release 75 == GRCh37 (hg19)
# Ensembl release 77 == GRCh38 (hg38)


print("Hello!")

ensembl = EnsemblRelease(release=75)

genes = ensembl.genes_at_locus(contig="1", position=1000000)