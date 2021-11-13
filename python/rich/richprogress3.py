#!/usr/bin/env python
from rich.progress import track
from rich import print
from rich.progress import Progress
from rich.table import Column
from rich.progress import Progress, BarColumn, TextColumn,TimeRemainingColumn,SpinnerColumn,TimeElapsedColumn
from rich.console import Console

filename="big.fa"

seqCount=0
num_lines = sum(1 for line in open(filename,'r'))
print("num_lines:",num_lines)

console = Console(record=True)

progress =  Progress(
    SpinnerColumn(),
    TextColumn("[progress.description]{task.description}"),
    BarColumn(),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    TimeRemainingColumn(),
    TimeElapsedColumn(),
    console=console,
    transient=True,
)

with open(filename) as f:
    for line in track(f,total=num_lines):
        if ">" in line: 
            seqCount+=1
            print(line.strip(),seqCount)


