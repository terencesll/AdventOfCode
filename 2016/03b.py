def goodTri(lengths):
        lengths.sort();
        return lengths[0] + lengths[1] > lengths[2]

file = open("03a.txt")
numGoodTri = 0
index = 0
mod = 3
buff = list(range(9))
for line in file:
        token = line.split()
        #print(token)
        lengths = list(map(int, token))
        if index == mod:
                index = 0
        buff[index*mod:(index+1)*mod] = lengths
        #print(lengths)
        #lengths.sort()
        if index == mod - 1:
                for i in range(mod):
                        numGoodTri += goodTri(buff[i:mod*mod:mod])
        index += 1
print(numGoodTri)
