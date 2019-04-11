from fich04.ex01_queue import Queue


def hot_potato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


def main():

        player = input("Insere os nomes de quem joga ")
        players = player.split()

        try:
            num = int(input("Insira o numero de jogadas por turno"))
            if num > 0:
                winner = hot_potato(players, num)
                print("Winner is: ", winner)
        except:
                print("Tem que inserir um numero positivo!")


if __name__ == "__main__":
    main()