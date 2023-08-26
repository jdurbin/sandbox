#!/usr/bin/env julia 

using FASTX

# Get the input FASTA file name and sequence name from command line arguments
if length(ARGS) < 3
	println("seqbyname.jl input targetname output")
	exit()
end

input_file = ARGS[1]
sequence_name = ARGS[2]
output_file = ARGS[3]


open(FASTA.Reader,input_file) do reader
	for record in reader
		if FASTA.identifier(record) == sequence_name
			open(FASTA.Writer,output_file) do writer
				write(writer,record)
			end			
			break
		end
	end
end

# Holy crap this is fast... not sure I believe it. 
# 5s 	for chr6
# 6.7s 	for chr20 
