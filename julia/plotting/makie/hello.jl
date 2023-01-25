#!/usr/bin/env julia

using CairoMakie

CairoMakie.activate!(type = "png")

x = range(0, 10, length=100)
y = sin.(x)
scene = lines(x, y)
save("plot.png",scene)


# Julia 1.8 (battery)
# ./hello.jl  37.01s
# julia --compile=min hello.jl  33.78s