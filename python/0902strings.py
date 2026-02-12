import random
import string
import choice
import time
ALPHABET = string.ascii_letters + string.digits + string.punctuation

print(ALPHABET)

def random_string(length):
    random_string = ''
    for i in range(length):
        random_string += random.choice(ALPHABET)
    return random_string

while True:
    rand_choice = random.choice(range(10,20))
    rand_string = random_string(rand_choice)
    print(rand_choice, ' letters->', rand_string)
    time.sleep(0.1)



