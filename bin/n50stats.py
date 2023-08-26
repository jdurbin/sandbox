#!/usr/bin/env python3
#!/usr/bin/env python3
from __future__ import division
from __future__ import print_function
from past.utils import old_div
import sys
import argparse

def n50list(buffer,N=False,verbose=False,print_num=False):
    buffer.sort(reverse=True)
    tot=sum(buffer)
    if N:
         c=0.0
         i=0
         for n in buffer:
             c+=n
             i+=1
             if (1.0-old_div(c,tot))<(1.0 - (old_div(N,100.0))):
                 if verbose: 
                     if print_num:
                         print("\t".join(map(str,[n,i])))
                     else:
                         print(n) #,c,tot-c,1.0-c/tot
                 else: 
                     return(n)
                 break
    else:
        n50recs=[]
        c=0.0
        i=0
        for n in buffer:
            c+=n
            i+=1
            if verbose: print(i,n,c,tot-c,1.0-old_div(c,tot))
            n50recs.append( (i,n,c,tot-c,1.0-(c/tot)) )
        return n50recs

def n50(fh,N=False,verbose=False,column=0,filterstr=False,print_num=False):
    result=[]
    buffer=[]
#    tot=0.0
    while True:
        l = fh.readline()
        if not l:
            break
        if l[0]=="#": continue        
        if filterstr and not filterstr in l: continue
        c=l.strip().split()
        x=float(c[column])
#        tot+=x
        buffer.append(x)

    return n50list(buffer,N,verbose,print_num)
    
def l50list(buffer,N=False,verbose=False):
    buffer.sort(reverse=True)
    tot=sum(buffer)
    if N:
         c=0.0
         i=0
         for n in buffer:
             c+=n
             i+=1
             if (1.0-old_div(c,tot))<(1.0 - (old_div(N,100.0))):
                 if verbose: 
                     print(i) #,c,tot-c,1.0-c/tot
                 else: 
                     return(i)
                 break
    else:
        n50recs=[]
        c=0.0
        i=0
        for n in buffer:
            c+=n
            i+=1
            if verbose: print(i,n,c,tot-c,1.0-old_div(c,tot))
            n50recs.append( (i,n,c,tot-c,1.0-(c/tot)) )
        return n50recs

def l50(fh,N=False,verbose=False,column=0,filterstr=False):
    result=[]
    buffer=[]
#    tot=0.0
    while True:
        l = fh.readline()
        if not l:
            break
        if l[0]=="#": continue        
        if filterstr and not filterstr in l: continue
        c=l.strip().split()
        x=float(c[column])
#        tot+=x
        buffer.append(x)

    return l50list(buffer,N,verbose)

    


def main():

    parser = argparse.ArgumentParser()

    #parser.add_argument('-i','--input')
    parser.add_argument('-d','--debug',default=False,action="store_true")
    parser.add_argument('-p','--progress',default=False,action="store_true")
    parser.add_argument('-i','--infile',default=False)
    parser.add_argument('-c','--col',default=False,type=int)
    parser.add_argument('-N',metavar='X',default=False,type=float,help="e.g. X=50 for N50 size")
    parser.add_argument('-P','--pretty',default=False,action="store_true",help="Generate a short human-readable summary.")
    parser.add_argument('-l','--print-l',default=False,action="store_true",help="Print LX in addition to N") 

    #parser.add_argument('-L','--length',default=False,type=int)

    args = parser.parse_args()
    if args.progress: print("#",args)

    if args.infile:
        fh=open(args.infile,"r")
    else:
        fh=sys.stdin

    c=0
    if args.col: c=args.col

    if args.pretty:
        recs = n50(fh,args.N,verbose=False,column=c)
        i=0
        while recs[i][4]>0.5: i+=1
        print("Total number of sequences : {: 15,}".format(recs[-1][0]))
        print("Total length of sequences : {: 15,} bp".format(int(recs[-1][2])))
        print("Longest sequence length   : {: 15,} bp".format(int(recs[0][1])))
        print("N50 sequence length       : {: 15,} bp".format(int(recs[i][1])))
#i,n,c,tot-c,1.0-(c/tot)

    else:
        r=n50(fh,args.N,verbose=True,column=c,print_num=args.print_l)
    


if __name__=="__main__":
    main()
