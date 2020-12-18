import datetime

class Buses:
    def __init__(self, line):
        tokens = line.strip().split(",")
        busPeriodOffset = []
        print("Go find an online Chinese remainder theorem solver, and plug in:" )
        for token in enumerate(tokens):
            if token[1] != "x":
                period = int(token[1])
                offset = token[0] % period
                busPeriodOffset.append((period, offset))
                print("x = {} (mod {})".format((period - offset)%period, period))
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

