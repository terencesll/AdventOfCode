file = open("09.txt")

def valid(preamble, entry):
    for i in preamble:
        supplement = entry - i
        if supplement != i and supplement in preamble:
            return True
    return False

preamble = []
preambleSize = 25
invalid = 0
entries = list(map(lambda x: int(x.strip()), file.readlines()))
for entry in entries:
    if len(preamble) < preambleSize:
        preamble.append(entry)
        continue
    if valid(preamble, entry):
        preamble.pop(0)
        preamble.append(entry)
    else:
        invalid = entry
        break

print(invalid)

# O(n^3) instead of O(n^2) 
for i in range(len(entries)):
    for j in range(i+1, len(entries)):
        thisSum = sum(entries[i:j])
        if thisSum == invalid:
            print(entries[i:j])
            print(min(entries[i:j]))
            print(max(entries[i:j]))
            print(min(entries[i:j]) + max(entries[i:j]))
        elif thisSum > invalid:
            break
