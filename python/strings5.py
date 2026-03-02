word = input("Enter a word: ")
text = input("Enter a text: ")

start = 0
for letter in word:
    position = text.find(letter, start)
    if position == -1:
        print("Not found.")
        exit(0)
    else:
        start = position + 1
print("Found")
