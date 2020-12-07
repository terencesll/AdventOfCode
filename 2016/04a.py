class Room:
    def __init__(self, desc):
        self.desc = desc
        desc = desc.rstrip("]")
        tokens = desc.split("[")
        self.checksum = tokens[1]
        tokens = tokens[0].rsplit("-", 1)
        self.sector = int(tokens[1])
        self.name = ""
        for i in tokens[0].split("-"):
            self.name += i
        charCount = {}
        for i in self.name:
            if i not in charCount:
                charCount[i] = 0
            charCount[i] += 1
        self.checkSumFull = ""
        charByCount = {}
        for key, value in charCount.items():
            if value not in charByCount:
                charByCount[value] = ""
            charByCount[value] += key
        for key, value in sorted(charByCount.items(), reverse=True):
            self.checkSumFull += "".join(sorted(value))
        self.checkSumGen = self.checkSumFull[0:5]

    def real(self):
        return self.checkSumGen == self.checksum

    def realName(self):
        ordinals = [ord(x)-ord('a') for x in self.name]
        realname = ""
        for x in ordinals:
            decrypted = (x + self.sector) % 26
            realname += chr(decrypted + ord('a'))
        return realname

sumSectorId = 0
for line in open("04a.txt"):
    room = Room(line.rstrip("\n"))
    if room.real():
        sumSectorId += room.sector
        if room.sector == 482:
            print(room.realName())
            print(room.desc)
print(sumSectorId)
