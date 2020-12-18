import collections
file = open("14.txt")
#file = ["mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X","mem[8] = 11","mem[7] = 101","mem[8] = 0"]
#file = ["mask = 000000000000000000000000000000X1001X","mem[42] = 100","mask = 00000000000000000000000000000000X0XX","mem[26] = 1"]

def getFloatMasks(digits):
    numMasks = 1 << len(digits)
    masks = [0] * numMasks
    for i, digit in enumerate(digits):
        value = 1 << digit
        #print("{} {} {}".format(i, digit, value))
        for j in range(numMasks):
            #print("j={} 1<<i={}".format(j, 1 << i))
            if j & 1 << i:
                #print("mask[{}] += {}".format(j, value))
                masks[j] += value
    return masks

Mask = collections.namedtuple('Mask', 'floatMasks orMask andMask')
mem = {}
mask = Mask([], 0, 0)
for line in file:
    tokens = line.strip().split(" = ")
    if tokens[0] == "mask":
        floatMask = int(tokens[1].replace("1", "0").replace("X", "1"), 2)
        orMask = int(tokens[1].replace("X", "0"), 2)
        andMask = int(tokens[1].replace("0", "1").replace("X", "0"), 2)
        floatDigits = []
        index = 0
        while floatMask:
            if floatMask % 2:
                floatDigits.append(index)
            floatMask >>= 1
            index += 1
        print(floatDigits)
        mask = Mask(getFloatMasks(floatDigits), orMask, andMask)
    else:
        address = int(tokens[0][4:-1])
        value = int(tokens[1])
        #print(bin(address))
        #print(bin(mask.orMask))
        #print(bin(mask.andMask))
        address = address & mask.andMask | mask.orMask
        #print(bin(address))

        for floatMask in mask.floatMasks:
            #print("mem[{}] = {}".format(address + floatMask, value))
            mem[address + floatMask] = value

print(sum(mem.values()))
