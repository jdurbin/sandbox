using CSV, DataFrames

fname = only(ARGS)
df = CSV.File(fname) |> DataFrame
println(first(df, 3))


# W/o daemon: 
# julia test.jl tsp_50.csv  11.65s

# time juliad test.jl tsp_50.csv
# 0.59s

