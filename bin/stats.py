#!/usr/bin/env python
import numpy,sys

# Compute basic statistics on set of  numbers piped in from stdin

data = numpy.array([float(line.strip()) for line in sys.stdin])

print("N:", len(data))
print("Min:", numpy.min(data))
print("Max:", numpy.max(data))
print("Mean:", round(numpy.mean(data),4))
print("Median:", numpy.median(data))
print("STD:", round(numpy.std(data),4))
print("Coeficient of Variation:", round(numpy.std(data) / numpy.mean(data),4))
print("Sum:", numpy.sum(data))