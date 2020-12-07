file = open("07.txt")

# root is ahnofa

class Tower:
    def __init__(self, name, weight, members):
        self.name = name
        self.weight = weight
        self.totalWeight = 0
        self.members = members
        #print(self)

    def calcTotalWeight(self, towerMap):
        if not self.totalWeight:
            self.totalWeight += self.weight
            eachMemberWeight = 0
            for i in self.members:
                self.totalWeight += towerMap[i].calcTotalWeight(towerMap)
                if not eachMemberWeight:
                    eachMemberWeight = towerMap[i].totalWeight
                elif towerMap[i].totalWeight != eachMemberWeight:
                    print("%s unbalanced eachMemberWeight:%d %s:%d" % (self.name, eachMemberWeight, i, towerMap[i].totalWeight))
                    print(towerMap[i])
            #print(self)
        return self.totalWeight

    def __repr__(self):
        return "%s %d %d %s" % (self.name, self.weight, self.totalWeight, self.members)

towerMap = {}
for line in file:
        tokens = line.split()
        name = tokens[0]
        weight = int(tokens[1][1:-1])
        members = []
        if len(tokens) > 3:
            for token in tokens[3:]:
                members.append(token.rstrip(","))
        towerMap[name] = Tower(name, weight, members)

#print(towerMap["cianrio"])
#print(towerMap["cianrio"].calcTotalWeight(towerMap))
#print(towerMap["bxqlx"])
print(towerMap["ahnofa"].calcTotalWeight(towerMap))
