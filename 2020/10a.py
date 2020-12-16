file = open("10.txt")

jolts = list(map(lambda x: int(x.strip()), file.readlines()))
jolts.sort()
jolts.insert(0, 0)
jolts.append(jolts[-1]+3)
print (jolts)
joltDiffs = list(map(lambda x, y: x - y, jolts[1:], jolts[:-1]))
print(joltDiffs)
print(len(list(filter(lambda x: x == 1, joltDiffs))) * len(list(filter(lambda x: x == 3, joltDiffs))))

countOfConsecOnes = {}
numConsecOnes = 0
for i in joltDiffs:
    if i == 1:
        numConsecOnes += 1
    else:
        if numConsecOnes not in countOfConsecOnes:
            countOfConsecOnes[numConsecOnes] = 0
        countOfConsecOnes[numConsecOnes] += 1
        numConsecOnes = 0

print(countOfConsecOnes)

# 1 -> 1
# 2 -> 11, 2
# 3 -> 111, 12, 21, 3
# 4 -> 1111, 112, 121, 211, 22, 13, 31

print(2**countOfConsecOnes[2] * 4**countOfConsecOnes[3] * 7**countOfConsecOnes[4])
#print(countOfConsecOnes[2]*2 * countOfConsecOnes[3]*4)
