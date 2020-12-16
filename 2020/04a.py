file = open("04.txt")
passport = {}
passports = []
for line in file:
    line = line.strip()
    if line:
        tokens = line.split()
        for token in tokens:
            kvp = token.split(":")
            passport[kvp[0]] = kvp[1]
    else:
        passports.append(passport)
        passport = {}

# No trigger to add last passport; do it after end of loop
passports.append(passport)
#print(len(passports))
numValid = 0
for passport in passports:
    # loose but easy test
    if len(passport) == 8 or len(passport) == 7 and "cid" not in passport:
        numValid += 1

print(numValid)
