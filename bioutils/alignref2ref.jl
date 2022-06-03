#!/usr/bin/env -S julia
using FASTX,BioAlignments,BioSequences,ArgParse

function parseargs()
	s = ArgParseSettings()
	s.description=
	"""
	Align one fasta vs another. 
	"""
	@add_arg_table s begin
		"--seq","-s"
			help = "Reference sequence to use"
			required=true
		"--refregion","-r"
			help="Ref region"
			required=true
		"--queryregion","-q"
			help = "Query region"
			required=true	
	end	
	return parse_args(s)
end

function parseRegion(rstr)
	sstart,send = split(rstr,":")
	return (parse(Int,sstart),parse(Int,send))
end
	
function main()
	args = parseargs()
			
	# Read reference and extract region...
	record = FASTA.Record()
	reader = open(FASTA.Reader,args["seq"])
	read!(reader,record)
	close(reader)

	seq = FASTA.sequence(record)
	rstart,rend = parseRegion(args["refregion"])	
	refseq = seq[rstart:rend]
	qstart,qend = parseRegion(args["queryregion"])
	qseq = seq[qstart:qend]
	
	scoremodel = AffineGapScoreModel(EDNAFULL, gap_open=-5, gap_extend=-1);	

	#if args["reverse"] reverse_complement!(hlaref) end	
	res = pairalign(LocalAlignment(),refseq,qseq,scoremodel)
	println(res)	
end

main()

