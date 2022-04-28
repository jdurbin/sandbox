
################
# Plots.jl
################

# Ten point line plot
./hello1.jl  12.82s

# julia --compile=min hello1.jl  7.92s


Supposedly early entry that maybe lacking in usability.  
It's just an interface for other software?  Often Python software?

################
# VegaLite
################
./hello.jl  16.76s

Feels pretty slow. 

With compile=min:
hello.jl  7.42s

################
# GadFly.jl 
################
Pretty slow start up, like 40s.  Need to see how much is RDatasets, etc.
	# Load iris data alone. 
	# ./hello.jl  15.18s
	# With using Gadfly
	# hello.jl  20.15s
	# entire first plot. 
	# 48.74
	# So plotting is about 28 seconds. 
 
Plots are nice. 
Their description of their jupyter support is more encouraging. 
Integration with DataFrames.jl 
Supports some interactive visualization. 


################
# makie
################


Plots.jl 13s, VegaLite 17s, GadFly 28s, CairoMakie 52s

