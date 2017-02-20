import os

def clear():
    os.system('clear')
clear()

def newline():
	print("")


filename = "big.in"

f = open(filename, 'r')

#print(f.readline())

#for char in f.readline():
#	print char

first_line = f.readline().split()
#print first_line

rows = int(first_line[0])
columns = int(first_line[1])
minIngred = int(first_line[2])
maxCells = int(first_line[3])

print rows,columns,minIngred,maxCells

pizza = [[]]

currRow = 0

for char in f.read():
	if (char != "\n"):
		pizza[currRow].append(char)
	else:
		currRow +=1
		pizza.append([])


#print(pizza[0][0])
print "Pizza uit file \"" + filename + "\" in 2-dimensionele lijst:"
for row in pizza:
	print row

'''
def printFromCoords(x1, y1, x2, y2):
	rows = y2-y1
	columns = x2-x1
	i = 0
	o = 0
	while (i < rows):
		print pizza[y1+i][x1:x2]
		while (o < columns):
			pizza[y1+i][x1+o] = "0"
			o += 1
		o = 0
		i += 1

newline()
printFromCoords(4,3,7,6)

newline()
for row in pizza:
	print row
'''

def sliceFromCoords(x1, y1, x2, y2):
	slice = []
	rows = y2-y1
	columns = x2-x1
	i = 0
	o = 0

	newline()
	print( "Slice tussen coordinaten ("+str(x1)+","+str(y1)+") en ("+str(x2)+","+str(y2)+"):" )

	while (i < rows):
		slice.append(pizza[y1+i][x1:x2])
		print(pizza[y1+i][x1:x2])
		while (o < columns):
			pizza[y1+i][x1+o] = "0"
			o += 1
		o = 0
		i += 1
	return slice

'''
newline()
slice = sliceFromCoords(4,3,7,6)
print(slice)
'''

def checkForIngredients(x1, y1, x2, y2):
	containsEnoughMushroom = False
	containsEnoughTomato = False

	amountOfSquares = (y2-y1)*(x2-x1)

	slice = sliceFromCoords(x1, y1, x2, y2)
	#newline()
	#print(slice)

	m = 0
	t = 0

	for lst in slice:
		for ingred in lst:
			if ingred == "M":
				m += 1
			if ingred == "T":
				t += 1

	if m >= minIngred:
		containsEnoughMushroom = True
	if t >= minIngred:
		containsEnoughTomato = True

	if (containsEnoughMushroom and containsEnoughTomato):
		return amountOfSquares #aantal punten voor de square
	else:
		return 0 #square is ongeldig (niet genoeg van elk ingred)


#sliceIsCorrect = checkForIngredients(4,3,7,6)
sliceIsCorrect = checkForIngredients(0,0,3,6)

newline()
print( "Zit het minimum aantal per ingredient (>=" + str(minIngred) + ") in de Slice?" )
print( "Zo ja, aantal punten (0 = incorrecte slice):" )
print(sliceIsCorrect)


def possibleDimensions():
    #maxCells = 25
    lst = []
    for i in range(1,maxCells+1):
    	lst.append(i)

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
    #for row in lstDim:
    #    print row
    
    return lstDim

newline()
print possibleDimensions()










