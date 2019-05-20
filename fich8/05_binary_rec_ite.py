import timeit
import random


def binarySearch_ite(alist, item):
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


def binarySearch_rec(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearch_rec(alist[:midpoint], item)
            else:
                return binarySearch_rec(alist[midpoint+1:], item)


def main():
    randoms = random.sample(range(101), 101)
    print("Lista com 100 items")
    print(randoms, "\n")

    t1 = timeit.Timer("binarySearch_ite(random.sample(range(101), 101), 17)",
                      "from __main__ import binarySearch_ite;"
                      "import random")
    print("binarySearch_ite of 17 in", t1.timeit(number=1000), "ms")

    t2 = timeit.Timer("binarySearch_rec(random.sample(range(101), 101), 17)",
                      "from __main__ import binarySearch_rec;"
                      "import random")
    print("binarySearch_rec of 17 in", t2.timeit(number=1000), "ms\n")

    randoms = random.sample(range(201), 201)
    print("Lista com 200 items")
    print(randoms, "\n")

    t1 = timeit.Timer("binarySearch_ite(random.sample(range(201), 201), 17)",
                      "from __main__ import binarySearch_ite;"
                      "import random")
    print("binarySearch_ite of 17 in", t1.timeit(number=1000), "ms")

    t2 = timeit.Timer("binarySearch_rec(random.sample(range(201), 201), 17)",
                      "from __main__ import binarySearch_rec;"
                      "import random")
    print("binarySearch_rec of 17 in", t2.timeit(number=1000), "ms\n")

    randoms = random.sample(range(401), 401)
    print("Lista com 400 items")
    print(randoms, "\n")

    t1 = timeit.Timer("binarySearch_ite(random.sample(range(401), 401), 17)",
                      "from __main__ import binarySearch_ite;"
                      "import random")
    print("binarySearch_ite of 17 in", t1.timeit(number=1000), "ms")

    t2 = timeit.Timer("binarySearch_rec(random.sample(range(401), 401), 17)",
                      "from __main__ import binarySearch_rec;"
                      "import random")
    print("binarySearch_rec of 17 in", t2.timeit(number=1000), "ms\n")


if __name__ == '__main__':
    main()