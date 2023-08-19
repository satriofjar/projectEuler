import time


def time_it(f, x):
    start = time.time()
    result = f(x)
    end = time.time()
    return (end - start, result)

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

if __name__ == '__main__':
    print(time_it(sol2, 4000000))