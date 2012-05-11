import math

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
    global answer

    number = 600851475143
    factors = get_factors_1(number)
    factors.sort(reverse=True)

    for factor in factors:
        if is_prime_1(factor):
            answer = factor
            return answer

answer = None
solutions = [ solution_1 ]
