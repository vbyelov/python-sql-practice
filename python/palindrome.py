# Palindrome checker (slice approach)

text = input("Enter text: ")


if text == "":
    print("Not a palindrome")
else:
    normalized = text.replace(" ", "").upper()

    if normalized == normalized[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")