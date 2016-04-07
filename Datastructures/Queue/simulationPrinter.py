from random import randrange


class Printer(object):
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        '''
        the tick method will decrement the internal timer and set the printer to idle of the
        task is completed.

        '''
        # if there is a current task going on then we will decrement the internal timer
        # by one.
        if self.currentTask != None:
            self.timeRemaining -= 1
            # if the time remaining gets to 0 the we have that the current task of that printer
            # will be set to None.
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        '''
        checks to see whether the printer is busy. If it is then it will return a boolean
        of true. Else it will return False
        '''

        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        '''

        :param newtask: this is the next task that the printer will begin,

        '''

        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate

class Task(object):
    '''
    The taks class will represent a single printing task. When a task is created, a
    random number generator will provide a length from 1-20 pages with the randrange
    function from random
    '''

    def __init__(self, time):
        self.timestamp = time
        self.pages = randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp
