import random
from fich04.printer import Printer
from fich04.task import Task
from fich04.ex01_queue import Queue


def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))


def newPrintTask():
    # num_alunos = 10
    # num_tarefas = 2*num_alunos
    # tempo = 1 h
    # calculo - 20/1 h * 1/60 min * 1/60 s
    # calculo = 20 tarefas/3600 seg
    # calculo = 1 tarefa/ x seg = 180 seg

    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False


for i in range(10):
    simulation(3600, 10)