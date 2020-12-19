#startingNumbers = "3,1,2".split(",")
startingNumbers = "1,0,15,2,10,13".split(",")
turn = 0

prevTurn = {}
nextNumber = 0
#lastNumber = 0

for startingNumber in startingNumbers:
    turn += 1
    prevTurn[int(startingNumber)] = turn
    #lastNumber = startingNumber

while turn < 30000000:
    turn += 1
    thisNumber = nextNumber
    if nextNumber in prevTurn:
        nextNumber = turn - prevTurn[thisNumber]
    else:
        nextNumber = 0
    prevTurn[thisNumber] = turn
    if turn == 2020:
        print("{} {}".format(turn, thisNumber))
    #print("{} {} {} {}".format(turn, thisNumber, nextNumber, prevTurn))

print("{} {}".format(turn, thisNumber))
