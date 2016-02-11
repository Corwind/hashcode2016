#!/usr/bin/python3

import sys
from poney import parse

def paint_lol(m, out):
    l = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == '#':
                l.append('PAINT_SQUARE {} {} 0\n'.format(i, j))
    with open(out, 'w') as o:
        o.write('{}\n'.format(len(l)))
        o.writelines(l)

if __name__ == "__main__":
    s, f, o = sys.argv
    paint_lol(parse(f), o)
