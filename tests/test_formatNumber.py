"""
Copyright (C) 2021 SE Slash - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: secheaper@gmail.com

"""
import os
import sys
import inspect
import math

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import src.formattr as formatter


def test_getNumbers():
    """
    Checks the getNumbers function
    """
    assert formatter.getNumbers("some chars and $10.00") == 10.0
    assert formatter.getNumbers("some chars and $10.99 some other chars") == 10.99
    assert formatter.getNumbers("") == math.inf
