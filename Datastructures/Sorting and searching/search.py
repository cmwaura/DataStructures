def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if item == alist[pos]:
            found = True
        else:
            pos += 1
    return found
print sequentialSearch([1, 2, 3, 4, 5], 5)
print sequentialSearch([1, 2, 3, 4, 5], 15)
