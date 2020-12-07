file = open("03a.txt")
numGoodTri = 0
for line in file:
        token = line.split()
        #print(token)
        lengths = sorted(map(int, token))
        #print(lengths)
        #lengths.sort()
        if lengths[0] + lengths[1] > lengths[2]:
            numGoodTri += 1

print(numGoodTri)
