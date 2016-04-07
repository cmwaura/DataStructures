
'''
lets begin by creating an abstract queue that we can then use for other
smaller more specialized classes.
'''

class Queue:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def enqueue(self,  item):
        self.item.insert(0, item)

    def dequeue(self):
        return self.item.pop()

    def size(self):
        return len(self.item)
