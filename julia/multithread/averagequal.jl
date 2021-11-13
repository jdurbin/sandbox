#!/usr/bin/env julia
using XAM,Statistics
bamName = ARGS[1]

function histQuals(bamInName) 
	count = 0   
    allquals=Int[]
    bamIn = open(BAM.Reader,bamInName)
    for a in bamIn
		count+=1
        push!(allquals,BAM.mappingquality(a))
    end
	
	println("Mean quality: ",mean(allquals))
	println("Count: ",count)
end

histQuals(bamName)


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

