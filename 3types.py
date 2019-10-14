import random


def f_rec_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + f_rec_sum(num_list[1:])


def stopwatch(f):
    import time

    def wrapper():
        start = time.time()
        f()
        end = time.time()
        print(end - start)
    return wrapper


count = 100
rnd_nums = random.sample(range(1000), count)


@stopwatch
def summing_with_for():
    for_sum = 0
    for i in range(count):
        for_sum += rnd_nums[i]
    print(for_sum)

@stopwatch
def summing_with_while():
    while_sum = 0
    i = 0
    while i < count:
        while_sum += rnd_nums[i]
        i += 1
    print(while_sum)

@stopwatch
def summing_recursive():
    recursive_sum = f_rec_sum(rnd_nums)
    print(recursive_sum)


summing_with_for()
summing_with_while()
summing_recursive()
