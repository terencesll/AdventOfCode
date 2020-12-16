
def ski(down, right):
    # TODO: read once!
    file = open("03.txt")
    numTree = 0
    x = 0
    y = 0
    for line in file:
        if y % down == 0:
            xPeriod = len(line.strip())
            x = x % xPeriod
            feature = line[x]
            if feature == "#":
                numTree += 1
            x += right
        y += 1
    return numTree
    
print(ski(1,1)*ski(1,3)*ski(1,5)*ski(1,7)*ski(2,1))
