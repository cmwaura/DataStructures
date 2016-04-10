from DequeImplementation import Deque

def palchecker(words):
    '''
    The purpose of this exercise is to see a deque implementation at work. Here
    we are going to create a checker that tries to see whether a word is the same
    implemented forwards or backwards. The word "radar" for instance is a palindrome
    that is still radar forwards or backwards.

    Here is the implementation. We will feed the word into a deque through the rear lol.
    Then we will remove a character at a time from the front and the rear as we check for
    whether these words are equal. If they are not equal we will return False. If Equal we
    will return true and thus a Palindrome.
    :param words: a string to be tested to see whether it is a palindrome
    :return: boolean value.
    '''

    charDeque = Deque()
    for char in words:
        charDeque.addRear(char)

    isStillEqual = True

    while charDeque.size() > 1 and isStillEqual:
        first = charDeque.removeFront()
        last = charDeque.removeRear()
        if first !=last:
            isStillEqual = False

    return isStillEqual
print palchecker("hello")
print palchecker("radar")


