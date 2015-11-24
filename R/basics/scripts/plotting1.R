
library(lattice)

# Creating a Graph
attach(mtcars)
plot(wt, mpg) 
abline(lm(mpg~wt))
title("Regression of MPG on Weight")


# Simple Histogram
hist(mtcars$mpg)

# Simple Dotplot
dotchart(mtcars$mpg,labels=row.names(mtcars),cex=.7,
  	main="Gas Milage for Car Models", 
   xlab="Miles Per Gallon")
   
# Boxplot of MPG by Car Cylinders 
boxplot(mpg~cyl,data=mtcars, main="Car Milage Data", 
     	xlab="Number of Cylinders", ylab="Miles Per Gallon")
		
# Simple Scatterplot
plot(wt, mpg, main="Scatterplot Example", 
	xlab="Car Weight ", ylab="Miles Per Gallon ", pch=19)
	
# Add fit lines
abline(lm(mpg~wt), col="red") # regression line (y~x) 
lines(lowess(wt,mpg), col="blue") # lowess line (x,y)

# Basic Scatterplot Matrix (better ones in Lattice, car, and gclus packages)
pairs(~mpg+disp+drat+wt,data=mtcars, 
   main="Simple Scatterplot Matrix")
   
   
# hexbin high density scatter plots

