#!/usr/bin/python3
import sys
import re
import parse

res = []

def load(drone_number, nb_products, type_product, warehouse_number):
  res[len(res) - 1][2] += "{} L {} {} {}\n".format(drone_number, warehouse_number, type_product, nb_products)
  res[len(res) - 1][1] += 1

def unload(drone_number, nb_products, type_product, warehouse_number):
  res[len(res) - 1][2] += "{} U {} {} {}\n".format(drone_number, warehouse_number, type_product, nb_products)
  res[len(res) - 1][1] += 1

def deliver(infos, drone_number, nb_products, type_product, order_number):
  res[len(res) - 1][2] += "{} D {} {} {}\n".format(drone_number, order_number, type_product, nb_products)
  res[len(res) - 1][1] += 1
  if (infos.orders[order_number] == []):
    res[len(res) - 1][0] += ((infos.turns - infos.drones[drone_number].turns) / infos.turns)

def wait(drone_number, nb_turns_to_wait):
  res[len(res) - 1][2] += "{} W {}\n".format(drone_number, nb_turns_to_wait)
  res[len(res) - 1][1] += 1

def write(name_input):
  with open(name_input.split('.')[0] + "_output.txt", 'w') as f_out:
    for score, nb, s in res:
      print("score: {}, nb commands: {}".format(score, nb))
    best = min(res, key=lambda r: r[0])
    f_out.write(str(best[1]) + "\n" + best[2])
