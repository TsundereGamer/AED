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
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1

        alist[position]=currentvalue


def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
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


def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)


def quickSortHelper(alist,first,last):
    if first<last:

        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


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

    t5 = timeit.Timer("quickSort(random.sample(range(501), 501))",
                      "from __main__ import quickSort;"
                      "import random")
    print("quickSort in", t5.timeit(number=1000), "ms")
    f.write("quickSort in " + str((t5.timeit(number=1000))) + " ms\n")
    f.close()


if __name__ == '__main__':
    main()