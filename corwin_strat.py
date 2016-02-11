#!/usr/bin/python3

import sys

from writer import *

from parse import parse

from distance import *

def main():
    s, f = sys.argv
    infos = parse(f)
    for drone in infos.drones:
        for order in infos.orders:
            if order.empty():
                pass
            w = next_warehouses(drone, order, infos.warehouses)
            turns = get_distance(drone, w) +get_distance(w, order)
            if drone.check_turns(turns):
                pds = []
                for i in range(len(order.products)):
                    for j in range()


if __name__ == "__main__":
    main()
