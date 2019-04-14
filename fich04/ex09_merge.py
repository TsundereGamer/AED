from fich04.ex01_queue import Queue
from fich03_group_I.stack import Stack


def merge(a, b):
    sa = Stack()
    sb = Stack()

    #   Inserir os items de cada queue em stacks independentes
    for i in a.items:
        sa.push(i)

    for j in b.items:
        sb.push(j)

    #   Comparar os 2 stacks
    sc = Stack()
    while not sa.isEmpty() and not sb.isEmpty():
        if sa.peek() < sb.peek():
            tmp = sa.pop()
            sc.push(tmp)
            tmp = sb.pop()
            sc.push(tmp)
        elif sb.peek() < sa.peek():
            tmp = sb.pop()
            sc.push(tmp)
            tmp = sa.pop()
            sc.push(tmp)

    #   Virar o stack ao contrario
    sd = Stack()
    while not sc.isEmpty():
        tmp = sc.pop()
        sd.push(tmp)

    #   Inserir o stack temporario na queue final
    c = Queue()
    for y in sd.items:
        c.enqueue(y)

    return c


def main():

    a = Queue()
    b = Queue()

    # items1 = input("Elementos da primeira fila (ordenados e separados por espaço) --> ")

    items1 = [5, 10, 30]
    for itema in items1:
        a.enqueue(itema)

    # items2 = input("Elementos da segunda fila (ordenados e separados por espaço) --> ")

    items2 = [6, 11, 31]
    for itemb in items2:
        b.enqueue(itemb)

    print("a: ", a.items)
    print("b: ", b.items)
    print("c:", merge(a, b))


if __name__ == "__main__":
    main()
