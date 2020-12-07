file = open("04.txt")
invalidCount = 0
count = 0
for line in file:
        tokens = line.split()
        words = set()
        for token in tokens:
            if str(sorted(token)) not in words:
                words.add(str(sorted(token)))
            else:
                invalidCount += 1
                break
        count += 1
print(count - invalidCount)
        
