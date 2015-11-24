#!/usr/bin/env python

from sklearn import datasets
from sklearn import svm
import pickle
#from sklearn.externals import joblib

iris = datasets.load_iris()
# sklearn.datasets.base.Bunch
#print iris.data
print iris.target

clf = svm.SVC(gamma=0.001,C=100.)

#clf.fit(iris.data[:-1],iris.target[:-1])
clf.fit(iris.data,iris.target)

predictions = clf.predict(iris.data)

print "predictions:",predictions



# Save the model for later. 
#pickle.dump(clf,open("modelspickle/iris.p","wb"))
#clf2 = pickle.load(open("modelspickle/iris.p","rb"))
#pred2 = clf2.predict(iris.data)
#print "pred2: ",pred2