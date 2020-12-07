file = open("11.txt")
dirs = file.readline().split(",")
#dirs = "se,sw,se,sw,sw".split(",")
# x is SE
# y is S
# z is (1,-1) is NE

curr = [0, 0]
furthest = 0
for i in dirs:
    if i == "se":
        dir = [1, 0]
    elif i == "nw":
        dir = [-1, 0]
    elif i == "s":
        dir = [0, 1]
    elif i == "n":
        dir = [0, -1]
    elif i == "ne":
        dir = [1, -1]
    elif i == "sw":
        dir = [-1, 1]
    curr[0] += dir[0]
    curr[1] += dir[1]
    distance = max(abs(curr[0]), abs(curr[1]), abs(curr[0] + curr[1]))
    furthest = max(furthest, distance)

print(curr)
print(furthest)
