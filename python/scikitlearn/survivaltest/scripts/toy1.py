#!/usr/bin/env python 

import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.metrics import confusion_matrix

data = pd.DataFrame({'pet':      ['cat', 'dog', 'dog', 'fish', 'cat', 'dog', 'cat', 'fish'],
                     'children': [4., 6, 3, 3, 2, 3, 5, 4],
                     'salary':   [90, 24, 44, 27, 32, 59, 36, 27]})
                     

