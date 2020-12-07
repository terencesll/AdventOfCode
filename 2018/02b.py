def diffCharCount(lhs, rhs):
    diff = 0
    for i in range(len(lhs)):
        if lhs[i] != rhs[i]:
            diff += 1
    return diff;

#print(getCharCountSet("abcdef"))
#print(getCharCountSet("bababc"))
#print(getCharCountSet("abbcde"))


file = open("02.txt")
boxIds = [line for line in file]
#print(charCounts)

for i, lhs in enumerate(boxIds):
    #print(i)
    for j in range(i+1, len(boxIds)):
        rhs = boxIds[j]
        diffC = diffCharCount(lhs, rhs)
    #for j, rhs in enumerate(charCounts[i+1:]):
        #print("%d, %d, %d" % (i, j, diffC))
        #print(rhs)
        if diffC == 1:
            print(lhs)
            print(rhs)

