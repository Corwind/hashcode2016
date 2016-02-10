#!/usr/bin/python
import sys
from pprint import pprint as print


def parse(f):
    l = []
    with open(f, 'r') as fi:
        n, m = map(int, fi.readline().split())
        for i in range(n):
            l.append(list(fi.readline().strip()))
    print(len(l))
    return l


if __name__ == "__main__":
    s, f = sys.argv
    parse(f)
