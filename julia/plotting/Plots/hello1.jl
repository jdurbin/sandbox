#!/usr/bin/env julia 
using Plots

x = 1:10; y = rand(10); # These are the plotting data
plot(x, y)
savefig("myplot.png")


# julia 1.7  ./hello1.jl  12.82s
# julia 1.7 --compile=min hello1.jl  7.92s


# So pretty notable improvement with julia 1.8 
# julia 1.8 ./hello1.jl  9.67s
# julia --compile=min hello1.jl  6.86s