#!/usr/bin/env python3

import sys,argparse

parser = argparse.ArgumentParser("Some program")
parser.add_argument("-foo",help="Classic foo input")

args= parser.parse_args()

#type(args): <class 'argparse.Namespace'>
print(f"type(args): {type(args)}")