import math

def combination(n:int, k:int):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

def permutation(n:int):
    return math.factorial(n)

def accomadation(n:int, k:int):
    return math.factorial(n)/math.factorial(n-k)
