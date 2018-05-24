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
    return 1 not in Map


def cover(M, Centers):
    nbl, nbc = M.shape
    for center in Centers:
        x = center[0]
        y = center[1]
        l_min = max(0, x - 14)
        l_max = min(nbl, x + 14)
        c_min = max(0, y - 14)
        c_max = min(nbc, y + 14)
        l = l_max - l_min
        c = c_max - c_min
        rng = np.zeros((l, c))
        M[l_min:l_max, c_min:c_max] = rng
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
print(cover(np.array([[0, 1], [0, 1]]), [(1, 1)]))
