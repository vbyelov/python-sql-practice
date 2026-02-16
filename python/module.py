
counter = 0

print("Inside a module!")
print('-----------------')
print(__name__)

if __name__ == '__main__':
    print("This is Main Script")
elif __name__ == 'module':
    print("Inside a module!")
else:
    print("Inside a function!")