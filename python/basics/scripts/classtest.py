#!/usr/bin/env python

#import SuperClass
# OK.. I think there is not a 1-1 correspondence between modules (files) and classes. 
# So import SuperClass just means to import the file/module. 
# If you want to import the class SuperClass from the file SuperClass, you need something like:
from SuperModule import SuperClass

# I presume this also means that the file could have some unrelated name... yep! 
# OK, got it.  

sc = SuperClass()
print sc.superAwesomeFunction(5)

# Interrogate the class..
# Is this really the most succinct way to show this...
#print 'The name of class for sc is: {}'.format(sc.__class__.__name__)
print 'The name of class for sc is:',sc.__class__.__name__
