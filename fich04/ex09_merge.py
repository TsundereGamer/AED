from fich04.ex01_queue import Queue
import string


def merge(a, b):
    c = Queue()
    c = a.items + b.items
    return c


def main():

    a = Queue()
    b = Queue()

    items1 = input("Elementos da primeira fila (ordenados e separados por espaço) --> ")

    a.enqueue(items1)

    items2 = input("Elementos da segunda fila (ordenados e separados por espaço) --> ")

    b.enqueue(items2)

    print("a: ", a)
    print("b: ", b)
    tmp = merge(a, b)
    print("merge =", " ".join(str(x) for x in tmp))


if __name__ == "__main__":
    main()