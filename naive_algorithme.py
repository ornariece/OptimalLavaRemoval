# Algo naïf pour résoudre le pb

import numpy as np
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


def ind2lc(ind, nbl, nbc):
    return (ind//nbc, ind%nbc)

def is_correct(Map):
    return not 1 in Map


def cover(M, Centers):
    mod = []
    nbl, nbc = M.shape
    for center in Centers:
        x = center[0]
        y = center[1]
        for i in range(15):
            for j in range(15):
                mod += [(x+i, y+j), (x-i, y+j), (x+i, y-j), (x-i, y-i)]
    for coord in mod:
        if coord[0] < nbl and coord[1] < nbc and coord[0] >= 0 and coord[1] >= 0:
            M[coord] = 0
    return M


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
        M = deepcopy(Map)
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
    return min(Covers, key= lambda x: len(x[1]))


print(best_cover(np.array([[0, 1], [0, 1]])))
print(cover(np.array([[0, 1], [0, 1]]), [(0, 0)]))
