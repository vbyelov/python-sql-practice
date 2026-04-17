"""

Task: Letter Frequency Histogram
Description:
The program reads a text file and counts how often each Latin letter appears.
Requirements:

1. Ask the user to enter the file name.

2. Read the file content.

3. Count only Latin letters (a-z), ignoring case (A == a).

4. Store counts using a dictionary:
   - keys → letters
   - values → number of occurrences

5. Print a histogram in alphabetical order.
6. Show only letters that appear at least once.
"""


source_filename = input("Enter file name: ")
try:
    with open(source_filename) as src_file:
        content = src_file.read()
except OSError:
    print("Can not open file")
    sys.exit()

dictionary = {}

for char in content:
    if char.lower() in "abcdefghijklmnopqrstuvwxyz":
        dictionary[char.lower()] = dictionary.get(char.lower(), 0) + 1

for letter in sorted(dictionary):
        print(letter,'-->', dictionary[letter])