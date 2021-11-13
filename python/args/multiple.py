#!/usr/bin/env python3

import sys,argparse

parser = argparse.ArgumentParser()
parser.add_argument('-foo', nargs='+', help='foo values', required=False)

args = parser.parse_args()

for foo in args.foo:
    print("Foo: ",foo)