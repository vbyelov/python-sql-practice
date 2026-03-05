class TheSimplestClass:
    pass

my_1st_object = TheSimplestClass()

stack = []


def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val


push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())

class Stack:  # Defining the Stack class.
    def __init__(self):  # Defining the constructor function.
        print("Hi!")


stack_object = Stack()

class Stack2:
    def __init__(self): print("Hi2!")

stackobj2 = Stack2()