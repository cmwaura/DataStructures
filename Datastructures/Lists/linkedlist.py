
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

    def remove(self, item):
        current = self.head
        # remember that previous is one step behind so when current is assigned the header,
        # prev will be assigned none.
        previous = None
        found = False

        while not found:
            # at this point we will iterate through the nodes and when we find the node
            # that we are looking for we will return a value of true. Else, we will move previous
            # to the current step then move current to the next step.

            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        # once we have found the item we are looking for, then we have to check for the case where the
        # item was actually the header. In that case then the header becomes the next element
        # else if that wasnt the case then we will shift the link and set the next item of previous as the
        # next item of current.

        if previous == None:

            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

class OrderedList:
    '''
    before we move ahead it is worth noting that the methods size(), isEmpty() and remove()
    will be the same as the unordered list. What changes is the adding method and search method
    '''

    def __init__(self):
        self.head = None

    def isEmpty(self):
        '''
        checks to see if the header is None. If true it will return True else False
        :return: bool
        '''
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count



    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:

                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def add(self, item):
        current = self.head
        stop = False
        found = False
        previous = None

        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            # if previous is the none value but the header value is greater than the
            # item we are looking for. We will set the item at the header
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.getNext(current)
            previous.setNext(temp)


    def search(self, item):
        '''
        we will search for the item in an ordered linked list. When stop is true the search will stop
        and while false it will keep on going until it finds the item or stop is set to be true.
        :param item: item to be searched for
        :return: found to be true or false.
        '''

        current = self.head
        stop = False
        found = False

        while current != None and not stop and not found:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current.getNext()
        return found






