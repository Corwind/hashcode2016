#! /usr/bin/python3

"""
  Written by adjou_k
"""

from parse import *
import sys
from distance import *

def next_warehouses(drone, order, warehouses, origin_warehouse):
  useful_warehouses = []
  distances = []
  for w in warehouses:
    for i, j in zip(order.products, w.stock):
      if (i > j):
        useful_warehouses.append(w)
  for ware in useful_warehouses:
    distances.append(get_distance(ware, origin_warehouse))
  return useful_warehouses[distances.index(min(distances))]

if __name__ == '__main__':
  infos = parse(sys.argv[1])
  a = next_warehouses(infos.drones[0], infos.orders[0], infos.warehouses, info.warehouses[0])
  print("line: {}, col: {}".format(a.line, a.col))
