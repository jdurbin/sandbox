#!/usr/bin/env Rscript

library(plyr)

colormap = read.table("../data/samplecolormap.tab",header=TRUE,sep="\t")
dim(colormap)
colormap[1:5,]

colorset = ddply(colormap,.(tissue),head,n=1)

dim(colorset)
colorset