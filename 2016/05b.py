import hashlib

root = "wtnhxymk"
index = 0
password = ["X" for x in range(8)]
while "X" in password:
    m = hashlib.md5()
    m.update((root + str(index)).encode('utf-8'))
    hexdigest = m.hexdigest()
    if hexdigest[0:5] == "00000":
        print(index)
        print(hexdigest)
        if hexdigest[5].isdigit() and int(hexdigest[5]) < len(password) and password[int(hexdigest[5])] == "X":
            password[int(hexdigest[5])] = hexdigest[6]
            print(password)
    index += 1
print(password)
