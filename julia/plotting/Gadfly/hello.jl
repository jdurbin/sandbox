#!/usr/bin/env julia 

using Gadfly, RDatasets
iris = dataset("datasets", "iris")

p = plot(iris, x=:SepalLength, y=:SepalWidth, Geom.point);

img = SVG("iris_plot.svg", 14cm, 8cm)
draw(img, p)


# Look at this, coloring by species.  
p2 = plot(iris, x=:SepalLength, y=:SepalWidth, color=:Species, Geom.point);
img2 = SVG("iris_plot2.svg", 14cm, 8cm)
draw(img2, p2)

# Egads. 
# ./hello.jl  42.91s

# Same time for 2 plots, though. 
# ./hello.jl  49.89s