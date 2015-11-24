#!/usr/bin/env python

import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.metrics import confusion_matrix


# Pandas DataFrame is a bit like an R dataframe   
expression = pd.read_csv("data/vijver2002_t.tab",delimiter="\t",header = 0,index_col=0)
metadata = pd.read_csv("data/vijver2002.clinical.t.tab",delimiter="\t",header=0,index_col=0)

#print type(metadata) #<class 'pandas.core.frame.DataFrame'>

survival = metadata['TIMEsurvival']
survival = survival._get_numeric_data()

print "SURVIVAL: ",survival

#print type(survival) # pandas.core.series.Series

classifier = svm.SVC(gamma=0.001,C=100.)
classifier.fit(expression,survival)


predictions = classifier.predict(expression._get_numeric_data())


print "PREDICTIONS:",predictions

print confusion_matrix(predictions,survival)