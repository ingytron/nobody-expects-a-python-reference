def lessThan4(aList):
    result = []
    for s in aList:
        if len(s) < 4:
            result += s
    return result
