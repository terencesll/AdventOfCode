file = open("01.txt")
freqs = [int(line) for line in file]
#freqs = [+3, +3, +4, -2, -4]
#print(freqs)
seen = set()
done = False
sumFreq = 0
numCycle = 0
seen.add(sumFreq)
while not done:
    for freq in freqs:
        sumFreq += freq
        if sumFreq in seen:
            print(sumFreq)
            done = True
            break
        else:
            seen.add(sumFreq)
    numCycle += 1
    print("numCycle:%d" % numCycle)
