#!/usr/bin/env python 

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
pd.set_option('display.width', 1000)

# Read data
expression = pd.read_csv("../data/vijver2002.tab",delimiter="\t")
expression = expression.transpose()
print expression
print "Expression Shape:",expression.shape
print "Expression[0]:\n",expression.iloc[0] # This is the text heading
print "Expression[1]:\n",expression.iloc[1] # This is the first numeric row
print "Expression[295]:\n",expression.iloc[295] # This is the last row
print expression.values # This includes the first row of names 


# Read metadata
metadata = pd.read_csv("../data/vijver2002.clinical.t.tab",delimiter="\t")
print metadata.head(10)
print "Metadata shape:",metadata.shape        # 295 x 16

# numpy array way to combine columns, output is numpy array
#survival = np.c_[metadata['ID'],metadata['TIMEsurvival']]
survival = pd.DataFrame(metadata,columns = ['ID','TIMEsurvival'])
print survival # dataframe

print "Survival shape:",survival.shape

print "expression values: ",expression.values[1:,:] # cut out column headings
print "survival.values: ",survival.values[:,1:] # cut out row labels

# Split data into test and train datasets
exp_train,exp_test,surv_train,surv_test = train_test_split(expression.values[1:,:],
                                                            survival.values[:,1:],
                                                            train_size=0.8)
print "EXP TRAIN TYPE:",type(exp_train)
print "EXP TRAIN SHAPE:",exp_train.shape # (236,9803)
#print exp_test.shape   # (59,9803)
print "EXP TRAIN: \n",exp_train
print "SURV TRAIN SHAPE: ",surv_train.shape #(236,1)
print "SURV TRAIN RAVEL SHAPE: ",surv_train.ravel().shape #(236,)
print "SURV TRAIN TYPE: ",type(surv_train) # numpy.ndarray
print "SURV TRAIN: \n",surv_train


model = RandomForestClassifier(n_estimators = 100)
model = model.fit(exp_train,surv_train.ravel())

output = model.predict(exp_test)

print "OUTPUT:\n",output
print "OUTPUT TYPE:",type(output) # numpy.ndarray
print "OUTPUT SHAPE:",output.shape
print "surv_test:\n",surv_test

# So this outputs some kind of numeric value.  I don't know where it comes from in a 
# RandomForest.  Perhaps it treated it as a multi-value prediction... let's see if the numbers
# in the output are in the input...


# output size: 59
# intersection size: 49
print "INTERSCTION of OUTPUT and surv_train:\n",np.intersect1d(output,surv_train)
print "INTERSECTION shape:\n",np.intersect1d(output,surv_train).shape

# So, I think it's pretty clea that it's just a multi-class classifier using these real numbers 
# as 59 different output classes. 