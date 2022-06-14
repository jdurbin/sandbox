#!/usr/bin/env julia 

open("test.txt","w") do fout
	write(fout,"Hello World!\n")
end