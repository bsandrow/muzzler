
__all__ = [ 'solutions', 'answer' ]

def solution_1():
    global answer
    multiples = {}

    i = 0
    while True:
        m3 = 3 * i
        if m3 < 1000:
            multiples[m3] = 1

        m5 = 5 * i
        if m5 < 1000:
            multiples[m5] = 1

        if m5 >= 1000 and m3 >= 1000:
            break

        i += 1

    answer = sum(multiples.keys())

def solution_2():
    global answer
    multiples = []

    for i in xrange(1,1000):
        if i == 1000:
            print 'BAD'

        if (i % 3) == 0 or (i % 5) == 0:
            multiples.append(i)

    answer = sum(multiples)

def solution_3():
    global answer
    multiples = {}

    for i in xrange(1,1000):
        if i == 1000:
            print 'BAD'

        if (i % 3) == 0 or (i % 5) == 0:
            multiples[i] = 1

    answer = sum(multiples.keys())

def solution_4():
    global answer
    multiples = {}

    i = 0
    while True:
        m = 3 * i
        if m >= 1000:
            break
        multiples[m] = 1
        i += 1

    i = 0
    while True:
        m = 5 * i
        if m >= 1000:
            break
        multiples[m] = 1
        i += 1

    answer = sum(multiples.keys())

def solution_5():
    global answer
    multiples = set()

    i = 0
    while True:
        m = 3 * i
        if m >= 1000:
            break
        multiples.add(m)
        i += 1

    i = 0
    while True:
        m = 5 * i
        if m >= 1000:
            break
        multiples.add(m)
        i += 1

    answer = sum(multiples)

answer = None
solutions = [
    solution_1,
    solution_2,
    solution_3,
    solution_4,
    solution_5,
]
