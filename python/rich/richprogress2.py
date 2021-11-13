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

with Progress(
    SpinnerColumn(),
    TextColumn("[progress.description]{task.description}"),
    BarColumn(),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    TimeRemainingColumn(),
    TimeElapsedColumn(),
    console=console,
    transient=True,
) as progress:
    task1 = progress.add_task("[green]Reading FASTA",total=num_lines)

    with open(filename) as f:
        for line in f:
            progress.update(task1,advance=1)
            if ">" in line: 
                seqCount+=1
                progress.log(line.strip(),seqCount)


