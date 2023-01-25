#!/usr/bin/env python3
import sys,argparse

myglobal=None

def parseArgs(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-foo", required=True,help="Global variable")

    args = parser.parse_args()
    return args   

def myfunction():
    print("My global is: ",myglobal)


def main(argv):
    args = parseArgs(argv)
    global myglobal
    myglobal = args.foo
    
    myfunction()
    

    

if __name__ == "__main__":
    main(sys.argv)