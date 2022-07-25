#!/usr/bin/env python3

import sys,argparse

parser = argparse.ArgumentParser()
parser.add_argument('-foo', nargs='+', help='foo values', required=False)
parser.add_argument('-bar',required=False)

args = parser.parse_args()

for foo in args.foo:
    print("foo: ",foo)
    
if args.bar:
    print(f"bar, baby!  bar is {args.bar}")
else:
    print("Sadly, no bar")