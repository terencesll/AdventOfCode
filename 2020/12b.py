import collections

Coordinate = collections.namedtuple('Coordinate', 'x y')
State = collections.namedtuple('State', 'location direction')
Instruction = collections.namedtuple('Instruction', 'op arg')

def madd(a, b, c):
    return Coordinate(a*b.x + c.x, a*b.y + c.y)

dirs = {"N": Coordinate(0,1), "S": Coordinate(0,-1), "E": Coordinate(1,0), "W": Coordinate(-1,0)}
def rTurn(direction):
    return Coordinate(direction.y, -direction.x)
def lTurn(direction):
    return Coordinate(-direction.y, direction.x)

def doNext(state, instruction):
    if instruction.op == "F":
        return State(madd(instruction.arg, state.direction, state.location), state.direction)
    
    elif instruction.op in "LR":
        direction = state.direction
        for i in range((instruction.arg // 90) % 4):
            if instruction.op  == "L":
                direction = lTurn(direction)
            else:
                direction = rTurn(direction)
        return State(state.location, direction)
    
    elif instruction.op in "NSEW":
        direction = dirs[instruction.op]
        return State(state.location, madd(instruction.arg, direction, state.direction))

    else: #bad
        return state
    

state = State(Coordinate(0,0), Coordinate(10,1))
file = open("12.txt")
#file = ["F10", "N3", "F7", "R90", "F11"]
for line in file:
    line = line.strip()
    instruction = Instruction(line[0], int(line[1:]))
    state = doNext(state, instruction)
    #print(state)

#print(state)
print(abs(state.location.x) + abs(state.location.y))
