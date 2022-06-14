#!/usr/bin/env julia 
using Plots

x = 1:10; y = rand(10); # These are the plotting data
plot(x, y)
savefig("myplot.png")



# julia --compile=min hello1.jl  7.92s
