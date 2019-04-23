def fibonacci_rec(n):
    if n < 0:
        print("Input Incorreto")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)


def fibonacci_ite(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b


def main():
    print("fibonacci recursivo: ", fibonacci_rec(9))
    print("fibonacci iterativo: ", fibonacci_ite(9))


if __name__ == '__main__':
    main()
