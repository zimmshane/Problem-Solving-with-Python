import random, math, timeit
from timeit import Timer


def slow_min()->int:
    valuelist = []
    for i in range(1000):
        valuelist.append(random.randint(1,10000))
    currentmin=101
    for value in valuelist:
        for value2 in valuelist:
            if value < ((currentmin) and (value2)):
                currentmin=value
    return currentmin
    

def fast_min()->int:
    valuelist = []
    for i in range(1000):
        valuelist.append(random.randint(1,10000))
    currentmin=101
    for value in valuelist:
        if value<currentmin:
            currentmin=value
    return currentmin



random.seed()

t1=Timer("fast_min()","from __main__ import fast_min")
print("The smallest element is",fast_min()," done in", t1.timeit(number=1000), "milliseconds")
t2=Timer("slow_min()","from __main__ import slow_min")
print("The smallest element (but slower) is",fast_min()," done in", t2.timeit(number=1000), "milliseconds")
    
