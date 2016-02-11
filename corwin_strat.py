#!/usr/bin/python3

import sys

from parse import parse

def main():
    s, f = sys.argv
    infos = parse(f)

if __name__ == "__main__":
    main()
