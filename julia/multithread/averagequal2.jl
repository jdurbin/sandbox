#!/usr/bin/env julia
using XAM,Statistics,GenomicFeatures

bName = ARGS[1]
cName = ARGS[2]

function histQuals(bamName,chrName) 
	allquals=Int[]
	bamIn = open(BAM.Reader,bamName,index="$bamName.bai")
	count = 0

	#for record in eachoverlap(reader, "Chr2", 10000:11000)
	for a in eachoverlap(bamIn,chrName,1:1000000)
		count+=1
    	push!(allquals,BAM.mappingquality(a))
	end

	close(bamIn)

	println("Count: ",count)
	println("Mean quality: ",mean(allquals))
end


histQuals(bName,cName)

# time averagequal.jl /Users/james/projects/hla/capture/bam38/PC-HLA-EG4.bam
# Reading BAM...done.
# Average quality: 43.76016208794757
# averagequal.jl /Users/james/projects/hla/capture/bam38/PC-HLA-EG4.bam  
# 15.48s user 0.94s system 99% cpu 16.422 total

# time averagequal.jl data/PC-HLA-EG4.bam
# Reading BAM...done.
# Average quality: 56.078356406954285
# averagequal.jl data/PC-HLA-EG4.bam  
# 1.85s user 0.42s system 108% cpu 2.105 total

