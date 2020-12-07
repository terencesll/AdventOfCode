import math

a = 265149
#a = 27

gridwidth = math.ceil(math.sqrt(200))
gridwidth = gridwidth if gridwidth % 2 else gridwidth + 1
semiwidth = int(gridwidth / 2)
print("gridwidth:%s semiwidth:%s" % (type(gridwidth), type(semiwidth)))
print("gridwidth:%d semiwidth:%d" % (gridwidth, semiwidth))

grid = [[0 for x in range(gridwidth)] for y in range(gridwidth)]

def getCoord(grid, semiwidth, x, y):
    return grid[semiwidth-y][x + semiwidth] if abs(x) <= semiwidth and abs(y) <= semiwidth else 0

def setCoord(grid, semiwidth, x, y, value):
    grid[semiwidth-y][x + semiwidth] = value
    if value > a:
        print(value)
        #system.exit()

def getNeightborSum(grid, semiwidth, x, y):
    val = 0;
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            #print("x:%d dx:%d y:%d dy:%d" % (x, dx, y, dy))
            if not (dx == 0 and dy == 0):
                #print("x:%d dx:%d y:%d dy:%d val:%d" % (x, dx, y, dy, getCoord(grid, semiwidth, x+dx, y+dy)))
                val += getCoord(grid, semiwidth, x+dx, y+dy)
    return val
    
val = 0
for i in range(1, gridwidth+1):
    s = int(i/2)
    if i == 1:
        val = 1
        setCoord(grid, semiwidth, 0, 0, val)
    elif i % 2 == 1:
        for y in range(s,-s,-1):
            val = getNeightborSum(grid, semiwidth, -s, y)
            print("i:%d x:%d y:%d val:%d" % (i, -s, y, val))
            setCoord(grid, semiwidth, -s, y, val)
        for x in range(-s,s+1):
            val = getNeightborSum(grid, semiwidth, x, -s)
            print("i:%d x:%d y:%d val:%d" % (i, x, -s, val))
            setCoord(grid, semiwidth, x, -s, val)
    else:
        for y in range(1-s,s):
            val = getNeightborSum(grid, semiwidth, s, y)
            print("i:%d x:%d y:%d val:%d" % (i, s, y, val))
            setCoord(grid, semiwidth, s, y, val)
        for x in range(s,-s,-1):
            val = getNeightborSum(grid, semiwidth, x, s)
            print("i:%d x:%d y:%d val:%d" % (i, x, s, val))
            setCoord(grid, semiwidth, x, s, val)

#print(grid)
