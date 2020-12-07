import copy

class Screen:
    def __init__(self, x, y):
        self.xlim = x
        self.ylim = y
        self.screen = [ [0]*x for _ in range(y) ]

    def rect(self, x, y):
        for i in range(x):
            for j in range(y):
                self.screen[j][i] = 1
        print(self)

    def rotateColumn(self, x, n):
        col = [self.screen[j][x] for j in range(self.ylim)]
        for j in range(self.ylim):
            self.screen[(j+n)%self.ylim][x] = col[j]
        print(self)

    def rotateRow(self, y, n):
        row = copy.deepcopy(self.screen[y])
        self.screen[y][n:] = row[:self.xlim - n]
        self.screen[y][:n] = row[self.xlim - n:]
        print(self)

    def sumLit(self):
        value = 0
        for j in range(self.ylim):
            value += sum(self.screen[j])
        return value

    def __repr__(self):
        visualization = ""
        for i in self.screen:
            visualization += "".join(["#" if j is 1 else "." for j in i]) + "\n"
        return visualization

screen = Screen(50, 6)
#screen = Screen(7, 3)

for line in open("08a.txt"):
    line = line.rstrip("\n")
    print("line:" + line)
    tokens = line.split()
    print("tokens:" + str(tokens))
    if tokens[0] == "rect":
        tokens2 = tokens[1].split("x")
        screen.rect(int(tokens2[0]), int(tokens2[1]))
    elif tokens[0]== "rotate":
        index = int(tokens[2][2:])
        magnitude = int(tokens[4])
        if tokens[1] == "row":
            screen.rotateRow(index, magnitude)
        elif tokens[1] == "column":
            screen.rotateColumn(index, magnitude)

print(screen)
print(screen.sumLit())
