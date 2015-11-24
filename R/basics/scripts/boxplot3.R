#!/usr/bin/env Rscript

bymedian <- with(InsectSprays, reorder(spray, -count, median))
bymedian


boxplot(count ~ bymedian, data = InsectSprays,
         xlab = "Type of spray", ylab = "Insect count",
         main = "InsectSprays data", varwidth = TRUE,
         col = "lightgray")