#!/usr/bin/env -S julia -t 10
using FASTX,BioAlignments,BioSequences,ArgParse,CodecZlib



"""
    getSNPListFromAlignment(aln)
	
Takes an alignment and produces a list of the SNPs and indels in the alignment.
"""
function getSNPAndListFromAlignment(aln,chrom,chrStart)
	index = 1		
	
	# This is a bit much, but everything else in the alignment 
	# interface is super clean...
	#refstart=aln.a.aln.anchors[1].refpos+1 
	refstart=aln.a.aln.anchors[1].refpos+chrStart
		
	snplist=Any[]
	for (q,r) in collect(aln)	
		# matches and insertions in query advance reference index	
		if r == q || q == DNA_Gap 
			index+=1		
		# Mismatches are saved unless reference is a gap. 
		elseif r != q && r!= DNA_Gap 
			push!(snplist,(chrom,index+refstart-1,r,q))				
			index+=1
		else 
			println("DEBUG:",r,q)			
		end		
	end 
	return(snplist)
end

function parseargs()
	s = ArgParseSettings()
	s.description=
	"""
	**************************  WARNING ***************************
	FASTX/BioSequence is currently badly broken so computing the reverse alignmet
	is currently disabled.  This code will work OK so long as the two sequences are derived 
	from the same strand but will FAIL if one sequence is on the opposite strand of the other. 
	
	This happens because FASTA.sequence returns a StringView but reverse_complement requires
	some kind of BioSequence object, but neither FASX.jl nor BioSequences.jl provide ANY function
	to convert a String into a Sequence object. 
	
	**************************  WARNING ***************************
	
	
	Align two sequences selected from a multiple-fasta file.  
	
	alignPair.jl -fa1 chr6.fa -reg1 chr6:102356-123456 -fa2 hla_gen.fa -reg2 HLA0021356
	
	alignPair.jl -fa1 chr6.fa -reg1 chr6:122354-187882 -reg2 chr6:22787-29348
	
	alignPair.jl -fa1 hla_gen.fa -reg1 HLA002137 -reg2 HLA004445
	
	"""
	@add_arg_table s begin
		"--reg1","-r"
			help = "ID of first sequence"
			required=true		
		"--reg2","-s"
			help = "ID of second sequence"
			required=true			
		"--fa1","-f"
			help = "Fasta file 1"
			nargs = '+'
			required=true		
		"--fa2","-g"
			help = "Fasta file 2.  Default assumes reg1 and reg2 both come from fasta1."
			nargs = '+'
			required=false					
	end	
	return parse_args(s)
end

function readRecordDict(files,name2seq)		
	SEQ_TYPE = FASTA
	for fileName in files	
		if occursin("fq",fileName) || occursin("fastq",fileName)
			SEQ_TYPE = FASTQ
		end
	
		# If compressed decompress stream.
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
	end
	
	return(SEQ_TYPE)
end

function parseRegion(region::AbstractString)
	println(stderr,"CHECK0 region: ",region)
	chrom,coords= split(region,':')
	println(stderr,"CHECK1 chrom: ",chrom,"\tcoords: ",coords)
	start,stop = split(coords,'-')
	println(stderr,"CHECK2 start: ",start,"\tstop: ",stop)
	start = parse(Int,start)
	stop = parse(Int,stop)
	println(stderr,"CHECK3 start: ",start,"\tstop: ",stop)
	return chrom,start,stop
end
	
function getSeq(name2record,region)
	# If no range is given take entire sequence. 
	if occursin("-",region)		
		println(stderr,"region has a range: ",region)	
		chrom,rstart,rend = parseRegion(region)
		record = name2record[chrom]
		seq = FASTA.sequence(record)
		println(stderr,"getSeq seq type: ",typeof(seq))
		seq = seq[rstart:rend]
	else
		println(stderr,"region ",region," has no range, taking entire sequence.",region)
		record = name2record[region]
		seq = FASTA.sequence(record)
	end
	
	return seq	
end
	
function main()
	args = parseargs()
	
	# First sequence always comes from fa1.  
	fasta1_name2record = Dict()
	SEQ_TYPE1 = readRecordDict(args["fa1"],fasta1_name2record)
	aseq = getSeq(fasta1_name2record,args["reg1"])
	
	# Second sequence may come from a different file...
	# Also may or may not have coordinate range. 
	fasta2_name2record = Dict()
	if args["fa2"] != nothing
		println(stderr,"CHECK fa2 exists")
		SEQ_TYPE2 = readRecordDict(args["fa2"],fasta2_name2record)
		bseq = getSeq(fasta2_name2record,args["reg2"])
	else
		bseq = getSeq(fasta1_name2record,args["reg2"])
	end
	
	scoremodel = AffineGapScoreModel(EDNAFULL, gap_open=-5, gap_extend=-1);	
					
	# Don't know how they are oriented, so align both ways and take better score...
	respos = pairalign(LocalAlignment(),aseq,bseq,scoremodel)
	posscore = score(respos)
	
	bseq = LongDNA{4}(bseq) # Convert this string object to a sequence, required by reverse_complement
	revaseq = reverse_complement(bseq)
	resneg = pairalign(LocalAlignment(),revaseq,bseq,scoremodel)
	negscore = score(resneg)
	
	println(stderr,"Alignment score:        \t",posscore)
	println(stderr,"Reverse alignment score:\t",negscore)
	
	
	println(args["fa1"])
	println(args["fa2"])
	if negscore > posscore
		print(alignment(resneg))		
	else
		print(alignment(respos))
	end							
end	

main()

