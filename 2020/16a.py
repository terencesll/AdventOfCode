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
    #print(minmaxes)
    rules[ruleName] = createRule(minmaxes)
    #print(rules[ruleName])
    #print(rules[ruleName](7))
    line = file.readline().strip()

#print(rules)

line = file.readline().strip() #your ticket:
line = file.readline().strip() #83,53,73,139,127,131,97,113,61,101,107,67,79,137,89,109,103,59,149,71
line = file.readline().strip() #
line = file.readline().strip() #nearby tickets:

tickets = []
line = file.readline().strip()
while line:
    tickets.append(list(map(int, line.split(","))))
    line = file.readline().strip()

#print(tickets)

def isValid(rules, value):
    for rule in rules.values():
        #print("{} {}".format(rule, value))
        if rule(value):
            #print("True")
            return True
    return False

errorRate = 0
for ticket in tickets:
    for value in ticket:
        if not isValid(rules, value):
            #print(value)
            errorRate += value

print(errorRate)
