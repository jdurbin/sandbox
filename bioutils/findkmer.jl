#!/usr/bin/env -S julia
using FASTX,BioAlignments,BioSequences,ArgParse,CodecZlib

# time ./findkmer.jl -t AGCTCCCTGCCTGGGGCAACTCTGTAAGTCCATAAGCAG -f OmniC_1_combined_R1.fastq.gz > R1.txt
# real    29m11.034s


function parseargs()
	s = ArgParseSettings()
	s.description=
	"""
	Output names of all reads matching a given exact sequence.  	
	"""
	@add_arg_table s begin
		"--tseq","-t"
			help = "Sequence to match"
			required=true		
		"--fastq","-f"
			help = "fastq file"
			required=true			
	end	
	return parse_args(s)
end


function scanFastQ(fastqName,targetseq)
	
	print("Scanning ",fastqName," for ",targetseq,"...")

	revtarget = reverse_complement(targetseq)
	query = ExactSearchQuery(targetseq)
	revquery = ExactSearchQuery(revtarget)
	
	reader = FASTQ.Reader(GzipDecompressorStream(open(fastqName)))
	for record in reader
		readseq = FASTQ.sequence(record)		
		if occursin(query,readseq) || occursin(revquery,readseq)
			println(FASTQ.identifier(record))
		end
	end
	close(reader)

end


function main()
	args = parseargs()	
	scanFastQ(args["fastq"],LongDNASeq(args["tseq"]))
end



main()
