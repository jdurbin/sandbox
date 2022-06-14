#!/usr/bin/env python3

from fastcore.script import *
@call_parse
def main(msg:str,     # The message
         upper:bool): # Convert to uppercase?
    "Program to convert msg to upper case"
    print(msg.upper() if upper else msg)