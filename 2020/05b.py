file = open("05.txt")

def seat(code):
    row = int(code[:7].replace("F", "0").replace("B", "1"), 2)
    column = int(code[7:].replace("L", "0").replace("R", "1"), 2)
    return (row, column)

def seatId(rowColumn):
    return rowColumn[0]*8+rowColumn[1]

maxSeatId = 0
minSeatId = 1000
sumSeatId = 0
seatCount = 0
for line in file:
    currSeatId = seatId(seat(line.strip()))
    if currSeatId > maxSeatId:
        maxSeatId = currSeatId
    if currSeatId < minSeatId:
        minSeatId = currSeatId
    sumSeatId += currSeatId
    seatCount += 1

print(minSeatId)
print(maxSeatId)
print(sumSeatId)
print(seatCount)

print((minSeatId + maxSeatId) / 2 * (seatCount + 1) - sumSeatId)
