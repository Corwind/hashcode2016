#!/usr/bin/python3

"""
Written by dore_g
"""

import sys
from pprint import pprint as print

from distance import get_distance

class Infos:
    def __init__(self, turns, warehouses, drones, orders, wgs):
        self.warehouses = warehouses
        self.turns = turns
        self.weights = wgs
        self.drones = drones
        self.orders = orders

    def __repr__(self):
        return "warehouses: {}\nturns: {}\nweights: {}\ndrones: {}\norders:\
            {}".format(self.warehouses, self.turns, self.weights, self.drones,
                    self.orders)

class Warehouse:
    def __init__(self, stock, line, col):
        self.stock = stock
        self.line = line
        self.col = col

    def update_stock(obj, quantity):
        self.stock[obj] -= quantity

    def check_obj(obj, quantity):
        return self.stock[obj] >= quantity

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
        self.turns = 0
        self.weight = weight
        self.line = line
        self.col = col

    def use_turns(n):
        self.turns -= n

    def check_turns(n):
        return self.turns >= n

    def go_to_warehouse(w):
        self.turns -= get_distance(self, w)

def parse(f):
    orders = []
    wh = []
    drones = []
    with open(f, 'r') as fi:
        lines, cols, t, dr, p = map(int, fi.readline().split())
        pt = int(fi.readline())
        pw = map(int, fi.readline().split())
        nw = int(fi.readline())
        for i in range(nw):
            line, col = map(int, fi.readline().split())
            stock = map(int, fi.readline().split())
            wh.append(Warehouse(stock, line, col))
        o = int(fi.readline())
        for i in range(o):
            line, col = map(int, fi.readline().split())
            nb = int(fi.readline())
            prods = map(int, fi.readline().split())
            orders.append(Order(prods, line, col))
        for i in range(dr):
            drones.append(Drone(p, wh[0].line, wh[0].col))
    return Infos(t, wh, drones, orders, pw)


if __name__ == "__main__":
    s, f = sys.argv
    print(parse(f))
