
def solution_1():
    global answer

    def fib():
        # Modified from version in PEP-0255
        x, y = 1, 2
        # x, y = 0, 1  <-- 'real' fibonacci start
        while y < 4000000:
            if (y % 2) == 0:
                yield y
            x, y = y, x+y

    answer = sum(i for i in fib())

class FibonacciSequence(list):
    def __init__(self, init=None):
        init = init or [0,1]
        list.__init__(self)
        self += init

    def __getitem__(self, index):
        while index >= len(self):
            self.append(self[-1] + self[-2])
        return list.__getitem__(self, index)

def solution_2():
    global answer
    sum = 0
    i   = 1
    seq = FibonacciSequence()
    x   = seq[i]
    while x < 4000000:
        i += 1
        if (x % 2) == 0:
            sum += x
        x = seq[i]
    answer = sum

def solution_3():
    global answer
    sum = 0
    seq = FibonacciSequence()
    for x in seq:
        if x >= 4000000:
            break
        if x % 2:
            continue
        sum += x
    answer = sum

answer = None
solutions = [ solution_1, solution_2, solution_3 ]
