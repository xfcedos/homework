import random
import copy

def stopwatch(f):
    import time

    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        result = f(*args, **kwargs)
        end = time.perf_counter_ns()
        print(f"Func: {f.__name__}; Time: {end - start} ns.")
        return result

    return wrapper


count = 100
rnd_nums = random.sample(range(1000), count)


@stopwatch
def summing_with_for(l):
    res = 0
    for el in l:
        res += el
    return res


@stopwatch
def summing_with_while(l):
    l = copy.copy(l)
    res = 0
    while len(l) > 0:
        res += l.pop()
    return res


@stopwatch
def summing_recursive(l):
    l = copy.copy(l)

    def f_rec_sum(*args):
        if len(l) == 0:
            return 0
        return l.pop() + f_rec_sum(l)

    return f_rec_sum(l)


@stopwatch
def summing_with_sum(l):
    return sum(l)


for f in [summing_with_for, summing_with_while, summing_recursive, summing_with_sum]:
    print(f(rnd_nums))
