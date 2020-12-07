charCountByLoc = []
for i in range(8):
    charCountByLoc.append({})

for line in open("06a.txt"):
    line = line.rstrip("\n")
    for i in range(len(line)):
        thisChar = line[i]
        if thisChar not in charCountByLoc[i]:
            charCountByLoc[i][thisChar] = 0
        charCountByLoc[i][thisChar] += 1

for i in range(8):
    print(sorted(charCountByLoc[i], key=charCountByLoc[i].get, reverse=True)[0])
for i in range(8):
    print(sorted(charCountByLoc[i], key=charCountByLoc[i].get)[0])
