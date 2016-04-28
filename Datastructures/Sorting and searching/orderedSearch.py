def orderedSequentialSearch(alist, item):
    found = False
    stop = False
    pos = 0
    while item < len(alist) and not found and not stop:
        if item == alist[pos]:
            found = True
        else:
            if item < alist[pos]:
                stop = True
            else:
                pos += 1
    return found
alist = [0, 1, 2, 8, 13, 17, 19, 32, 42,57]
print(orderedSequentialSearch(alist, 15))
print(orderedSequentialSearch(alist, 8))
print(orderedSequentialSearch(alist, 32))