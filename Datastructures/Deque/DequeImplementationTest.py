from DequeImplementation import Deque

d = Deque()
print d.isEmpty()
d.addRear(4)
d.addFront('cat')
d.addFront(True)
print d.size()
print d.isEmpty()
d.addRear(8.4)
d.removeRear()
d.removeFront()