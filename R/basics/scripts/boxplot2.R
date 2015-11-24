#!/usr/bin/env Rscript

# What to o when you subset data and want that data not to show up?

# convert cyl to a factor
mtcars$cyl <- as.factor(mtcars$cyl)
# The normal boxplot
boxplot(mpg ~ cyl, data = mtcars)
# With one of the levels missing we see the same problem you have
boxplot(mpg ~ cyl, data = mtcars, subset = cyl != "6")
# Create a dataset with the subset of interest
newdat <- mtcars[mtcars$cyl != "6",]
# Examine to make sure we don't have any 6s left
summary(newdat$cyl)
# Use droplevels to remove the empty levels from the list of levels
newdat$cyl <- droplevels(newdat$cyl)
# Now it looks better
boxplot(mpg ~ cyl, data = newdat)