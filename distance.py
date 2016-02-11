#!/usr/bin/python3

def get_distance(ra, rb, ca, cb):
    return sqrt(pow(abs(ra-rb), 2) + pow(abs(ca-cb), 2))
