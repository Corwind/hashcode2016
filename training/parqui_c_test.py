#!/usr/bin/python3
import sys
import re
from copy import deepcopy

# parser

lines = []
dims = []
with open(sys.argv[1]) as fp:
  for line in fp:
    if dims == []:
      dims = line.split()
    else:
      lines.append(list(line))

# paint!

res = []

res.append([0, ""])
for r in range(int(dims[0])):
  for c in range(int(dims[1])):
    if lines[r][c] == '#':
      res[len(res)-1][1] += "PAINT_SQUARE {} {} 0\n".format(r, c)
      res[len(res)-1][0] += 1

def check_square(liness, r_center, c_center, size):
  for r in range(r_center - size, r_center + size + 1):
    for c in range(c_center - size, c_center + size + 1):
      if r < 0 or c < 0 or r > int(dims[0]) - 1 or c > int(dims[1]) - 1:
        return False
      if liness[r][c] == ".":
        return False
  return True

def paint_square(liness, r_center, c_center, size):
  for r in range(r_center - size, r_center + size + 1):
    for c in range(c_center - size, c_center + size + 1):
      liness[r][c] = '.'

res.append([0, ""])
liness = deepcopy(lines)
for r in range(int(dims[0])):
  for c in range(int(dims[1])):
    if liness[r][c] == '#':
      square_size = 0
      while check_square(liness, r + square_size + 1, c + square_size + 1, square_size + 1):
        square_size += 1

      res[len(res)-1][1] += "PAINT_SQUARE {} {} {}\n".format(r + square_size, c + square_size, square_size)
      paint_square(liness, r + square_size, c + square_size, square_size)
      res[len(res)-1][0] += 1



with open(sys.argv[1].split('.')[0] + "_output.txt", 'w') as f_out:
  for n, s in res:
    print(n)
  best = min(res, key=lambda r: r[0])
  f_out.write(str(best[0]) + "\n" + best[1])
