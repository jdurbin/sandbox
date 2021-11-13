#!/usr/bin/env python

import traceback

def div(num, den):
    return num / den


try:
    print(div(2, 0))
except Exception:
    traceback.print_exc()