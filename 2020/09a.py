file = open("09.txt")

def valid(preamble, entry):
    for i in preamble:
        supplement = entry - i
        if supplement != i and supplement in preamble:
            return True
    return False

preamble = []
preambleSize = 25
for line in file:
    entry = int(line)
    if len(preamble) < preambleSize:
        preamble.append(entry)
        continue
    if valid(preamble, entry):
        preamble.pop(0)
        preamble.append(entry)
    else:
        print(entry)
        break
