#!/usr/bin/env python3 

import csv
import numpy as np
import matplotlib.pyplot as plt

# Read in the tsv file and store the data in a list
data = []
with open('beer.tab') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
        data.append(row)

# Extract the price and calories columns from the data
price = [float(row[0]) for row in data]
calories = [float(row[1]) for row in data]

# Compute the correlation between the price and calories columns
corr = np.corrcoef(price, calories)[0][1]

# Plot a scatter plot of price vs calories
plt.scatter(price, calories)
plt.xlabel('Price')
plt.ylabel('Calories')
plt.title('Price vs Calories (r = {:.2f})'.format(corr))
plt.show()
