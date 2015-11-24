#!/usr/bin/env Rscript

args = commandArgs(trailingOnly=TRUE)
datafile= args[1]

cat("Read ",datafile,"...\n",sep="")
all.data = read.table(datafile,
			row.names = 1,header=TRUE,sep="\t",check.names=FALSE)
print(dim(all.data))
print(all.data[1:3,1:2])
cnames = colnames(all.data)
paste("cnames:",cnames)