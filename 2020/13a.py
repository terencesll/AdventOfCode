file = open("13.txt")
departTime = int(file.readline().strip())

busTimes = []
tokens = file.readline().strip().split(",")
for token in tokens:
    if token != "x":
        busTimes.append(int(token))

#print(busTimes)

earliestDepartBus = 0
earliestDepartTime = 2000000
for busTime in busTimes:
    busNum = departTime // busTime
    # assume there's always non-zero remainder
    thisDepartTime = (busNum + 1) * busTime
    if thisDepartTime < earliestDepartTime:
        earliestDepartTime = thisDepartTime
        earliestDepartBus = busTime
        print("earliestDepartTime={}, earliestDepartBus={}".format(earliestDepartTime, earliestDepartBus))

print((earliestDepartTime - departTime) * earliestDepartBus)
