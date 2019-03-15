# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


input_parser = parser()


def get_word():
    global input_parser
    return next(input_parser)


def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

def total_value(items, max_weight):
    return sum([x[2] for x in items]) if sum([x[1] for x in items]) < max_weight else 0


cache = {}


def solve(items, max_weight):
    if not items:
        return ()
    if (items, max_weight) not in cache:
        head = items[0]
        tail = items[1:]
        include = (head,) + solve(tail, max_weight - head[1])
        dont_include = solve(tail, max_weight)
        if total_value(include, max_weight) > total_value(dont_include, max_weight):
            answer = include
        else:
            answer = dont_include
        cache[(items, max_weight)] = answer
    return cache[(items, max_weight)]


# numpy and scipy are available for use
import numpy
import scipy

for t in range(get_number()):
    c, n = get_number(), get_number()
    items = [ (get_number(), get_number()) for _ in range(n)]
    solution = sorted(solve(items, c), key=lambda x: x[1])
