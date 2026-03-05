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
    def push(self, val):
        self.__stack_list.append(val)
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
    def show(self):
        print(self.__stack_list)
        return self.__stack_list[::-1]


stack_object = Stack()

for i in range(4,400,25):
    stack_object.push(i)

print(stack_object.show())

