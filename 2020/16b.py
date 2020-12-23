import collections
file = open("16.txt")

# Check python lambda capture; using a function simulates capturing by value
def createRule(minmaxes):
    return lambda x: x>=minmaxes[0] and x<=minmaxes[1] or x>=minmaxes[2] and x<=minmaxes[3]

rules = {}
line = file.readline().strip()
while line:
    # rules
    tokens = line.strip().split(": ")
    ruleName = tokens[0]
    tokens = tokens[1].split(" or ")
    minmaxes = []
    for token in tokens:
        minmax = token.split("-")
        minmaxes.append(int(minmax[0]))
        minmaxes.append(int(minmax[1]))
    rules[ruleName] = createRule(minmaxes)
    line = file.readline().strip()

line = file.readline().strip() #your ticket:
line = file.readline().strip() #83,53,73,139,127,131,97,113,61,101,107,67,79,137,89,109,103,59,149,71
myTicket = list(map(int, line.split(",")))
line = file.readline().strip() #
line = file.readline().strip() #nearby tickets:

tickets = []
line = file.readline().strip()
while line:
    tickets.append(list(map(int, line.split(","))))
    line = file.readline().strip()

def isValid(rules, value):
    for rule in rules.values():
        if rule(value):
            return True
    return False

validTickets = []
for ticket in tickets:
    thisTicketIsValid = True
    for value in ticket:
        if not isValid(rules, value):
            thisTicketIsValid = False
            break
    if thisTicketIsValid:
        validTickets.append(ticket)

print(len(tickets))
print(len(validTickets))

ruleToColIndices = {}

for ruleName, rule in rules.items():
    ruleToColIndices[ruleName] = []
    for i in range(len(rules)):
        wholeColumnValid = True
        for ticket in validTickets:
            if not rule(ticket[i]):
                wholeColumnValid = False
                break
        if wholeColumnValid:
            ruleToColIndices[ruleName].append(i)

print(ruleToColIndices)

ruleToColIndex = {}

while ruleToColIndices:
    for ruleName, colIndices in ruleToColIndices.items():
        if len(colIndices) == 1:
            thisIndex = colIndices[0]
            ruleToColIndex[ruleName] = thisIndex
            break
    ruleToColIndices.pop(ruleName)
    for colIndices in ruleToColIndices.values():
        colIndices.remove(thisIndex)

print(ruleToColIndex)

answer = 1
for ruleName, index in ruleToColIndex.items():
    if ruleName.startswith("departure"):
        print(myTicket[index])
        answer *= myTicket[index]
print(answer)
