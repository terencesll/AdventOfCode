import pprint
pp = pprint.PrettyPrinter(indent=4)

class Scanner:
    def __init__(self, layer, scanRange):
        self.layer = layer
        self.scanRange = scanRange
        self.position = 0
        self.direction = 1

    def advance(self):
        if self.position == 0:
            self.direction = 1
        elif self.position == self.scanRange - 1:
            #print("layer %d pos %s range %d" % (self.layer, self.position, self.scanRange))
            self.direction = -1
        self.position += self.direction

    def __repr__(self):
        return str(self.__dict__)

file = open("13.txt")
scanners = {}
fullDepth = 0

for line in file:
    tokens = line.split(": ")
    layer = int(tokens[0])
    scanRange = int(tokens[1])
    scanners[layer] = Scanner(layer, scanRange)
    fullDepth = layer

#pp.pprint(scanners)

def getSeverity(scanners, delay):
    for i in range(delay):
        for scanner in scanners.values():
            scanner.advance()
    severity = 0
    for i in range(fullDepth+1):
        #print(i)
        if i in scanners:
            if scanners[i].position == 0:
                #severity = 1
                severity += scanners[i].layer * scanners[i].scanRange
                print("layer: %d severity: %d sum: %d" % (i, scanners[i].layer * scanners[i].scanRange, severity))
        for scanner in scanners.values():
            scanner.advance()
        #pp.pprint(scanners)
    return severity

print(getSeverity(scanners, 0))

for i in range(1, 10):
    for scanner in scanners.values():
        scanner.position = 0
        scanner.direction = 1
    severity = getSeverity(scanners, i)
    print("%d: %d" % (i, severity))
    if severity == 0:
        print("%d: %d" % (i, severity))
        break
    elif i % 100 == 0:
        print(i)
