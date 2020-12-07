file = open("10.txt")
#circList = list(range(256))
lengths = list(map(ord, file.readline()))
lengths.extend([17, 31, 73, 47, 23])
print(lengths)

def knotHashRound(circList, curr, skip, lengths):
    circListLength = len(circList)
    for length in lengths:
        #print("skip:%d, length:%d" % (skip, length))
        sublistEnd = curr + length
        if sublistEnd < circListLength:
            subList = circList[curr:sublistEnd]
            subList.reverse()
            circList[curr:sublistEnd] = subList
        else:
            subList = circList[curr:]
            subList.extend(circList[:sublistEnd%circListLength])
            subList.reverse()
            circList[curr:] = subList[:circListLength-curr]
            circList[:sublistEnd%circListLength] = subList[circListLength-curr:]
        curr += skip + length
        curr %= circListLength
        skip += 1
        #print(curr)
        #print(circList)
    return circList, curr, skip

def knotHash(circList):
    curr = 0
    skip = 0
    for i in range(64):
        circList, curr, skip = knotHashRound(circList, curr, skip, lengths)

    denseHash = list(range(16))
    for i in range(16):
        denseHash[i] = circList[i*16]
        for j in range(15):
            denseHash[i] ^= circList[i*16+j+1]

    hexDenseHash = ""
    for i in denseHash:
        hexDenseHash += "%02x" % i
    return hexDenseHash

def knotHashString(plaintext):
    return knotHash(list(map(ord, plaintext)))

print(knotHash(list(range(256))))
print(knotHashString("AoC 2017"))

key = 'flqrgnkx'

for row in range(128):
    plaintext = key + "-" + str(row)
    print("%s: %s" % (plaintext, knotHashString(plaintext)))
