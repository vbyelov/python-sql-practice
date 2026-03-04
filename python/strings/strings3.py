def mysplit(strng):
    strng=strng.split()
    finallist = []
    for words in strng:
        words = words.strip()
        finallist.append(words)
        # if words == "that" : return None

    return finallist


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
