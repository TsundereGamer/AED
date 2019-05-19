def merge(alist, lefthalf, righthalf):

    # the merge operation places the items back into
    # the alist one at a time by repeatedly
    # taking the smallest item from the sorted lists
    print("Merging ", alist)
    i = 0
    j = 0
    k = 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] <= righthalf[j]:
            alist[k] = lefthalf[i]
            i = i + 1
        else:
            alist[k] = righthalf[j]
            j = j + 1
        k = k + 1

    # Insert all the remaining values of
    # the left half into the new sorted list
    while i < len(lefthalf):
        alist[k] = lefthalf[i]
        i = i + 1
        k = k + 1

    # Insert all the remaining values of
    # the left half into the new sorted list
    while j < len(righthalf):
        alist[k] = righthalf[j]
        j = j + 1
        k = k + 1

def mergeSort(alist):

    print("Splitting ", alist)

    # Ask the base case question. If the length of the list
    # is 1, then the list is sorted and we are finished
    if len(alist) > 1:

        # divide the list into two halves
        # using the slice operation to extract them
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        # SORT the left half
        mergeSort(lefthalf)
        # SORT the right half
        mergeSort(righthalf)

        # MERGE the two sorted halves into a larger sorted list
        # in this case into the original list alist
        merge(alist, lefthalf, righthalf)


#alist = [93, 54, 26, 77, 31]
alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)