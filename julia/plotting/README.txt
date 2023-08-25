
################
# Plots.jl
################

# Julia 1.7
# Ten point line plot
./hello1.jl  12.82s
# julia --compile=min hello1.jl  7.92s

# So pretty notable improvement with julia 1.8 
# julia 1.8 ./hello1.jl  9.67s
# julia --compile=min hello1.jl  6.86s

Supposedly early entry that maybe lacking in usability.  
It's just an interface for other software?  Often Python software?

################
# VegaLite
################
Julia 1.7 
./hello.jl  16.76s
Feels pretty slow. 
With compile=min:
hello.jl  7.42s

Julia 1.8 (note, tested on battery... repeat on power)
./hello.jl  11.09s
julia --compile=min hello.jl  10.84s

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

Julia 1.8 (bttery):
./hello.jl  54.78s (loaded some web pages at same time)
julia --compile=min ./hello.jl  49.15s

################
# makie
################

Plots.jl 13s, VegaLite 17s, GadFly 28s, CairoMakie 52s

