#!/usr/bin/python3
import sys
import re

res = []

def load(drone_number, nb_products, type_product, warehouse_number):
  res[len(res) - 1][1] += "{} L {} {} {}\n".format(drone_number, warehouse_number, type_product, nb_products)
  res[len(res) - 1][0] += 1

def unload(drone_number, nb_products, type_product, warehouse_number):
  res[len(res) - 1][1] += "{} U {} {} {}\n".format(drone_number, warehouse_number, type_product, nb_products)
  res[len(res) - 1][0] += 1

def deliver(drone_number, nb_products, type_product, customer_number):
  res[len(res) - 1][1] += "{} D {} {} {}\n".format(drone_number, customer_number, type_product, nb_products)
  res[len(res) - 1][0] += 1

def wait(drone_number, nb_turns_to_wait):
  res[len(res) - 1][1] += "{} W {}\n".format(drone_number, nb_turns_to_wait)
  res[len(res) - 1][0] += 1

def write(name_input):
  with open(name_input.split('.')[0] + "_output.txt", 'w') as f_out:
    for n, s in res:
      print(n)
    best = min(res, key=lambda r: r[0])
    f_out.write(str(best[0]) + "\n" + best[1])
