def toStr(n, base):
    convertString = "0123456789ABCDEF"
    # if n < base then we will convert it to a string by checking its position at
    # convertString.
    if n< base:
        return convertString[n]
    # else we will use a recursion where we divide n by the base and feed the result back to
    # original function along with the base. This will be done until n < base.
    # meanwhile we will keep note of the remainders and convert them to the string as they come.
    else:
        return toStr(n // base, base) + convertString[n % base]
print toStr(769, 16)