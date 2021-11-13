#!/usr/bin/env python
from time import sleep

from rich.table import Column
from rich.progress import Progress, BarColumn, TextColumn

total=0
with Progress() as progress:
    task = progress.add_task("twiddling thumbs", total=10)
    for job in range(10):
        progress.console.print(f"Working on job #{job}")
        total+=10
        progress.advance(task)
        
