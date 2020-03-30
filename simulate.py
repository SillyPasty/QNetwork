import random

def simulate(times, size):
    for i in range(0, times):
        start = random.randint(0, size)
        end = start
        while end == start:
            end = random.randint(0, size)
        # do algorithm
        