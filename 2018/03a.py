
fabric = []
for i in range(1000):
    fabric.append([0] * 1000)

file = open("03.txt")

for line in file:
    ##1269 @ 306,634: 28x28
    #print(line)
    tokens = line.split(" @ ", 1)
    #print(tokens)
    num = int(tokens[0].split("#")[1])
    #print(num)
    tokens = tokens[1].split(": ")
    #print(tokens)
    [x, y] = [int(i) for i in tokens[0].split(",", 1)]
    [lenx, leny] = [int(i) for i in tokens[1].split("x", 1)]
    #print("%d %d %d %d" % (x, y, lenx, leny))
    for i in range(x, x+lenx):
        #print(i)
        for j in range(y, y+leny):
            fabric[i][j] += 1
            #print(fabric[i])

count = 0
for i in fabric:
    for j in i:
        if j > 1:
            count += 1

print(count)

for i, row in enumerate(fabric):
    for j, cell in enumerate(row):
        if cell == 1:
            print("%d %d" % (i, j))
