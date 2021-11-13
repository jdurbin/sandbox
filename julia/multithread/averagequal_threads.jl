#!/usr/bin/env julia --threads 6
using XAM,Statistics,GenomicFeatures

bName = ARGS[1]

println("Threads: ",Threads.nthreads())

function histQuals(bamName,chrName) 
	allquals=Int[]
	bamIn = open(BAM.Reader,bamName,index="$bamName.bai")
	count = 0

	for a in eachoverlap(bamIn,chrName,1:40000000)
		count+=1
    	push!(allquals,BAM.mappingquality(a))
	end

	close(bamIn)

	println(chrName," Count: ",count)
	println("Mean quality: ",mean(allquals))
end


chromList=["chr1","chr2","chr3","chr4","chr5","chr6","chr7","chr8","chr9","chr10","chr11",
			"chr12","chr13","chr14","chr15","chr16","chr17","chr18","chr19","chr20","chr21","chrX"]

Threads.@threads for cName in chromList
	histQuals(bName,cName)
end

# ./averagequal_threads.jl PC-HLA-EG4.bam  16.93s user 0.81s system 342% cpu 5.185 total