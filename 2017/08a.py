file = open("08.txt")
registers = {}
maxVal = 0
for line in file:
        tokens = line.split()
        register = tokens[0]
        instruction = tokens[1]
        argument = int(tokens[2])
        condVar = tokens[4]
        condComp = tokens[5]
        condArg = int(tokens[6])
        if condVar not in registers:
            registers[condVar] = 0
        if condComp == "==":
            condVal = registers[condVar] == condArg
        elif condComp == "!=":
            condVal = registers[condVar] != condArg
        elif condComp == ">":
            condVal = registers[condVar] > condArg
        elif condComp == "<":
            condVal = registers[condVar] < condArg
        elif condComp == ">=":
            condVal = registers[condVar] >= condArg
        elif condComp == "<=":
            condVal = registers[condVar] <= condArg

        if condVal:
            if register not in registers:
                registers[register] = 0
            if instruction == "inc":
                registers[register] += argument
            elif instruction == "dec":
                registers[register] -= argument
            if registers[register] > maxVal:
                maxVal = registers[register]

print(registers)
print(maxVal)
