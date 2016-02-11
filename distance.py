#!/usr/bin/python3

from math import *

def get_distance(o1, o2):
    return ceil(sqrt(pow(abs(o1.line - o2.line), 2) + pow(abs(o1.col - o2.col), 2)))
