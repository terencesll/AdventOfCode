class Bag:
    def __init__(self, line):
        tokens = line.replace(".", "").split(" contain ")
        self.color = tokens[0][:-5]
        self.size = 0
        self.contains = []
        if tokens[1] == "no other bags":
            self.size = 1
        else:
            neighbors = tokens[1].split(",")
            for neighbor in neighbors:
                tokens2 = neighbor.strip().split(" ")
                self.contains.append((int(tokens2[0]), tokens2[1] + " " + tokens2[2]))

    def __repr__(self):
        return "{} {} {}".format(self.color, self.size, self.contains)
        

file = open("07.txt")
bags = {}

for line in file:
    bag = Bag(line.strip())
    bags[bag.color] = bag


def size(bagColor):
    bag = bags[bagColor]
    if bag.size != 0:
        return bag.size
    else:
        thisSize = 1
        for (num, color) in bag.contains:
            thisSize = thisSize + (num * size(color))
        bag.size = thisSize
        return thisSize

# -1 to not count shiny gold bag itself
print(size("shiny gold") - 1)
