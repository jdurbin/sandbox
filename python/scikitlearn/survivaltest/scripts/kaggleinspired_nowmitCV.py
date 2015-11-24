#!/usr/bin/env python 

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn import cross_validation

pd.set_option('display.width', 1000)

# Read data
expression = pd.read_csv("../data/vijver2002.tab",delimiter="\t")
expression = expression.transpose()


# Read metadata
metadata = pd.read_csv("../data/vijver2002.clinical.t.tab",delimiter="\t")

# numpy array way to combine columns, output is numpy array
#survival = np.c_[metadata['ID'],metadata['TIMEsurvival']]
survival = pd.DataFrame(metadata,columns = ['ID','TIMEsurvival'])
survival = survival.values[:,1:] # now I've converted it to a ndarray...


# Survival is numeric.  Do a simple conversion to above/below mean. 
meanSurvival = np.mean(survival)
survival[survival < meanSurvival] = 0
survival[survival >= meanSurvival] = 1

survival = survival.astype(bool)

# Split data into test and train datasets
#exp_train,exp_test,surv_train,surv_test = train_test_split(expression.values[1:,:],
#                                                           survival,
#                                                           train_size=0.8)

model = RandomForestClassifier(n_estimators = 100)

exp_vals = expression.values[1:,:]
print "EXPRESSION VALS SHAPE: ",exp_vals.shape
#print "EXPRESSION VALS: \n",exp_vals
print "SURVIVAL SHAPE: ",survival.ravel().shape
scores = cross_validation.cross_val_score(model,exp_vals,survival.ravel(),cv=5,scoring='roc_auc')
print "RAW ROC AUC VALUES: ",scores
print("ROC AUC: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
