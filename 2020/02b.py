file = open("02.txt")
numValid = 0
for line in file:
    tokens = line.split(":")
    policy = tokens[0].split(" ")
    policyMinMax = policy[0].split("-")
    policyMin = int(policyMinMax[0])
    policyMax = int(policyMinMax[1])
    policyLetter = policy[1]
    password = tokens[1].strip()
    count = { policyLetter: 0}
    first = len(password) >= policyMin and password[policyMin-1] == policyLetter
    second = len(password) >= policyMax and password[policyMax-1] == policyLetter
    valid = first ^ second
    if valid:
        numValid += 1
    
print(numValid)
