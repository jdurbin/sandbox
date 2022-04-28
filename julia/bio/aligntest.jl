#!/usr/bin/env -S julia
using FASTX,BioAlignments,BioSequences,ArgParse



function main()
	scoremodel = AffineGapScoreModel(EDNAFULL, gap_open=-5, gap_extend=-1);	
	
	
	
end




main()