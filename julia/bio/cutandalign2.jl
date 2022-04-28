#!/usr/bin/env julia 
using FASTX
using BioAlignments

# Read sequence dictionary for HLA
seqFile = "data/S2_callseqs.fa"
name2seq = Dict()
open(FASTA.Reader,seqFile) do reader
	for record in reader
		name2seq[FASTA.identifier(record)]=FASTA.sequence(record)
	end
end
 
#target = "HLA:HLA00602" # >HLA:HLA00602 DQA1*01:02:01:01 6484 bp
#chrStart=32628178 # DQA1
#chrEnd=32637531
target = "HLA:HLA00010" # >HLA:HLA00010 A*02:05:01:01 3517 bp
chrStart = 29941259
chrEnd = 29945884

hlaseq = name2seq[target]

# Read chromosome 6
chr6File= "data/chr6_hg38.fa"
chr6record = FASTA.Record()
reader = open(FASTA.Reader,chr6File)
read!(reader,chr6record)
close(reader)

# Pull out region of chromosome6 
chr6seq = FASTA.sequence(chr6record)
hlaref = chr6seq[chrStart:chrEnd]

# Align that region to big HLA sequence

for j in 0:40 
	scoremodel = AffineGapScoreModel(EDNAFULL, gap_open=-5, gap_extend=-1);
	res = pairalign(LocalAlignment(),hlaref,hlaseq,scoremodel)
end

#print(res)

# HLA-A
# ./cutandalign.jl  2.69s user 0.54s system 104% cpu 3.080 total

# 10X loop: 
# cutandalign2.jl  3.48s

# 20X loop: 
# cutandalign2.jl  4.54s


# 40X ./cutandalign2.jl  6.65s
# So 2sec = 20X extra so 10X/second steady state. 


# HLA-DQA1
# ./cutandalign.jl  2.58s user 0.86s system 101% cpu 3.398 total


