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

target = "HLA:HLA00602" # >HLA:HLA00602 DQA1*01:02:01:01 6484 bp
chrStart=32628178 # DQA1
chrEnd=32637531
# target = "HLA:HLA00010" # >HLA:HLA00010 A*02:05:01:01 3517 bp
#chrStart = 29941259
#chrEnd = 29945884

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
for i in 1:2000
	scoremodel = AffineGapScoreModel(EDNAFULL, gap_open=-5, gap_extend=-1);
	res = pairalign(GlobalAlignment(),hlaref,hlaseq,scoremodel)
end

#print(res)

# HLA-A
# ./cutandalign.jl  2.69s user 0.54s system 104% cpu 3.080 total

# HLA-DQA1
# ./cutandalign.jl  2.58s user 0.86s system 101% cpu 3.398 total

# HLA-DQA1 * 2000.  :-(  
# ./cutandalign.jl  648.30s user 17.76s system 99% cpu 11:10.78 total


