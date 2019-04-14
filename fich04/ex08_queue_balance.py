from fich04.ex01_queue import Queue
from fich03_group_I.stack import Stack


def process(q, a, b):
    q_s = Stack()
    for i in q.items:
        q_s.push(i)

    a_s = Stack()
    b_s = Stack()

    while not q_s.isEmpty():
        tmp_op = q_s.pop()
        tmp_name = q_s.pop()
        if tmp_op == "A":
            a_s.push(tmp_name)
        elif tmp_op == "B":
            b_s.push(tmp_name)
        elif tmp_op == "X":
            if a_s.size() < b_s.size():
                a_s.push(tmp_name)
            elif a_s.size() > b_s.size():
                b_s.push(tmp_name)
            elif a_s.size() == b_s.size():
                tmp_name = None
                tmp_op = None

    for x in a_s.items:
        a.enqueue(x)

    for y in b_s.items:
        b.enqueue(y)

    for j in q_s.items:
        q.enqueue(j)

    return q.items, a.items, b.items


def __str__(self):
    string = ""
    for item in self.items:
        string = string + " " + str(item)

    return string


def read_int():
    while True:
        try:
            n = int(input("Número de nomes --> "))
            if n >= 1:
                return n
            else:
                print("Ops! O número tem de ser um inteiro positivo")
        except ValueError:
            print("Ops! O número tem de ser um inteiro positivo")


def main():

    q = Queue()
    a = Queue()
    b = Queue()

    n = read_int()

    for i in range(0, n):

        nome_operacao = input("Nome e Operação (separados por espaço) --> ")
        nome_operacao = nome_operacao.split()

        q.enqueue(nome_operacao[1])
        q.enqueue(nome_operacao[0])

    print("Início:")
    print("q: ", q)
    print("a: ", a)
    print("b: ", b)

    process(q, a, b)

    print("-------------------------------")
    print("Final:")
    print("q: ")
    print("a: ", a)
    print("b: ", b)


if __name__ == "__main__":
    main()

