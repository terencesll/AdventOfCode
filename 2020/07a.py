file = open("07.txt")
edges = []
for line in file:
    tokens = line.strip().replace(".", "").split(" contain ")
    curr = tokens[0][:-5]
    if tokens[1] == "no other bags":
        continue
    neighbors = tokens[1].split(",")
    for neighbor in neighbors:
        tokens2 = neighbor.strip().split(" ")
        #print(tokens2)
        edges.append((curr, int(tokens2[0]), tokens2[1] + " " + tokens2[2]))

#print(edges)

containedBy = {}
for edge in edges:
    if edge[2] not in containedBy:
        containedBy[edge[2]] = []
    containedBy[edge[2]].append((edge[0], edge[1]))

#print(containedBy)

candidate = ["shiny gold"]
visited = set()

while candidate:
    curr = candidate.pop(0)
    visited.add(curr)
    if curr in containedBy:
        for neighbors in containedBy[curr]:
            candidate.append(neighbors[0])
    #print(candidate)
    #print(visited)
    #print("{} {}".format(len(candidate), len(visited)))

# -1 for shiny gold
print(len(visited) - 1)
