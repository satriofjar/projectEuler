from math import sqrt
from functools import reduce
import time


def time_it(f, *args):
    start = time.time()
    result = f(*args)
    end = time.time()
    return (end - start, result)

def is_even(n):
    return True if n % 2 == 0 else False

def is_zero(a, b):
    return True if a % b == 0 else False

def is_prime(n):
    akar_n = round(sqrt(n)) + 1

    if n < 2:
        return False
    elif n == 2:
        return True
    elif is_even(n):
        return False
    else:
        for i in range(3, akar_n, 2):
            if n % i == 0:
                return False
        
        return True
    
def factors(n):
    akar_n = round(sqrt(n)) + 1
    
    res = []

    for i in range(3, akar_n, 2):
        if n % i == 0:
            res.append(i)

    return res



def fak_prime(n):

    if is_prime(n):
        return [n]
    
    akar_n = round(sqrt(n)) + 1

    ls = list(filter(is_prime, range(1, akar_n + 1)))
    res = []

    for i in ls:
        if is_zero(n, i):
            temp = divmod(n, i)
            while temp[1] == 0:
                res.append(i)
                
                temp = divmod(temp[0], i)
    
    return res


def kpk(a, b):
    res = 1
    gabung = set(a).union(set(b))
    for i in gabung:
        if (i in a) and (i in b):
            res *= (i ** a.count(i)) if a.count(i) >= b.count(i) else (i ** b.count(i))

        elif i in a:
            res *= (i ** a.count(i))
        elif i in b:
            res *= (i ** b.count(i))

    return res



def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
