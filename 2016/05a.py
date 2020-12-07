import hashlib

root = "wtnhxymk"
index = 0
password = ""
while len(password) < 8:
    m = hashlib.md5()
    m.update((root + str(index)).encode('utf-8'))
    hexdigest = m.hexdigest()
    if hexdigest[0:5] == "00000":
        print(index)
        print(hexdigest)
        password += hexdigest[5]
        print(password)
    index += 1
print(password)
