#!/usr/bin/env julia 


mutable struct Person
	name
	height
	position
end

function displace!(p,delta)
	p.position = p.position+delta
end

me = ("Leandro","1.80",0.)

# Don't know why this code fails if I put this line in this file. 
# If I type all of this into REPL it works.  
displace!(me,2.)
