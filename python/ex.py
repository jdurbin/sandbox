
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# With header, you are in business
df = pd.read("myfile.bed","\t")

# With no header, tell it, then headings will be 0,1,2,3.  Otherwise it'll be first row of your data!
df=pd.read_csv("bY.bed","\t",header=None)

# Or you can pick some columns and give them names
df = pd.read_csv("myfile.bed", usecols=[3,6], names=['colA', 'colB'])

hist = df.hist(column=7)

# Because Python has a fucked idea about variable scoping and object identity, 
# this just magically knows aobut the plot above which, to repeat myself, is totally
# janky shit.  
plt.show()