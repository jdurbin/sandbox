#!/usr/bin/env -S julia
using FASTX,BioAlignments,BioSequences,ArgParse,CodecZlib,XAM

# time ./findkmer.jl -t AGCTCCCTGCCTGGGGCAACTCTGTAAGTCCATAAGCAG -f OmniC_1_combined_R1.fastq.gz > R1.txt
# real    29m11.034s


# AAATAAATAAGAAAGAAAGAAAGAAAGAAA

function parseargs()
	s = ArgParseSettings()
	s.description=
	"""
	Output names of all reads (from either FASTQ or BAM) matching a given exact sequence.  	
	"""
	@add_arg_table s begin
		"--tseq","-t"
			help = "Sequence (e.g. kmer) to match"
			required=true		
		"--fastq","-f"
			help = "fastq file (optional, one of fastq/bam required)"
			required=false				
		"--bam","-b"
			help = "bam file (optional, one of bam/fastq required.)"
			required = false
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

function scanBAM(bamName,targetseq)
	
	println(stderr,"Scanning ",bamName," for ",targetseq,"...")

	revtarget = reverse_complement(targetseq)
	query = ExactSearchQuery(targetseq)
	revquery = ExactSearchQuery(revtarget)	
	
	bamIn = open(BAM.Reader,bamName)
	for a in bamIn
		readseq = BAM.sequence(a)
		if occursin(query,readseq) || occursin(revquery,readseq)
			println(BAM.tempname(a))
		end
	end
	close(bamIn)
end


function main()
	args = parseargs()	
	
	if args["fastq"] != nothing
		scanFastQ(args["fastq"],LongDNASeq(args["tseq"]))
	elseif args["bam"] != nothing
		scanBAM(args["bam"],LongDNASeq(args["tseq"]))
	else
		println("Must specify one of -fastq or -bam")
	end
end



main()
