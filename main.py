#!/usr/bin/python3
import writer
import sys

def main():

  #begin solution 1
  writer.res.append([0, ""])#nb_commands, commands
  #test solution here, using writing.py
  writer.load(0, 0, 0, 0)
  writer.deliver(0, 0, 0, 0)
  #end solution 1

  #begin solution 2
  writer.res.append([0, ""])#nb_commands, commands
  #test solution here, using writing.py
  writer.load(0, 0, 0, 0)
  writer.deliver(0, 0, 0, 0)
  writer.load(0, 0, 0, 0)
  writer.deliver(0, 0, 0, 0)
  #end solution 2

  writer.write(sys.argv[1])

main()
