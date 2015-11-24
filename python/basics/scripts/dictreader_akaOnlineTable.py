#!/usr/bin/env python

import csv

with open('beer.tab') as bobTheFile:
    reader = csv.DictReader(bobTheFile,delimiter='\t')        
    for row in reader:
        print row['price']


# Just to test my understanding... bobTheFile is just a handle
# for the opened file, so could rearrange like...
bobTheFile = open('beer.tab')
with bobTheFile:
    reader = csv.DictReader(bobTheFile,delimiter='\t')        
    for row in reader:
        print row['brand']
        
# How about this...
reader = csv.DictReader(open('beer.tab'),delimiter="\t")
for row in reader:
    print row['domestic']
    
    
# Yep, all of that works just fine... 
