import re

abba = re.compile(r"([a-z])([a-z])\2\1")
aaaa = re.compile(r"([a-z])\1\1\1")
aba = re.compile(r"([a-z])([a-z])\1")
aaa = re.compile(r"([a-z])\1\1")

class IP:
    def __init__(self, desc):
        self.desc = desc
        self.inside = []
        self.outside = []
        for i in desc.split("["):
            if "]" not in i:
                self.outside.append(i)
            else:
                tokens = i.split("]")
                self.inside.append(tokens[0])
                self.outside.append(tokens[1])

    def ssl(self):
        for i in self.outside:
            group = aba.search(i)
            while group:
                if group.group(1) != group.group(2):
                    bab = re.compile(group.group(2) + group.group(1) + group.group(2))
                    for j in self.inside:
                        if bab.search(j):
                            return True
                group = aba.search(i, group.start(2))
        return False
    
    def abba(self, value):
        group = abba.search(value)
        while group:
            if not aaaa.match(group.group(0)):
                return True
            else:
                group = abba.search(value, group.end(0))

    def tls(self):
        for i in self.inside:
            if self.abba(i):
                #print("inside match " + i)
                return False
            else:
                pass
                #print("inside no match " + i)
        for i in self.outside:
            if self.abba(i):
                #print("outside match " + i)
                return True
            else:
                pass
                #print("outside no match " + i)
        return False

    def __str__(self):
        return str(self.__dict__)


#desc = "ioxxoj[asdfgh]zxcvbn"
#ip = IP(desc)
#print(ip)
#print(ip.tls())

#desc = "aba[bab]xyz"
#desc = "xyx[xyx]xyx"
#desc = "aaa[kek]eke"
desc = "zazbz[bzb]cdb"
ip = IP(desc)
print(ip)
print(ip.ssl())

tlsCount = 0
count = 0
#if False:
for line in open("07a.txt"):
    ip = IP(line.strip())
    count += 1
    print(count)
    if ip.ssl():
        tlsCount += 1

print(str(tlsCount) + "/" + str(count))
