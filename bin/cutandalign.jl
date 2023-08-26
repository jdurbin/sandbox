#!/usr/bin/env julia 
using FASTX
using BioAlignments
using ArgParse
using BioSequences


function parseargs()
	s = ArgParseSettings()
	s.description=
	"""
	Align a sequence drawn from a multiple-fasta of sequences (e.g. hla_nuc.fasta)
	against a region of a reference genome (e.g. chr6_hg38.fa)
	"""
	@add_arg_table s begin
		"--source","-s"
			help = "Reference sequence to use"
			required=true			
		"--range","-r"
				help = "Range in ref to use (e.g. 3500:3600)"		
				required=true	
		"--querydb","-q"
			help = "Query database of sequences"
			required=true
					
		"--id","-i"
			help = "Name of query db sequence to align."
			
	end	
	return parse_args(s)
end

# >HLA:HLA00001 A*01:01:01:01 3503 bp
#               ^-- gene name
function getGeneName(record)
	description_raw = FASTA.description(record)
	fields = split(description_raw," ")
	description = fields[2]
	fields = split(description,"*")
	name = fields[1]
	return "HLA-"*name
end

# >HLA:HLA00001 A*01:01:01:01 3503 bp
#               ------------- < HLA type
function getHLAType(record)
	description = FASTA.description(record)
	fields = split(description," ")
	#println("\tgetHLAType getHLAType: ",fields[2])
	return fields[2]
end

function main()

	args = parseargs()
	
	# Read sequence dictionary 
	seqFile = args["querydb"] # hla_nuc.fasta
	print("Reading ",seqFile,"...")
	name2record = Dict()
	open(FASTA.Reader,seqFile) do reader
		for record in reader
			hlatype = getHLAType(record)
			name2record[hlatype]=record
		end
	end
	println("done.")
	
	target = args["id"] # "DQA1*01:02:01:01"
	println("target: ",target)
	targetrecord = name2record[target]
	targetseq = FASTA.sequence(LongDNA{4},targetrecord)	
	
	# Read chromosome 6
	#chr6File= "data/chr6_hg38.fa"
	#chrStart=32628178 # DQA1
	#chrEnd=32637531
	sourceFile = args["source"]
	parts = split(args["range"],":")
	chrStart = parse(Int,parts[1])
	chrEnd = parse(Int,parts[2])

	print("Reading ",sourceFile,"...")
	sourceRecord = FASTA.Record()
	reader = open(FASTA.Reader,sourceFile)
	read!(reader,sourceRecord)
	close(reader)
	println("done.")
	
	# Pull out region of chromosome6 
	sourceSeq = FASTA.sequence(LongDNA{4},sourceRecord)
	sourceExtract = sourceSeq[chrStart:chrEnd]
	
	# Align that region to big HLA sequence
	scoremodel = AffineGapScoreModel(EDNAFULL, gap_open=-5, gap_extend=-1);
	alignment_result = pairalign(LocalAlignment(),sourceExtract,targetseq,scoremodel)

	# Doesn't actually print the alignment
	#print(alignment_result)
	#println(sprint(show,alignment_result))
	
	# Fancy way to replicate what you get from the REPL
	show(IOContext(stdout, :limit => true), MIME("text/plain"), alignment_result)
	println()
	
end

main()

# HLA-DQA1
# ./cutandalign.jl  2.58s user 0.86s system 101% cpu 3.398 total


