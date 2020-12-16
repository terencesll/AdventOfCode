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

def hgtTest(x):
    unit = x[-2:]
    if unit not in ["cm", "in"]:
        return False
    value = int(x[:-2])
    if unit == "cm":
        return value >= 150 and value <= 193
    elif unit == "in":
        return value >= 59 and value <= 76
    else:
        return False

def hclTest(x):
    if len(x) != 7:
        return False
    if x[0] != "#":
        return False
    for c in x[1:]:
        if c not in "0123456789abcdef":
            return False;
    return True

def pidTest(x):
    if len(x) != 9:
        return False
    for c in x[1:]:
        if c not in "0123456789":
            return False;
    return True

numValid = 0
predicates = {
    "byr": lambda x : int(x) >= 1920 and int(x) <= 2002,
    "iyr": lambda x : int(x) >= 2010 and int(x) <= 2020,
    "eyr": lambda x : int(x) >= 2020 and int(x) <= 2030,
    "hgt": hgtTest,
    "hcl": hclTest,
    "ecl": lambda x : x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": pidTest
    }
for passport in passports:
    # loose but easy test
    if len(passport) == 8 or len(passport) == 7 and "cid" not in passport:
        isValid = True
        #print(passport)
        for field in predicates:
            if not predicates[field](passport[field]):
                isValid = False
        if isValid:
            numValid += 1

print(numValid)
