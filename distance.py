#!/usr/bin/python3

from math import *

def get_distance(ra, rb, ca, cb):
    return ceil(sqrt(pow(abs(ra-rb), 2) + pow(abs(ca-cb), 2)))
