# Algo naïf pour résoudre le pb


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


