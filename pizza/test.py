
def possibleDimensions():
    lst = []
    maxCells = 100
    for i in range(1, maxCells/2+1):
        if maxCells % i == 0:
            lst.append(i)
    lst.append(maxCells)
    #print lst
    counter = 0
    lstDim = []
    i = 0
    for item in lst:
        for k in range(len(lst)):
            if item*lst[k] <= maxCells and k >= i:
                #print item, "*", lst[k], "=", item*lst[k]
                lstDim.append([])
                lstDim[-1].append(item)
                lstDim[-1].append(lst[k])
            counter += 1
        i+=1
    for row in lstDim:
        print row
    
    return lstDim

print possibleDimensions()
