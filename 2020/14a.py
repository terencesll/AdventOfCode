import collections
file = open("14.txt")
#file = ["mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X","mem[8] = 11","mem[7] = 101","mem[8] = 0"]

Mask = collections.namedtuple('Mask', 'andMask orMask')
mem = {}
mask = Mask(0, 0)
for line in file:
    tokens = line.strip().split(" = ")
    if tokens[0] == "mask":
        andMask = int(tokens[1].replace("X", "1"), 2)
        orMask = int(tokens[1].replace("X", "0"), 2)
        mask = Mask(andMask, orMask)
    else:
        address = int(tokens[0][4:-1])
        value = int(tokens[1])
        mem[address] = value & mask.andMask | mask.orMask

print(sum(mem.values()))
