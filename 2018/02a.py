def getCharCountSet(boxId):
    charCount = {}
    for i in boxId:
        if i not in charCount:
            charCount[i] = 1
        else:
            charCount[i] += 1
    charCountSet = set()
    for k,v in charCount.items():
        charCountSet.add(v)
    return charCountSet


#print(getCharCountSet("abcdef"))
#print(getCharCountSet("bababc"))
#print(getCharCountSet("abbcde"))


file = open("02.txt")
#sum = 0
twoCount = 0
threeCount = 0
for line in file:
    charCountSet = getCharCountSet(line)
    if 2 in charCountSet:
        twoCount += 1
    if 3 in charCountSet:
        threeCount += 1

print(twoCount * threeCount)
