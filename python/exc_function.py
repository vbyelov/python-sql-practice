def read_int(prompt, min, max):
    while True:

        try:
            value = int(input(prompt))
            if value < min or value > max:
                print (f"Error: the value is not within permitted range ({min}..{max})")
            else:
                return value
        except ValueError:
            print("Please enter a number.")




v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
