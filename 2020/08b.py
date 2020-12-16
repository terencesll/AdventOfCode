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
        
def getFinalState(instructions):
    state = State(0, 0)
    seenInst = set()
    while state.nextInst not in seenInst:
        #print(state)
        seenInst.add(state.nextInst)
        instruction = instructions[state.nextInst]
        #print(instruction)
        state = doNext(state, instruction)
        if state.nextInst >= len(instructions):
            break

    #print(state)
    return state

#print(getFinalState(instructions))

for i in range(len(instructions)):
    instruction = instructions[i]
    if instruction.op == "acc":
        continue
    thisInstructions = instructions.copy()
    if instruction.op == "nop":
        thisInstructions[i] = Instruction("jmp", instruction.arg)
    elif instruction.op == "jmp":
        thisInstructions[i] = Instruction("nop", instruction.arg)
    state = getFinalState(thisInstructions)
    if state.nextInst >= len(instructions):
        print(state)
        break
