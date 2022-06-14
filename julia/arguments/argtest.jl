#!/usr/bin/env julia

using ArgParse

function parseargs()
	s = ArgParseSettings()
	s.description=
	"""
	Program to do something amazing.
	"""
	@add_arg_table s begin
		"--reference","-r"
			help = "Reference sequence to use"
			required=true		
		"--querydb","-q"
			help = "Query database of sequences"
			required=true		
		"--snpsout","-s"
			help = "Name of output SNP file."		
			required=true		
		"--reverse"
			help = "Reverse complement sequence"
			action = :store_true
	end	
	return parse_args(s)
end



function main()
	parsed_args = parseargs()
	println("Parsed args: ")
	for (arg,val) in parsed_args
		println("  $arg  ==>   $val")
	end
	
	println("Reference: ",parsed_args["reference"])
end



main()