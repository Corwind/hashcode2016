#!/usr/bin/python
import sys
import re

# parser

lines = []
dims = []
with open(sys.argv[1]) as fp:
  for line in fp:
    if dims == []:
      dims = line.split()
    else:
      lines.append(line)

# paint!

text_to_write = ""
nb_lines = 0
for r in range(int(dims[0])):
  for c in range(int(dims[1])):
    if lines[r][c] == '#':
      text_to_write += "PAINT_SQUARE {} {} 0\n".format(r, c)
      nb_lines += 1
with open(sys.argv[1].split('.')[0] + "_output.txt", 'w') as f_out:
  f_out.write(str(nb_lines) + "\n" + text_to_write)

