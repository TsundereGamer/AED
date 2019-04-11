from fich04.ex01_queue import Queue


def process(q, a, b):
    while q is not q.isEmpty():
        for item in q.items:
            if a.size() < b.size() or q.items :
                a.enqueue(q.items)
            elif b.size() < a.size():
                b.enqueue(q.items)
            else:
                q.dequeue()


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
    print("q: ", q)
    print("a: ", a)
    print("b: ", b)


if __name__ == "__main__":
    main()
