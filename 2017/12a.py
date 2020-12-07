file = open("12.txt")

neighbors = {}
for line in file:
    tokens = line.split()
    neighbors[int(tokens[0])] = []
    for i in range(2, len(tokens)):
        neighbors[int(tokens[0])].append(int(tokens[i].rstrip(",")))

#print(neighbors)

def getGroup(neighbors, root):
    candidate = []
    candidate.append(root)
    visited = []

    while candidate:
        curr = candidate.pop(0)
        visited.append(curr)
        for i in neighbors[curr]:
            if i not in candidate and i not in visited:
                candidate.append(i)
        #print(curr)
        #print(visited)
        #print(candidate)

    return visited
    #print(visited)
    #print(len(visited))

nodes = set(neighbors.keys())
#print(nodes)
numGroups = 0
while nodes:
    curr = next(iter(nodes))
    group = set(getGroup(neighbors, curr))
    nodes -= group
    numGroups += 1
    #print(nodes)
    #print(curr)
    #print(group)
    #print(len(nodes))

print(numGroups)
