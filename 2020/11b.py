import copy
import collections

Coordinate = collections.namedtuple('Coordinate', 'x y')
Grid = collections.namedtuple('Grid', 'grid xMax yMax')

def cloneGrid(grid):
    return Grid(copy.deepcopy(grid.grid), grid.xMax, grid.yMax)

def inGrid(grid, seat):
    return seat.x >=0 and seat.x < grid.xMax and seat.y >=0 and seat.y < grid.yMax

def getFeature(grid, seat):
    return grid.grid[seat.y][seat.x]

def sees(grid, seat, direction):
    nextCoordinate = Coordinate(seat.x + direction.x, seat.y + direction.y)
    while inGrid(grid, nextCoordinate):
        feature = getFeature(grid, nextCoordinate)
        if feature != ".":
            return feature
        nextCoordinate = Coordinate(nextCoordinate.x + direction.x, nextCoordinate.y + direction.y)
    return "."

def sumOccupied(grid, seat):
    currSum = 0
    for yi in range(-1,2):
        for xi in range(-1,2):
            if xi != 0 or yi != 0:
                direction = Coordinate(xi, yi)
                feature = sees(grid, seat, direction)
                #print("Seat:{} dir:{} feature:{}".format(seat, direction, feature))
                if feature == '#':
                    currSum += 1
    return currSum

def advance(grid):
    nextGrid = cloneGrid(grid)
    for yi in range(grid.yMax):
        for xi in range(grid.xMax):
            seat = Coordinate(xi, yi)
            #print("seat: {} feature:{}".format(seat, getFeature(grid, seat)))
            if grid.grid[yi][xi] == 'L':
                if sumOccupied(grid, seat) == 0:
                    nextGrid.grid[yi][xi] = '#'
            elif grid.grid[yi][xi] == '#':
                #print("seat: {} feature:{} sumOccupied:{}".format(seat, getFeature(grid, seat), sumOccupied(grid, seat)))
                if sumOccupied(grid, seat) >= 5:
                    nextGrid.grid[yi][xi] = 'L'
    return nextGrid

def numOccupied(grid):
    # figure out how to do reduce
    currSum = 0
    for i in grid.grid:
        for j in i:
            if j == '#':
                currSum += 1
    return currSum

file = open("11.txt")
seats = list(map(lambda x: list(x.strip()), file.readlines()))
#print(list(map(lambda x: "".join(x), seats)))
grid = Grid(seats, len(seats[0]), len(seats))

lastNumOccupied = 0
grid = advance(grid)
#print(list(map(lambda x: "".join(x), grid.grid)))
currNumOccupied = numOccupied(grid)
print(currNumOccupied)
while currNumOccupied != lastNumOccupied:
    lastNumOccupied = currNumOccupied
    grid = advance(grid)
    #print(list(map(lambda x: "".join(x), grid.grid)))
    currNumOccupied = numOccupied(grid)
    print(currNumOccupied)
    

