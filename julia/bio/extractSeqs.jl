#!/usr/bin/env julia 

#!/usr/bin/env julia 
using FASTX
using BioAlignments


targets = readlines(ARGS[1])


# Read sequence dictionary for HLA
seqFile = "data/hla_gen.fa"
type2seq = Dict()
open(FASTA.Reader,seqFile) do reader
	for record in reader
		# HLA:HLA14787_DQA1*01:01:01:03_5667_bp
		# HLA:HLA17305_DQA1*01:01:01:05_6493_bp
		name = FASTA.identifier(record)	
		FASTA.identifier		
		
		
		#type2seq[name]=FASTA.sequence(record)
	end
end

#type2seqID=Dict()
#for (name,seq) in name2seq
		
#end

fields = split(name,":")
5-element Vector{SubString{String}}:
 "HLA"
 "HLA14787_DQA1*01"
 "01"
 "01"
 "03_5667_bp"