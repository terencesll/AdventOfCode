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
    for char in password:
        if char not in count:
            count[char] = 0
        count[char] += 1
    #print(count)
    if count[policyLetter] >= policyMin and count[policyLetter] <= policyMax:
        numValid += 1

print(numValid)
