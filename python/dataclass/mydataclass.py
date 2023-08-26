from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import logging
from scipy.stats import fisher_exact
from typing import ClassVar, TextIO


@dataclass
class PhaseCounts:
    hlatype: str
    
    @property
     def genotype(self):
         return self.hlatype
        
    @classmethod
    def load():
        datastr = "A:B:C:D"
        genotype, name, n1,n2 = datastr.split(":")
        
        
        


