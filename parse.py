#!/usr/bin/python3

"""
Written by dore_g
"""

import sys
from pprint import pprint as print

class Infos:
    def __init__(self, turns, warehouses, drones, orders, wgs):
        self.warehouses = warehouses
        self.turns = turns
        self.weights = wgs
        self.drones = drones
        self.orders = orders

class Warehouse:
    def __init__(self, stock, line, col):
        self.stock = stock
        self.line = line
        self.col = col

class Order:
    def __init__(self, pdts, line, col):
        self.products = {}
        for i in pdts:
            try:
                self.products[i] += 1
            except:
                self.products[i] = 1
        self.line = line
        self.col = col

class Drone:
    def __init__(self, weight, line, col):
        self.weight = weight
        self.line = line
        self.col = col
def parse(f):
    orders = []
    wh = []
    drones = []
    with open(f, 'r') as fi:
        lines, cols, t, dr, p = map(int, fi.readline())
        pt = int(fi.readline())
        pw = map(int, fi.readline())
        nw = int(fi.readline())
        for i in range(nw):
            line, col = map(int, fi.readline())
            stock = map(int, fi.readline())
            wh.append(Warehouse(stock, line, col))
        o = int(fi.readline())
        for i in range(o):
            line, col = map(int, fi.readline())
            nb = int(fi.readline())
            prods = map(int, fi.readline())
            orders.append(Order(prods, line, col))
        for i in range(dr):
            drones.append(p, wh[0].line, wh[0].col)
    return Infos(t, wh, drones, oerders, pw)


if __name__ == "__main__":
    s, f = sys.argv
    print(parse(f))
