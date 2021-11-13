#!/usr/bin/env python3

import sys
import pandas as pd
import argparse

def parseArgs(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-dfs", required=True, default=None, nargs="+")
    parser.add_argument("-output", required=True)
    args = parser.parse_args()
    return args
    

def main(argv):
    args = parseArgs(argv)

    masterdf = pd.DataFrame()
    for fname in args.dfs:
        rootname = fname.replace(".tab","")
        df = pd.read_csv(fname,sep="\t",names=[f'{rootname}_x',f'{rootname}_y'])
        masterdf = pd.concat([masterdf,df],axis=1)

    masterdf.to_csv(args.output, index=False,sep="\t")



if __name__ == "__main__":
    main(sys.argv)