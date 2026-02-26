def mysplit(strng):
    strng=strng.split()
    finallist = []
    for words in strng:
        words = words.strip()
        finallist.append(words)
    return finallist


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
