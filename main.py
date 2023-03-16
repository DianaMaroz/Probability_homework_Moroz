import math


def combination(n: int, k: int):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


def permutation(n: int):
    return math.factorial(n)


def accomadation(n: int, k: int):
    return math.factorial(n) / math.factorial(n - k)


def bernulli(n: int, k: int, p: float):
    q = 1 - p
    return combination(n, k) * p ** k * q ** (n - k)

def puasson(n, p, m):
    la = p*n
    return (la**m / math.factorial(m)) * math.exp(-la)

