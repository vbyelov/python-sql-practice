import os
#Opening tzop.txt in read mode, returning it as a file object:
stream = open("tzop.txt", "rt", encoding="utf-8")

content = stream.read()

print("=== START ===")
print(content)
print("=== END ===")


with open("tzop.txt", "rt", encoding="utf-8") as stream:
    content = stream.read()

print("length:", len(content))
print("Inhalt:", content)


from os import strerror

try:
    cnt = 0
    s = open('text.txt', "rt")
    ch = s.read(1)
    while ch != '':
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
