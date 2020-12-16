file = open("03.txt")
numTree = 0
xInc = 3
x = 0
for line in file:
    xPeriod = len(line.strip())
    x = x % xPeriod
    feature = line[x]
    if feature == "#":
        numTree += 1
    x += xInc
    
print(numTree)
