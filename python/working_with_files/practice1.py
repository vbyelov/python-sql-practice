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
import sys

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

sorted_items = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

"""
Task: Letter Frequency Histogram — Part 2 (Improvement)

Description:
Improve the previous program to make the output more useful and structured.

Requirements:

1. Sort the histogram by frequency (descending order):
   - letters with higher counts should appear first

2. Use lambda inside sorted():
   - sort by dictionary values (counts), not keys

3. Save the result to a new file:
   - the new file name should be the same as the input file
   - add the suffix ".hist" to the original name

4. Write the histogram to the file in the format:
   letter -> count

Example:

Input file content:
cBabAa

Output file (samplefile.txt.hist):

a -> 3
b -> 2
c -> 1

Notes:
- Use dictionary.items() to get (letter, count) pairs
- Use lambda x: x[1] to sort by frequency
- Use reverse=True for descending order
- Use with open(..., "w") to write to file
"""

try:
    with open(source_filename + '.hist', 'w') as dest_file:
        for letter, count in sorted_items:
            dest_file.write(f"{letter} -> {count}\n")
except OSError:
    print("Can not save file")
    sys.exit()
