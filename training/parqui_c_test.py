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
      print(len(lines))
    print(line)
  fp.close()

print("THE BEGINNING")
for i in dims:
  print(i)
print("THE END")

# paint!

for l in range(int(dims[0])):
  sys.stdout.write(str(l))
