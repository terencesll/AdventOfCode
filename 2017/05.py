file = open("05.txt")

jumps = [int(line) for line in file]

        
print(jumps)
currInst = 0
steps = 0
while currInst < len(jumps):
    nextInst = currInst + jumps[currInst]
    if jumps[currInst] >= 3:
        jumps[currInst] -= 1
    else:
        jumps[currInst] += 1
    currInst = nextInst
    steps += 1

print(steps)
