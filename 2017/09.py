file = open("09.txt")
#line = "{{{}}}"
#line = "{{<a!>},{<a!>},{<a!>},{<ab>}}"
#print(line)
#
#print(length)

i = 0
level = 0
score = 0
garbage = False
garbageCount = 0

line = tuple(file.readline())
length = len(line)
print(length)
while i < length:
    curr = line[i]
##while True:
##    if not curr:
##        break
##    curr = file.read(1)
    if curr == "!":
        i += 2
    elif garbage:
        if curr == ">":
            garbage = False
        else:
            garbageCount += 1
        i += 1
    elif curr == "{":
        level += 1
        print("%d: %d" % (i, level))
        i += 1
    elif curr == "}":
        score += level
        level -= 1
        print("%d: %d score:%d" % (i, level, score))
        i += 1
    elif curr == "<":
        garbage = True
        i += 1
    else:
        i += 1

print(level)
print(score)
print(garbageCount)
