
'''

The main purpose of this module is to create a node that has data and a pointer to
the next node. It wiill also have methods similar to the one implemented in the Deque.
Lets get started.

'''


class Node:

    def __init__(self, initdata):
        '''
        here we will set the node up with the two requirements. It will take in the value of
        the initial data and will set that as data. Then we will ground the next by assigning it
        the value of none. This means that at the node has just been intially created.
        :param initdata: initial data to assign to data.
        :return:
        '''
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    '''
    here we will begin creating the unordered list from a collection of nodes that we set above.
    As long as we know where to find the first node, each item can be found successfully by folliwing
    the links hence the unordered list must contain a rederence to the first node.
    '''

    def __init__(self):
        '''
        here we will use the reference of None as we did in the node. This will represent the head of the list
        and does not refer to anything. The head od the list will refer to the first node which will contain the
        first item of the list.
        :return: nada
        '''
        self.head = None

    def isEmpty(self):
        '''
        checks to see if the header is None. If true it will return True else False
        :return: bool
        '''
        return self.head == None

    def add(self, item):
        '''
        The new item is added at the beginning of the list and becomes the new head. hence when we have
            mylist.add(31)
            mylist.add(77)
            mylist.add(17)
            mylist.add(93)
            mylist.add(26)
            mylist.add(54)
        then 31 becomes the last item as 54 becomes the first.
        :param item:takes in a new item
        :return:
        '''

        temp = Node(item) # assign temp as the node taking in the item
        temp.setNext(self.head) # change the next method to refer to the old first node of the list
        self.head = temp # now we can refer the head of the list to refer to the new node.

    def size(self):

        '''
        things to take note as we look at this particular method:
        1) self.head is the last item that is added in the list. Hence when we start
        at that, we are basically moving backwards to what was originally the start.
        2) initially the header had the value of None.
        :return:  counter
        '''

        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current.getNext()

        return found
