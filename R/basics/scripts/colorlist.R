#!/usr/bin/env Rscript
library(ggplot2)


outputfile="colorlist.png"
png(outputfile, units="px", width=1000, height=4000, res=150)

par(mar=c(0,0,0,0))
cars <- c(1, 3, 6, 4, 9)
plot(cars)

colorlist = read.table("easycolors.txt",header=TRUE,sep="\t",check.names=FALSE)
			
colorlist

legend("topleft",as.character(colorlist$name),fill=as.character(colorlist$color))

#legend("topleft", c("cars","trucks"),fill=c("blue","red"));
