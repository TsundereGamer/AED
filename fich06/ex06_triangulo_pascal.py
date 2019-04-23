def pascal_triangle(n):
    # Caso base
    if n == 0:
        return []

    if n == 1:
        return [[1]]

    # Caso recursivo
    last_list = pascal_triangle(n - 1)
    this_list = [1]

    for i in range(1, n-1):
        this_list.append(last_list[n-2][i-1] + last_list[n-2][i])
    this_list.append(1)

    last_list.append(this_list)

    return last_list


def ultima_linha(n):
    triangle = pascal_triangle(n)
    return triangle[n-1]


def main():
    for x in pascal_triangle(5):
        print(x)


if __name__ == '__main__':
    main()
