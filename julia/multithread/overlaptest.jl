#!/usr/bin/env julia
using XAM,Statistics,GenomicFeatures

bamName = "PC-HLA-EG4.bam"

bamIn = open(BAM.Reader,bamName, index="$bamName.bai")
targetChr="chr1"

numAligns = 0
numAligns+=1

allquals=Int[]
for record in eachoverlap(bamIn,targetChr,1:100000)
	numAligns+=1
	push!(allquals,BAM.mappingquality(record))
end
close(bamIn)

println("Num aligns: ",numAligns)
println("Mean quality: ",mean(allquals))