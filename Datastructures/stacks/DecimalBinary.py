from stackImplementation import Stack

def dividebytwo(decNumber):
    '''
    this function takes in the decNumber and divides it by two saving the result
    as a remainder rem. We will then use Stack.Push to append the result unto the
    list since the stack was implemented as a list. Then we will divide the number
    two until decNumber ==0
    :param decNumber:
    :return:
    '''
    remstack = Stack()

    while decNumber > 0:
        # take the mod of the number given then divide that number by two
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ''
    while not remstack.isEmpty():
        #concatenate the remainder to the variable binString
        binString = binString + str(remstack.pop())
    return binString
print dividebytwo(233)


