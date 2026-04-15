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