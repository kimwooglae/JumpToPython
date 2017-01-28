
f = open("1.file.txt", "r")
while True:
    str = f.readline()
    if not str:
        break
    print("[" + str + "]")
