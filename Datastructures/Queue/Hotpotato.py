from queueimplementation import Queue
'''
here we will implement a hot potato game. The main aim of this game is to have
a potato passed around from one person t another then at a particular point the
potato will be stopped. The person holding the potato at that particular time will
be eliminated. This will ben implemented via the queue class.
'''

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()

    return simqueue.dequeue()
print hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"],7)
