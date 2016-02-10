#! /usr/bin/python3
import sys
from parse import parse

def paint_dat_shit_nigga(image):
    lolreturn = ""
    combien_de_lignes = 0
    for r in range(len(image)):
        for c in range(len(image[r])):
            if image[r][c] == "#":
                lolreturn += "PAINT_SQUARE {} {} 0\n".format(r, c)
                combien_de_lignes += 1
    print(combien_de_lignes)
    print(lolreturn)

paint_dat_shit_nigga(parse(sys.argv[1]))

