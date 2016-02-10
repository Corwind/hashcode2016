#! /usr/bin/python3
import sys
from parse import parse

def paint_dat_shit_nigga(image):
    lolreturn = ""
    combien_de_lignes = 0
    boule = False
    start_r = False
    start_c = False
    for r in range(len(image)):
        for c in range(len(image[r])):
            if boule:
                if image[r][c] == "#":
                    boule = True
                    start_r = r
                    start_c = c
            else:
                if image[r][c] == ".":
                    boule = False
                    combien_de_lignes += 1
                    lolreturn += "PAINT_LINE {start_r} {start_c} {end_r} {end_c}\n".format(start_r=start_r, start_c=start_c, end_r=r-1, end_c=c-1)
    print(combien_de_lignes)
    print(lolreturn)

paint_dat_shit_nigga(parse(sys.argv[1]))

