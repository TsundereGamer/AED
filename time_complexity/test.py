import random
import timeit


def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found


randoms = random.sample(range(1000), 500)
print(randoms)

timeit.Timer("sorted(r)", setup = "import random; r = random.sample(range(1000), 500)")
timeit.Timer("sorted(r)", "from __main__ import sorted")
print("binarySearch de 17 =", binarySearch(random.sample(range(1000), 500), 17), "in", timeit.timeit(number=1000), "ms")