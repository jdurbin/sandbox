#!/usr/bin/env julia 
using CairoMakie

CairoMakie.activate!(type = "svg")
scene = scatter(rand(10,2),figure=(;resolution=(300,300)))
save("plot2.svg",scene)


# 55s
# julia --compile=min hello_svg.jl  27.43s