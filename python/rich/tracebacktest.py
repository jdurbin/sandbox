#!/usr/bin/env python

from rich.console import Console

console = Console()

def div(num, den):
    return num / den

try:
    print(div(2, 0))
except:
    console.print_exception()