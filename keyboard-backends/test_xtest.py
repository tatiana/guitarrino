#!/usr/bin/env python

# Actually it does not work - we can't make key F1 work (other keys working)
# sudo aptitude install python-pip python-pyrex
# sudo pip install xtest


import xtest
import time


fake = xtest.XTest()

start = time.time()
fake.fakeKeyEvent(key='A')
end = time.time()
print end - start
