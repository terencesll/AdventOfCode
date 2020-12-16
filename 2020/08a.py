import collections
file = open("08.txt")

Instruction = collections.namedtuple('Instruction', 'op arg')
instructions = []

for line in file:
    tokens = line.strip().split()
    instructions.append(Instruction(tokens[0], int(tokens[1])))

State = collections.namedtuple('State', 'nextInst acc')

def doNext(state, instruction):
    nextState = State(state.nextInst, state.acc)
    if instruction.op == "nop":
        return State(state.nextInst + 1, state.acc)
    elif instruction.op == "acc":
        return State(state.nextInst + 1, state.acc + instruction.arg)
    elif instruction.op == "jmp":
        return State(state.nextInst + instruction.arg, state.acc)
    else: #bad
        return state
        

state = State(0, 0)

seenInst = set()

while state.nextInst not in seenInst:
    print(state)
    seenInst.add(state.nextInst)
    instruction = instructions[state.nextInst]
    print(instruction)
    state = doNext(state, instruction)

print(state)
