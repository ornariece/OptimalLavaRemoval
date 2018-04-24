# Algo naïf pour résoudre le pb

import numpy as np


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


def ind2lc(ind, nbl, nbc):
    return (ind//nbc, ind%nbc)

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


def good_cover(Map):
    """
    :type Map: np.ndarray
    :param Map:
    :return:
    """
    Res = []
    (nbl, nbc) = Map.shape
    for i in range(2**(nbl*nbc)):
        Centers = []
        M = Map.__deepcopy__()
        D = binary(i, nbl*nbc)
        for j in range(len(D)):
            if D[j] == 1:
                Centers += [ind2lc(j, nbl, nbc)]
        M = cover(M, Centers)
        if is_correct(M):
            Res += [(i, Centers)]
    return Res


def best_cover(Map):
    Covers = good_cover(Map)
    return max(Covers, key= lambda x: len(x[1]))
