def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def shortBubbleSort(alist): #bubblesort otimizado
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


alist = [54,26,93,17,77,31,44,55,20]
blist = [20,30,40,90,50,60,70,80,100,110]
bubbleSort(alist)
shortBubbleSort(blist)
print(alist)
print(blist)