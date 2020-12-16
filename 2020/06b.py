file = open("06.txt")
answer = set()
answers = []
newGroup = True
for line in file:
    line = line.strip()
    if line:
        if newGroup:
            answer = set(line)
            newGroup = False
        else:
            answer = answer.intersection(set(line))
    else:
        answers.append(answer)
        answer = set()
        newGroup = True

# No trigger to add last answer; do it after end of loop
answers.append(answer)
#print(len(passports))
numAnswers = 0
for answer in answers:
    # loose but easy test
    numAnswers += len(answer)

print(numAnswers)
