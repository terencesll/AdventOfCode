import pprint
pp = pprint.PrettyPrinter(indent=4)
from collections import deque
import functools
import datetime

def gcd(*numbers):
    """Return the greatest common divisor of the given integers"""
    from fractions import gcd
    return functools.reduce(gcd, numbers)

# Least common multiple is not in standard libraries? It's in gmpy, but this is simple enough:

def lcm(*numbers):
    """Return lowest common multiple."""    
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return functools.reduce(lcm, numbers, 1)


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

class Firewall:
    def __init__(self, file):
        self.scanners = {}
        self.fullDepth = 0
        for line in file:
            tokens = line.split(": ")
            layer = int(tokens[0])
            scanRange = int(tokens[1])
            self.scanners[layer] = Scanner(layer, scanRange)
            self.fullDepth = layer

    def getPositions(self):
        positions = {}
        for scanner in self.scanners.values():
            positions[scanner.layer] = scanner.position
        return positions

    def advance(self):
        for scanner in self.scanners.values():
            scanner.advance()

    def maxCycle(self):
        factors = set()
        for scanner in self.scanners.values():
            factors.add(scanner.scanRange)
        product = 1
        for i in factors:
            product = lcm(product, (i-1)*2)
        return product
        
def getSeverity(positionss, fullDepth):
    severity = 0
    for i in range(fullDepth+1):
        #print(i)
        positions = positionss[i]
        if i in positions:
            if positions[i] == 0:
                severity += i+1
                #severity += scanners[i].layer * scanners[i].scanRange
                #print("severity: %d sum: %d" % (scanners[i].layer * scanners[i].scanRange, severity))
    return severity

file = open("13.txt")
firewall = Firewall(file)
print(firewall.maxCycle())

#pp.pprint(firewall.scanners)
#print(getSeverity(scanners, 0))
positionss = deque([])
positionss.append(firewall.getPositions())
for i in range(firewall.fullDepth):
    firewall.advance()
    positionss.append(firewall.getPositions())

severity = getSeverity(positionss, firewall.fullDepth)
#print("%d: %d" % (0, severity))
#pp.pprint(positionss)
for i in range(1,1000000000):
    positionss.popleft()
    firewall.advance()
    positionss.append(firewall.getPositions())
    #pp.pprint(positionss)

    severity = getSeverity(positionss, firewall.fullDepth)
    #print("%d: %d" % (i, severity))
    if severity == 0:
        print("%d: %d" % (i, severity))
        break
    elif i % 10000 == 0:
        print("%s: %d" % (datetime.datetime.now(), i))
