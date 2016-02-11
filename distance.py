#!/usr/bin/python3

from math import *

def get_distance(ra, rb, ca, cb):
    if ra < 0 or rb < 0 or ca < 0 or cb < 0:
        print('COORDONNÉE NÉGATIVE WESH')
        return -1
    return ceil(sqrt(pow(abs(ra-rb), 2) + pow(abs(ca-cb), 2)))
