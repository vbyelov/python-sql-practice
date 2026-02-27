# Caesar cipher (improved)

text = input("Enter your message: ")

# --- shift validation ---
while True:
    try:
        shift = int(input("Enter shift (1-25): "))
        if 1 <= shift <= 25:
            break
        else:
            print("Shift must be between 1 and 25.")
    except ValueError:
        print("Please enter a valid integer.")

cipher = ""

for char in text:
    if char.isalpha():
        if char.isupper():
            base = ord('A')
        else:
            base = ord('a')

        new_code = base + (ord(char) - base + shift) % 26
        cipher += chr(new_code)
    else:
        cipher += char

print("Encoded text:", cipher)