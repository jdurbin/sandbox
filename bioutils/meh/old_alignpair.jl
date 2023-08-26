#!/usr/bin/env -S julia -t 10
using FASTX,BioAlignments,BioSequences,ArgParse,CodecZlib

function parseargs()
	s = ArgParseSettings()
	s.description=
	"""
	Aligns two single fasta files.  	
	"""
	@add_arg_table s begin
		"--fasta1","-f"
			help = "First fasta file"
			required=true		
		"--fasta2","-g"
			help = "Second fasta file"
			required=true			
	end	
	return parse_args(s)
end


function main()
	args = parseargs()
			
	sequence1 = FASTA.Reader(open(args["fasta1"])) do reader
	    record = first(reader)
	    seq = FASTA.sequence(record)
	end
	
	sequence2 = FASTA.Reader(open(args["fasta2"])) do reader
	    record = first(reader)
		FASTA.sequence(record)
	end

					
	scoremodel = AffineGapScoreModel(EDNAFULL, gap_open=-5, gap_extend=-1);						
	# Don't know how they are oriented, so align both ways and take better score...
	respos = pairalign(LocalAlignment(),sequence1,sequence2,scoremodel)
	posscore = score(respos)
	
	#revseq1 = reverse_complement(sequence1)
	#resneg = pairalign(LocalAlignment(),revseq1,sequence2,scoremodel)
	#negscore = score(resneg)
	negscore = -9999999
	println(stderr,"Alignment score:        \t",posscore)
	#println(stderr,"Reverse alignment score:\t",negscore)
	
	
	println(args["fasta1"])
	println(args["fasta2"])
	if negscore > posscore
		println(alignment(resneg))		
	else
		println(alignment(respos))				
	end							
end	


main()


#  ~/src/sandbox/bioutils/alignpair.jl --fasta1 HLA00522_04.fa --fasta2 HLA02047_105.fa > HLA00522_04_vs_HLA02047_105.txt