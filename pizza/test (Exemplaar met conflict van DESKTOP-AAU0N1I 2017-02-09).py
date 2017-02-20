
def possibleDimensions():
    lst = []
    maxCells = 999
    for i in range(1, maxCells/2+1):
        if maxCells % i == 0:
            lst.append(i)
    #print lst


    i = 0
    for item in lst:
        for o in range(len(lst)):
            print lst[o],lst[item]
            if item*lst[o] <= maxCells:
                print item*lst[o]
        #print item, lst[-1-i]
        #i += 1
        print

possibleDimensions()
