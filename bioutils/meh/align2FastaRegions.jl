#!/usr/bin/env -S julia
using FASTX,BioAlignments,BioSequences,ArgParse,CodecZlib

function parseRegion(rstr)
	sname,srange= split(rstr,":")
	sstart,send = split(srange,"-")
	return (sname, parse(Int,sstart),parse(Int,send))
end


function readRecordDict(fileName,name2seq)		
	SEQ_TYPE = FASTA
	if occursin("fq",fileName) || occursin("fastq",fileName)
		SEQ_TYPE = FASTQ
	end
	
	if occursin("gz",fileName)
		reader = SEQ_TYPE.Reader(GzipDecompressorStream(open(fileName)))		
	else
		reader = SEQ_TYPE.Reader(open(fileName))
	end
	
	print(stderr,"Reading ",fileName,"...")	
	for record in reader
		name2seq[SEQ_TYPE.identifier(record)]=record
	end
	println(stderr,length(name2seq)," sequences read.")	
	
	return(SEQ_TYPE)
end


function parseargs()
	s = ArgParseSettings()
	s.description=
	"""
	Aligns two regions of a single fasta file.  For example, maybe two 
	different regions in a reference genome.  
	"""
	@add_arg_table s begin
		"--seq","-s"
			help = "Fasta sequence input (e.g. hg38.fa)"
			required=true
		"--refregion","-r"
			help="Ref region (e.g. chr22:42126499-42130810)"
			required=true
		"--queryregion","-q"
			help = "Query region (e.g. chr22:42140203-42144577)"
			required=true	
	end	
	return parse_args(s)
end
	
function main()
	args = parseargs()
		
	# Dictionary for input sequence...	
	allelename2seq = Dict()
	SEQ_TYPE = readRecordDict(args["seq"],allelename2seq)		

	rseqname,rstart,rend = parseRegion(args["refregion"])	
	rrecord = allelename2seq[rseqname]
	rseq = FASTA.sequence(rrecord)
	rseq = rseq[rstart:rend]
	println(stderr,"Reference length:",length(rseq))
	
	qseqname,qstart,qend = parseRegion(args["queryregion"])
	qrecord = allelename2seq[qseqname]
	qseq = FASTA.sequence(qrecord)
	qseq = qseq[qstart:qend]
	println(stderr,"Query length:",length(qseq))
	
	scoremodel = AffineGapScoreModel(EDNAFULL, gap_open=-5, gap_extend=-1);	

	# Don't know how they are oriented, so align both ways and take better score...
	respos = pairalign(LocalAlignment(),rseq,qseq,scoremodel)
	posscore = score(respos)
	
	revqseq = reverse_complement(qseq)
	resneg = pairalign(LocalAlignment(),rseq,revqseq,scoremodel)
	negscore = score(resneg)
	
	println(stderr,"Alignment score:        \t",posscore)
	println(stderr,"Reverse alignment score:\t",negscore)
		
	if negscore > posscore
		println(resneg)		
	else
		println(respos)	
	end
			
end

main()

