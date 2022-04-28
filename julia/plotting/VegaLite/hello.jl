#!/usr/bin/env -S julia --compile=min

using VegaLite, VegaDatasets

# p = dataset("cars") |> @vlplot(:bar, x="count()", y=:Origin)

p = dataset("cars") |>
       @vlplot(
           :point,
           x=:Horsepower,
           y=:Miles_per_Gallon,
           color=:Origin,
           width=400,
           height=400
       )

save("myplot.svg", p)

#  Time: 
# ./hello.jl  12.42s


# @time using VegaLite, VegaDatasets
# 3.722158 seconds. using
# 2.087367 seconds	vplot
# 3.784914 seconds	save
# 9.4 seconds

# 2nd run:
# 0.004162 seconds vplot (includes near instantaneous open of webpage with plot)
# 2.814209 seconds save
# 

# And who can even explain this?: 
# back to back: 
# julia> @time save("myplot2.svg", p)
#   2.814209 seconds (234.42 k allocations: 7.033 MiB)
# 
# julia> @time save("myplot3.svg", p)
#   3.642300 seconds (234.41 k allocations: 7.033 MiB)
# 
# julia> @time save("myplot4.svg", p)
#   2.916682 seconds (234.41 k allocations: 7.033 MiB)