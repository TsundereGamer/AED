import timeit


def fibonacci_rec(n):
    if n == 0: #caso base
        return 0
    if n == 1: #caso base
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2) #passo recursivo


def fibonacci_ite(n):
    a = 0
    b = 1

    if n == 0:
        return a
    if n == 1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b


def main():
    t1 = timeit.Timer("fibonacci_ite(9)", "from __main__ import fibonacci_ite")
    print("fibonacci ite de 9 =", fibonacci_ite(9), "in", t1.timeit(number=1000), "ms")

    t2 = timeit.Timer("fibonacci_rec(9)", "from __main__ import fibonacci_rec")
    print("fibonacci rec de 9 =", fibonacci_rec(9), "in", t2.timeit(number=1000), "ms")


if __name__ == '__main__':
    main()
