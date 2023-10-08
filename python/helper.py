from math import sqrt
import time


def time_it(f, x):
    start = time.time()
    result = f(x)
    end = time.time()
    return (end - start, result)

def is_even(n):
    return True if n % 2 == 0 else False

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