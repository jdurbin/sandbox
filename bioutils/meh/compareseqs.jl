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
	Align two sequences selected from a multiple-fasta file.  
	"""
	@add_arg_table s begin
		"--aseq","-a"
			help = "ID of first sequence"
			required=true		
		"--bseq","-b"
			help = "ID of second sequence"
			required=true			
		"--querydb","-q"
			help = "Query database of sequences"
			nargs = '+'
			required=true				
#		"--chromstart","-c"
#			help = "Chromosome start"
#			default = "0"
#			required = false 
	end	
	return parse_args(s)
end

function readRecordDict(files,name2seq)		
	SEQ_TYPE = FASTA
	for fileName in files	
		if occursin("fq",fileName) || occursin("fastq",fileName)
			SEQ_TYPE = FASTQ
		end
	
		reader = SEQ_TYPE.Reader(GzipDecompressorStream(open(fileName)))		
		print(stderr,"Reading ",fileName,"...")	
		for record in reader
			name2seq[SEQ_TYPE.identifier(record)]=record
		end
		println(stderr,length(name2seq)," sequences read.")	
	end
	
	return(SEQ_TYPE)
end
	
	
function main()
	args = parseargs()
	
	allelename2seq = Dict()
	SEQ_TYPE= readRecordDict(args["querydb"],allelename2seq)
	
	scoremodel = AffineGapScoreModel(EDNAFULL, gap_open=-5, gap_extend=-1);	
	# Align hla type sequence to reference region			
	arecord=allelename2seq[args["aseq"]]	
	aseq = SEQ_TYPE.sequence(arecord)			
	brecord=allelename2seq[args["bseq"]]
	bseq = SEQ_TYPE.sequence(brecord)
					
	# Don't know how they are oriented, so align both ways and take better score...
	respos = pairalign(LocalAlignment(),aseq,bseq,scoremodel)
	posscore = score(respos)
	
	revaseq = reverse_complement(aseq)
	resneg = pairalign(LocalAlignment(),revaseq,bseq,scoremodel)
	negscore = score(resneg)
	
	println(stderr,"Alignment score:        \t",posscore)
	println(stderr,"Reverse alignment score:\t",negscore)
	
	
	println(args["aseq"])
	println(args["bseq"])
	if negscore > posscore
		println(resneg)		
	else
		println(respos)		
#		chrom="chr6"
#		chrStart = parse(Int,args["chromstart"])
#		if chrStart != 0
#			println("SNPS:")
#			snps = getSNPListFromAlignment(alignment(respos),chrom,chrStart)
#			for (chrom,loc,r,q) in snps
#				println(chrom,":",string(loc),":",string(r),":",string(q))
#			end
#		end				
	end							
end	


main()

# bedfile B Start: 31351875
# bedfile B End: 31359179	
# Size: 
# minimap B start: 31353599
# minimap B end:  31357442

# 50 sequences:
# real	0m4.318s
# 100 alignments:
# real	0m6.165s
# 500 alignments:
# real	0m10.336s.  Not bad

