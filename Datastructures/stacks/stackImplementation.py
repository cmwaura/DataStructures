'''

we will implement a simple stack using python's list version. In this case we will
assume that the end of the list will be the top of the stack to make it easy. As the
stack grows as push operations occur and new items will be added to the end of the list.
pop operations will manipulate that same end.

'''


class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items ==[]
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        '''
        remember to account for the 0 position
        :return: the last element on top of the stack
        '''
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)