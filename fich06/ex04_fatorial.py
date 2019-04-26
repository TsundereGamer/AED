def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)


def main():
    print(fatorial(1))
    print(fatorial(0))
    print(fatorial(4))


if __name__ == '__main__':
    main()