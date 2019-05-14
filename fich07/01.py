def min_list_n(l):
    min_n = l[0]
    for i in l:
        if i < min_n:
            min_n = i
    return min_n


def min_list_n2(l):
    i = 0
    found = False
    while i < len(l) and found is False:
        is_min = True
        j = 0
        while j < len(l) and is_min is True:

            if l[j] < l[i]:
                is_min = False
            else:
                j = j + 1

        found = is_min
        i = i + 1

    return l[i]


def main():
    my_list = [20, 40, 10, 30, 25, 50, 85, 15]
    # print(min_list_n(my_list))
    print(min_list_n2(my_list))


if __name__ == '__main__':
    main()
