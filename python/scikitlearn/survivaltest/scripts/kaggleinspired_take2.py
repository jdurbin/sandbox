#!/usr/bin/env python 

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.pipeline import Pipeline

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
exp_train,exp_test,surv_train,surv_test = train_test_split(expression.values[1:,:],
                                                           survival,
                                                           train_size=0.8)

model = RandomForestClassifier(n_estimators = 100)
model = model.fit(exp_train,surv_train.ravel())
output = model.predict(exp_test)

print "OUTPUT:\n",output
print "surv_test:\n",surv_test.ravel()

print "CONFUSION MATRIX:\n",confusion_matrix(surv_test,output)
print "PRECISON:",precision_score(surv_test,output)