import timeit


def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while swapped is True:

        swapped = False

        for i in range (start, end):
            if a[i] > a[i + 1]:
                a[i], a[i + 1]= a[i + 1], a[i]
                swapped = True

        if swapped is False:
            break

        swapped = False

        end = end-1

        for i in range(end-1, start-1, -1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        start = start + 1


def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum-1


def exchange(alist):
    first = alist[0]
    alist.append(first)
    alist.remove(first)

    return alist


a = list(range(1, 100))
a.append(0)
b = list(range(100, 200))
b.append(0)
c = list(range(200, 300))
c.append(0)
d = list(range(400, 500))
d.append(0)

print("list " + str(a))
string_a = "shortBubbleSort(" + str(a) +")"
string_b = "cocktailSort(" + str(a) +")"
t1 = timeit.Timer(string_a,  "from __main__ import shortBubbleSort")
print("shortBubbleSort in", t1.timeit(number=1000), "ms")

t2 = timeit.Timer(string_b, "from __main__ import cocktailSort")
print("cocktailSort in", t2.timeit(number=1000), "ms\n")


print("list " + str(b))
string_a = "shortBubbleSort(" + str(b) +")"
string_b = "cocktailSort(" + str(b) +")"
t1 = timeit.Timer(string_a,  "from __main__ import shortBubbleSort")
print("shortBubbleSort in", t1.timeit(number=1000), "ms")

t2 = timeit.Timer(string_b, "from __main__ import cocktailSort")
print("cocktailSort in", t2.timeit(number=1000), "ms\n")


print("list " + str(c))
string_a = "shortBubbleSort(" + str(c) +")"
string_b = "cocktailSort(" + str(c) +")"
t1 = timeit.Timer(string_a,  "from __main__ import shortBubbleSort")
print("shortBubbleSort in", t1.timeit(number=1000), "ms")

t2 = timeit.Timer(string_b, "from __main__ import cocktailSort")
print("cocktailSort in", t2.timeit(number=1000), "ms\n")


print("list " + str(d))
string_a = "shortBubbleSort(" + str(d) +")"
string_b = "cocktailSort(" + str(d) +")"
t1 = timeit.Timer(string_a,  "from __main__ import shortBubbleSort")
print("shortBubbleSort in", t1.timeit(number=1000), "ms")

t2 = timeit.Timer(string_b, "from __main__ import cocktailSort")
print("cocktailSort in", t2.timeit(number=1000), "ms\n")
