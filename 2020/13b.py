import datetime

class Buses:
    def __init__(self, line):
        tokens = line.strip().split(",")
        busPeriodOffset = []
        
        for token in enumerate(tokens):
            if token[1] != "x":
                period = int(token[1])
                busPeriodOffset.append((period, token[0]%period))
        self.busPeriodOffset = sorted(busPeriodOffset, key=lambda item: item[0], reverse=True)

    def __repr__(self):
        return "{}".format(self.busPeriodOffset)

    def isValid(self, largestPeriodNum):
        offsetZeroTimestamp = self.busPeriodOffset[0][0] * largestPeriodNum - self.busPeriodOffset[0][1]
        #print(offsetZeroTimestamp)
        for period, offset in self.busPeriodOffset[1:]:
            #print("{} {} {}".format(period, offset, (offsetZeroTimestamp + offset) % period))
            if (offsetZeroTimestamp + offset) % period != 0:
                return (False, offsetZeroTimestamp)
        return (True, offsetZeroTimestamp)

file = open("13.txt")
file.readline()
buses = Buses(file.readline().strip())
#buses = Buses("1789,37,47,1889")

earliestDepartTime = 100000000000000
#earliestDepartTime = 1000000000

largestPeriodNum = earliestDepartTime // buses.busPeriodOffset[0][0]
while not buses.isValid(largestPeriodNum)[0]:
    if largestPeriodNum % 10000000 == 0:
        print("{} {} {}".format(datetime.datetime.now(), largestPeriodNum, buses.isValid(largestPeriodNum)[1]))
        print(largestPeriodNum)
        print(buses.isValid(largestPeriodNum)[1])
    largestPeriodNum += 1

print(largestPeriodNum)
print(buses.isValid(largestPeriodNum))
