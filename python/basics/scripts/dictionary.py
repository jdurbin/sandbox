#!/usr/bin/env python

m = {'foo':40,'bar':9000,'killroy':100000}

print m['bar']

s = set()
s.add('foo')
s.add('foo')
s.add('bar')

print s

print 'foo' in s
print 'mary' in s
