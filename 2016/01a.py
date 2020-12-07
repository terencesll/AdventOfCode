class Walker:
    def __init__(self):
        self.dir = (0, 1)
        self.pos = [0, 0]
        self.turnmap = {}
        self.turnmap['R'] = {}
        self.turnmap['R'][(0,1)] = (1,0)
        self.turnmap['R'][(1,0)] = (0,-1)
        self.turnmap['R'][(0,-1)] = (-1,0)
        self.turnmap['R'][(-1,0)] = (0,1)
        self.turnmap['L'] = {}
        self.turnmap['L'][(0,1)] = (-1,0)
        self.turnmap['L'][(-1,0)] = (0,-1)
        self.turnmap['L'][(0,-1)] = (1,0)
        self.turnmap['L'][(1,0)] = (0,1)
        self.visited = set()

    def go(self, chirality, steps):
        self.dir = self.turnmap[chirality][self.dir]
        for i in range(steps):
            for i in (0, 1):
                self.pos[i] += self.dir[i]
            if tuple(self.pos) in self.visited:
                print("visisted:" + str(self.pos))
            self.visited.add(tuple(self.pos))

    def __repr__(self):
        return str([self.dir, self.pos])

fred = Walker()

instruction = "L4, L1, R4, R1, R1, L3, R5, L5, L2, L3, R2, R1, L4, R5, R4, L2, R1, R3, L5, R1, L3, L2, R5, L4, L5, R1, R2, L1, R5, L3, R2, R2, L1, R5, R2, L1, L1, R2, L1, R1, L2, L2, R4, R3, R2, L3, L188, L3, R2, R54, R1, R1, L2, L4, L3, L2, R3, L1, L1, R3, R5, L1, R5, L1, L1, R2, R4, R4, L5, L4, L1, R2, R4, R5, L2, L3, R5, L5, R1, R5, L2, R4, L2, L1, R4, R3, R4, L4, R3, L4, R78, R2, L3, R188, R2, R3, L2, R2, R3, R1, R5, R1, L1, L1, R4, R2, R1, R5, L1, R4, L4, R2, R5, L2, L5, R4, L3, L2, R1, R1, L5, L4, R1, L5, L1, L5, L1, L4, L3, L5, R4, R5, R2, L5, R5, R5, R4, R2, L1, L2, R3, R5, R5, R5, L2, L1, R4, R3, R1, L4, L2, L3, R2, L3, L5, L2, L2, L1, L2, R5, L2, L2, L3, L1, R1, L4, R2, L4, R3, R5, R3, R4, R1, R5, L3, L5, L5, L3, L2, L1, R3, L4, R3, R2, L1, R3, R1, L2, R4, L3, L3, L3, L1, L2"

for i in instruction.split(", "):
    fred.go(i[0], int(i[1:]))
