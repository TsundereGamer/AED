import timeit


def sequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos+1

    return found


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


def main():
    t1 = timeit.Timer("sequentialSearch([0, 1, 2, 8, 13, 17, 19, 32, 42], 17)", "from __main__ import sequentialSearch")
    print("sequentialSearch de 17 =", sequentialSearch([0, 1, 2, 8, 13, 17, 19, 32, 42], 17), "in", t1.timeit(number=1000), "ms")

    t2 = timeit.Timer("binarySearch([0, 1, 2, 8, 13, 17, 19, 32, 42], 17)", "from __main__ import binarySearch")
    print("binarySearch de 17 =", binarySearch([0, 1, 2, 8, 13, 17, 19, 32, 42], 17), "in", t2.timeit(number=1000), "ms")


if __name__ == '__main__':
    main()
