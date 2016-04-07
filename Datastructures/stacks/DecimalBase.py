from stackImplementation import Stack

def baseConverter(decNumber, base):
    '''
    this is the base implementation of converting a number from decimal to
    binary, Hex and Octal. It uses the class of stack and will return the
    coverted number as a string.
    :param decNumber: the actual decimal number
    :param base: the base you want to convert the number to
    :return: the resulting solution based on the base insisted
    '''
    digits = "0123456789ABCDEF"

    remstack = Stack()
    while decNumber > 0:
        # Similar to the binary execution, here we use the base that the user
        # specifies.

        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""

    while not remstack.isEmpty():
        newString = newString + str(remstack.pop())
    return newString

print baseConverter(25, 2)
print baseConverter(256, 16)
print baseConverter(26, 26)
