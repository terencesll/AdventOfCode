
file = open("01.txt")
seen = set()
requiredSumEntry = 2020
for line in file:
    entry = int(line)
    for seenEntry in seen:
        supplement = requiredSumEntry - entry - seenEntry
        if supplement in seen:
            print("{} {} {} {}".format(entry, seenEntry, supplement, entry*seenEntry*supplement))
            break
    seen.add(entry)
