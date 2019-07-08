def findmin_n(l):
    min_n = l[0]
    for i in l:
        if i < min_n:
            min_n = i
    return min_n


def findmin_n2(alist):
    for i in alist:
        i_is_min = True
        for j in alist:
            if j < i:
                i_is_min = False
        if i_is_min:
            return i

    return min


def main():
    my_list = [20, 40, 10, 30, 25, 50, 85, 15]
    print(findmin_n2(my_list))


if __name__ == '__main__':
    main()
