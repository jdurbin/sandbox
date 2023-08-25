#!/usr/bin/env python3 

# import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# read in the tsv file
df = pd.read_csv("beer.tab", sep="\t")

# compute the correlation between price and calories
corr = df["price"].corr(df["calories"])

# print the correlation
print("The correlation between price and calories is: ", corr)

# create a scatter plot of price vs calories
plt.scatter(df["price"], df["calories"])
plt.xlabel("Price")
plt.ylabel("Calories")
plt.title("Price vs Calories")
plt.show()


# Straight out of chatGPT
# Only changes were adding shebang and making file name beer.tab. 

# Prompt:  write a python program to read in a tsv file and compute 
# the correlation between the price and calories columns, then plot 
# a scatter plot of price vs calories. 

# The first version was based on numpy and didn't use named columns. 
# Version three is this one but was presented as a description not 
# as code.  I asked it to convert it to code and got this program. 