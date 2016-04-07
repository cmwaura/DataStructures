from queueimplementation import Queue
from simulationPrinter import *

import random

def simulation(numSeconds, pagesPerMinute):
    '''
    this will implement the algorithm described with the printer. printQueue is an instance
    of the exisiting queue. A boolean function newprintTask decides whether a new printing task
    needs to be created or not.
    :param numSeconds:
    :param pagePerMinute:
    :return:
    '''

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task) #takes in task

        if not labprinter.busy() and not printQueue.isEmpty():
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)
    print ("Average Wait %6.2f secs %3d tasks remaining." %(averageWait, printQueue.size()))

def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    return False

for i in range(10):
    simulation(3600,5)