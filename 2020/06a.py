file = open("06.txt")
answer = set()
answers = []
for line in file:
    line = line.strip()
    if line:
        answer = answer.union(set(line))
    else:
        answers.append(answer)
        answer = set()

# No trigger to add last answer; do it after end of loop
answers.append(answer)
#print(len(passports))
numAnswers = 0
for answer in answers:
    # loose but easy test
    numAnswers += len(answer)

print(numAnswers)
