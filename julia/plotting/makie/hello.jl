#!/usr/bin/env julia

using CairoMakie

CairoMakie.activate!(type = "png")

x = range(0, 10, length=100)
y = sin.(x)
scene = lines(x, y)
save("plot.png",scene)