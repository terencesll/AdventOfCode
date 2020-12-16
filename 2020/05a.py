file = open("05.txt")

def seat(code):
    row = int(code[:7].replace("F", "0").replace("B", "1"), 2)
    column = int(code[7:].replace("L", "0").replace("R", "1"), 2)
    return (row, column)

def seatId(rowColumn):
    return rowColumn[0]*8+rowColumn[1]

#print(seatId(seat("FBFBBFFRLR")))
maxSeatId = 0
for line in file:
    currSeatId = seatId(seat(line.strip()))
    if currSeatId > maxSeatId:
        maxSeatId = currSeatId

print(maxSeatId)
