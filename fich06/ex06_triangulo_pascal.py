def triangle(n):
    # Caso base
    if n == 0:
        return []
    # Caso base
    elif n == 1:
        return [[1]]
    # Passo recursivo
    else:
        new_row = [1]
        result = triangle(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result.append(new_row)
    return result


def main():
    h = 5

    for i in triangle(h):
        print(*i)


if __name__ == '__main__':
    main()
