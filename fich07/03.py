import random

def selectionSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def find_kmin(alist, pos):
    selectionSort(alist)
    temp = [alist[i] for i in [pos]]
    return temp


l = random.sample(range(51), 25)
selectionSort(l)
print(l)
print(find_kmin(l, 10))

