#!/usr/bin/env python 

import numpy as np
import pandas as pd
import sys


filename = sys.argv[1]

df = pd.read_csv(filename,delimiter="\t",header = 0)
print df.shape


# engine="python"
#(11650, 5373)
# real	0m43.677s

# engine="c"
#(11650, 5373)
#real	0m15.324s

# engine omitted for default
#(11650, 5373)
#real	0m15.033s

# engine="c"
#(11650, 8294)
# real	0m30.269s