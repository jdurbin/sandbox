#!/usr/bin/env python3 

from fastcore.script import *
@call_parse
def main(bam:str,   # Bam file to use
         r="chr1:1-2000",    # Region to extract         
         pairs:bool):   # Whether to output pairs                           
    "Extract region from bamfile (optionally including pairs outside of region.)"

    print("hello")
