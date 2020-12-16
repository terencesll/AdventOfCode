import copy

file = open("11.txt")

seats = list(map(lambda x: list(x.strip()), file.readlines()))
print(list(map(lambda x: "".join(x), seats)))

def sumOccupied(seats, x, y, xMax, yMax):
    xSlice = list(filter(lambda x: x >=0 and x < xMax, list(range(x-1, x+2))))
    ySlice = list(filter(lambda x: x >=0 and x < yMax, list(range(y-1, y+2))))
    currSum = 0
    for yi in ySlice:
        for xi in xSlice:
            if xi != x or yi != y:
                #print("{} {} {} {} {}".format(x, y, xi, yi, seats[yi][xi]))
                if seats[yi][xi] == '#':
                    currSum += 1
    #print("{} {} {} {} {}".format(x, y, xSlice, ySlice, currSum))
    return currSum

def advance(seats):
    nextSeats = copy.deepcopy(seats)
    yMax = len(seats)
    xMax = len(seats[0])
    for yi in range(yMax):
        for xi in range(xMax):
            if seats[yi][xi] == 'L':
                if sumOccupied(seats, xi, yi, xMax, yMax) == 0:
                    nextSeats[yi][xi] = '#'
            elif seats[yi][xi] == '#':
                if sumOccupied(seats, xi, yi, xMax, yMax) >= 4:
                    nextSeats[yi][xi] = 'L'
    return nextSeats

def numOccupied(seats):
    # figure out how to do reduce
    currSum = 0
    for i in seats:
        for j in i:
            if j == '#':
                currSum += 1
    return currSum

lastNumOccupied = 0
seats = advance(seats)
currNumOccupied = numOccupied(seats)
print(currNumOccupied)
while currNumOccupied != lastNumOccupied:
    lastNumOccupied = currNumOccupied
    seats = advance(seats)
    currNumOccupied = numOccupied(seats)
    print(currNumOccupied)
    

