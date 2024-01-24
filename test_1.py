'''
    improve pylint score1
'''

import os, sys

sys.path.insert(0, os.getcwd())

from script import addition


def test_add():
    
    ''' improve pylint score  '''

    x = addition(25, 75)
    print("Value of x = ", x)
    assert x == 100


test_add()
