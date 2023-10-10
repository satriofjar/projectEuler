from math import sqrt
from helper import *


# Solutions problem 1

def sol1(x):
    result = 0
    for i in range(x):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

def sol1a(x):
    return sum([i if i % 3 == 0 or i % 5 == 0 else 0 for i in range(x)])

def sol1b(x):
    return sum(filter(lambda a: a % 3 == 0 or a % 5 == 0, [i for i in range(x)]))

def sol1c(x):
    return sum([i for i in range(3,x,3)]) + sum([i for i in range(5,x,5)]) - sum([i for i in range(15,x,15)])


# Solutions problem 2

def sol2(lim):
    f0 = 0
    fibo = 1
    fhelper = 0
    result = 0
    while True:
        fhelper = fibo
        fibo = f0 + fibo
        f0 = fhelper
        result += fibo if fibo % 2 == 0 else 0
        if fibo >= lim:
            break

    return result

def sol2a(a, b, lim, res):
    if res >= lim :
        return res
    else:
        return sol2a(b, a + b, lim, res + a if is_even(a) else res)


# Solutions problem 3

def sol3(n):
    return max(filter(is_prime, factors(n)))

def sol3a(n):
    akar_n = round(sqrt(n)) + 1
    i = 3
    res = 0

    while i <= akar_n:
        if n % i == 0:
            if is_prime(i):
                res = i
        
        i += 2
    return res


    
def sol3b(n, fak_n, res):
    if len(fak_n) == 1 :
        return fak_n[0]
    if res > fak_n[0] if is_prime(fak_n[0]) else res:
        return res
    else:
        return sol3b(n, fak_n[1:], fak_n[0])


if __name__ == '__main__':
    print(time_it(sol3, 600851475143))
    print(time_it(sol3a, 600851475143))
    print(time_it(sol3b, 600851475143, factors(600851475143), 0))