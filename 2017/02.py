##file = open("02.txt")
##checksum = 0
##for line in file:
##        token = list(map(int, line.split()))
##        maxValue = max(token)
##        minValue = min(token)
##        checksum += maxValue - minValue

##print(checksum)

file = open("02.txt")
checksum = 0
for line in file:
        token = list(map(int, line.split()))
        token.sort(reverse=True)
        found = False
        for index, value in enumerate(token):
            print("%d, %d" % (index, value))
            for denom in token[index+1:]:
                if value % denom == 0:
                    checksum += value / denom
                    found = True
                    break
            if found:
                break

print(checksum)
