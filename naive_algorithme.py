# Algo naïf pour résoudre le pb

import numpy
from copy import deepcopy


def binary(n, length):
    res = []
    while n != 0:
        a = n%2
        if a == 1:
           res = [1] + res
        elif a == 0:
            res = [0] + res
        n = n//2
    while len(res) < length:
        res = [0] + res
    return res


def is_correct(Map):
    return not 1 in Map


def cover(Map, Centers):
    mod = []
    for center in Centers:
        for i in range(15):
            for j in range(15):
                mod += [center + (i,j), center + (-i,j), center + (i, -j), center + (-i, -j)]
    for coord in mod:
        Map[coord] = 0
    return Map

