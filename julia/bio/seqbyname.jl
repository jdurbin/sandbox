#!/usr/bin/env julia 

using FASTX

seqFile = "data/hla_gen.fa"

name2seq = Dict()
open(FASTA.Reader,seqFile) do reader
	for record in reader
		name2seq[FASTA.identifier(record)]=FASTA.sequence
	end
end

print(name2seq["HLA:HLA16652_A*01:01:01:09_3340_bp"])


# time ./seqbyname.jl
# sequence./seqbyname.jl  1.28s user 0.27s system 112% cpu 1.375 total

# ./seqbyname.py  0.50s user 0.09s system 99% cpu 0.598 total