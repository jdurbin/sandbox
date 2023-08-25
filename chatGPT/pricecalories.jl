#!/usr/bin/env julia 
using CSV, DataFrames, Statistics

# Read the TSV file into a DataFrame
df = DataFrame(CSV.File("beer.tab", delim='\t'))

# Compute the correlation between the price and calories columns
price_column = df[!,:price]
calories_column = df[!,:calories]
correlation = cor(price_column, calories_column)
correlation = round(correlation, digits=2)

# Print the correlation
println("Correlation between price and calories: ", correlation)

# Plot the price and calories columns as a scatter plot
using Plots
scatter(price_column, calories_column, xlabel="price", ylabel="calories")

# Save the scatter plot to a file
savefig("scatter.png")