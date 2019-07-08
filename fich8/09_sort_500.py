import timeit
import random


def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def selectionSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position]=currentvalue


def mergeSort(alist):
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)


def main():
    randoms = random.sample(range(501), 501)

    for j in randoms:
        print(j)

    f = open("tests.txt", "w+")

    t1 = timeit.Timer("bubbleSort(random.sample(range(501), 501))",
                      "from __main__ import bubbleSort;"
                      "import random")
    print("bubbleSort in", t1.timeit(number=1000), "ms")
    f.write("bubbleSort in " + str((t1.timeit(number=1000))) + " ms\n")

    t2 = timeit.Timer("selectionSort(random.sample(range(501), 501))",
                      "from __main__ import selectionSort;"
                      "import random")
    print("selectionSort in", t2.timeit(number=1000), "ms")
    f.write("selectionSort in " + str((t2.timeit(number=1000))) + " ms\n")

    t3 = timeit.Timer("insertionSort(random.sample(range(501), 501))",
                      "from __main__ import insertionSort;"
                      "import random")
    print("insertionSort in", t3.timeit(number=1000), "ms")
    f.write("insertionSort in " + str((t3.timeit(number=1000))) + " ms\n")

    t4 = timeit.Timer("mergeSort(random.sample(range(501), 501))",
                      "from __main__ import mergeSort;"
                      "import random")
    print("mergeSort in", t4.timeit(number=1000), "ms")
    f.write("mergeSort in " + str((t4.timeit(number=1000))) + " ms\n")


if __name__ == '__main__':
    main()