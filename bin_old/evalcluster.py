#!/usr/bin/env python3
import sys

fileIn = sys.argv[1]

# h2tg000020l	h1tg000006l	h1tg000039l	h2tg000023l	h1tg000320l	h2tg000206l	h1tg000350l	h1tg000010l	h1tg000239l	h1tg000174l	h2tg000223l	h1tg000229l	h2tg000187l	h2tg000330l	h1tg000336l	h2tg000235l	h2tg000366l	h1tg000331l	h2tg000267l	h1tg000231l	h1tg000186l	h2tg000374l	h2tg000425l	h1tg000259l	h2tg000136l	h1tg000490l	h2tg000207l	h1tg000497l	h1tg000238l	h2tg000019l	h1tg000121l	h1tg000281l	h2tg000365l	h2tg000433l	h1tg000198l	h2tg000311l	h1tg000177l	h2tg000392l	h2tg000044l	h1tg000399l	h1tg000471l	h1tg000416l	h2tg000281l	h2tg000112l	h1tg000318l	h1tg000390l	h2tg000333l	h1tg000382l	h1tg000361l	h1tg000395l	h1tg000463l	h2tg000174l	h1tg000393l	h1tg000383l	h1tg000523l	h2tg000234l	h1tg000250l	h1tg000315l	h2tg000229l	h1tg000397l	h2tg000265l	h2tg000417l	h2tg000372l	h1tg000404l	h2tg000338l	h1tg000367l	h1tg000359l	h2tg000212l	h1tg000403l	h2tg000176l	h2tg000405l	h1tg000432l	h1tg000398l	h1tg000446l	h1tg000334l	h2tg000350l	h1tg000408l	h1tg000443l	h1tg000258l	h2tg000415l	h1tg000379l	h2tg000474l	h2tg000429l	h2tg000379l	h1tg000261l	h2tg000427l	h1tg000381l	h2tg000271l	h2tg000423l	h1tg000193l	h1tg000509l	h1tg000156l	h2tg000430l	h2tg000238l	h1tg000414l	h1tg000289l	h1tg000417l	h2tg000178l	h2tg000475l	h1tg000313l

print("paternal\tmaternal\tfractionpat\tfractionmat")
with open(fileIn) as fin:
    for line in fin:
        mat=0
        pat=0        
        line = line.strip()
        fields = line.split("\t")
        for f in fields:    
            if "h1t" in f:
                pat+=1
            
            if "h2t" in f:
                mat+=1        
                                
        fracpat = round(pat/(pat+mat),2)
        fracmat = round(mat/(pat+mat),2)
        print(f"{pat}\t{mat}\t{fracpat}\t{fracmat}")                
        
