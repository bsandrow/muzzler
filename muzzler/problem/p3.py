import math

number = 600851475143

def median(n):
    return ((n-1) // 2) + 1

def get_factors_1(n):
    limit = n
    factors = []
    i = 1
    while i < limit:
        if (n % i) == 0:
            factors += [ i, n / i ]
        limit = (n // i) + 1
        i += 1
    return factors

def is_prime_1(n):
    if (n % 2) == 0:
        return False
    else:
        return n == 1 or len(get_factors_1(n)) == 2

def solution_1():
    """ My initial stab at the problem """
    global answer

    factors = get_factors_1(number)
    factors.sort(reverse=True)

    for factor in factors:
        if is_prime_1(factor):
            answer = factor
            return answer

def get_factors_2(n):
    limit = n
    factors = []
    i = 1
    while i < limit:
        q, r = divmod(n, i)
        if r == 0:
            factors += [ i, q ]
        limit = (n // i) + 1
        i += 1
    return factors

def is_prime_2(n):
    if (n % 2) == 0:
        return False
    else:
        return n == 1 or len(get_factors_1(n)) == 2

def solution_2():
    """ Same as solution_1, but use divmod() in get_factors_2() """
    global answer

    factors = get_factors_2(number)
    factors.sort(reverse=True)

    for factor in factors:
        if is_prime_2(factor):
            answer = factor
            return answer

answer = None
solutions = [ solution_1, solution_2 ]
