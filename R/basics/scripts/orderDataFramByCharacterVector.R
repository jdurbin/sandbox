#!/usr/bin/env Rscript

# If you don't put check.names=FALSE R will (silently!) convert column headings that begin with 
# numbers 123 into X123. 
all.data = read.table("../data/ea2_simpleonly.tab",
			row.names = 1,header=TRUE,sep="\t",check.names=FALSE)
dim(all.data)
all.data[1:3,1:4]

cnames = colnames(all.data)


colormap = read.table("../data/samplecolormap.tab",header=TRUE,sep="\t")
dim(colormap)
colormap[1:5,]

ordered = colormap[match(cnames,colormap[,1]),]

dim(ordered)

ordered[1:5,]


ordered$color[1:5]

