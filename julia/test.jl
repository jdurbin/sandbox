#!/usr/bin/env julia 

import Pkg
#Pkg.add("Plots")
#Pkg.add("GR")
#Pkg.add("PlotlyBase")

using Plots

x = 1:10; y = rand(10, 2) # 2 columns means two lines
println(x)
println(y)
#plotly() # Set the backend to Plotly
# This plots into the web browser via Plotly
#gr()
plotly()

plt = plot(x, y, title = "This is Plotted using Plotly")
display(plt)