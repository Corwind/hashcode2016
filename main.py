#!/usr/bin/python3
import writer
import sys
import parse

def main():
  s, f = sys.argv

  #begin solution 1
  infos = parse.parse(f)
  writer.res.append([0, 0, ""])#score, nb_commands, commands
  #test solution here, using writing.py
  writer.load(0, 0, 0, 0)
  writer.deliver(infos, 0, 0, 0, 0)
  #end solution 1

  #begin solution 2
  writer.res.append([0, 0, ""])#score, nb_commands, commands
  #test solution here, using writing.py
  writer.load(0, 0, 0, 0)
  writer.deliver(0, 0, 0, 0)
  writer.load(0, 0, 0, 0)
  writer.deliver(0, 0, 0, 0)
  #end solution 2

  writer.write(sys.argv[1])

if __name__ == "__main__":
  main()
