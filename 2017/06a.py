file = open("06.txt")
blocks = list(map(int, file.readline().split()))
numBlocks = len(blocks)

seenConfig = {}

def getMax(blocks):
    index = 0
    value = blocks[0]
    for i in range(1, len(blocks)):
        if blocks[i] > value:
            index = i
            value = blocks[i]
    return value, index

numCycle = 0
while tuple(blocks) not in seenConfig:
    seenConfig[tuple(blocks)] = numCycle
    value, index = getMax(blocks)
    blocks[index] = 0
    quotient = value // numBlocks
    reminder = value % numBlocks
    
    blocks = list(map(lambda x: x + quotient, blocks))
    for i in range(index+1, index+1+reminder):
        blocks[i%numBlocks] += 1
    #print(blocks)
    numCycle += 1

print(numCycle)
print(numCycle - seenConfig[tuple(blocks)])
