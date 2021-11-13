#!/usr/bin/env python3

import os
import os.path
from os import path


def isLocalFile(filein): 
    # Is file a script in the current local directory? 
    cwd = os.getcwd()
    basename = path.basename(filein)
    testpath = f"{cwd}/{basename}"    
    return path.exists(testpath)
    
    
print(isLocalFile("samtools"))
print(isLocalFile("localfile.py"))
print(isLocalFile("pathparse.py"))