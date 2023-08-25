#!/usr/bin/env julia 
using FASTX
using BioAlignments
using ArgParse

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
scoremodel = AffineGapScoreModel(EDNAFULL, gap_open=-5, gap_extend=-1);
res = pairalign(LocalAlignment(),hlaref,hlaseq,scoremodel)

print(res)

prettyprint(stdout, res)

# HLA-DQA1
# ./cutandalign.jl  2.58s user 0.86s system 101% cpu 3.398 total


