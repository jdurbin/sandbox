#!/usr/bin/env julia

using Cooler


coolName = "MB286.mcool"
startCoord=1000
endCoord = 10000000
resolution = "resolutions/1000"

matrix = Cooler.matrix(coolName,startCoord,endCoord,resolution)
println(length(matrix))