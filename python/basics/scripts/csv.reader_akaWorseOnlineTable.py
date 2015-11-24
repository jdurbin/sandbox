#!/usr/bin/env python

import scipy
import pylab
import csv
import sys
# WTH does this do?  I try to import pprint and get error. 
# 
from pprint import pprint as p 

# Reading a csv file... OK, but it's not yet up to OnlineTable standards...
with open("beer.tab") as tsv:
    for line in csv.reader(tsv, dialect="excel-tab"):
        print line[1]
        
print "Script running under Python:"+sys.version        
        
# Supposedly anything in sys.path can be picked up as a module
# what is sys.path?
# print sys.path    works fine
p(sys.path) # prettier... a bit...

# OK, try out my module...
superlib.sayhi()