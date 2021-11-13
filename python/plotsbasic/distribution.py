#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

#snpfile="c20_snp_coverage.txt"
#indelfile="c20_indel_coverage.txt"
indelfile="fragsizes.txt"

#snpdata = pd.read_csv(snpfile,names=['counts'])
indeldata = pd.read_csv(indelfile,names=['Distance Between First and Last SNP'])

histbins=[i for i in range(0,39995925)]
sns.distplot(indeldata['Distance Between First and Last SNP'],kde=False, color='blue', bins=histbins)
#sns.distplot(snpdata['counts'], kde=False, color='red', bins=histbins,label='SNPs')
plt.legend(prop={'size':12})
plt.title("Distirution of Fragment Sizes\nMax: 39,995,925 Mean: 694,622 Median: 61")
#plt.xlim([0,251])
plt.show()

#plt.savefig('')