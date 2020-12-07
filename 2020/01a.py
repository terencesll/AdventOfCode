
file = open("01.txt")
seen = set()
requiredSumEntry = 2020
for line in file:
    entry = int(line)
    supplement = requiredSumEntry - entry
    if supplement in seen:
        print("{} {} {}".format(entry, supplement, entry*supplement))
        break
    else:
        seen.add(entry)
