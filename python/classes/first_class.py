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
        self.__stack_list = []
        print("Hi!")


stack_object = Stack()

print(len(stack_object.__stack_list))
