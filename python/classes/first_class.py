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
    def get_stack(self):
        return self.__stack_list
    def __iter__(self):
        return iter(self.__stack_list)




stack_object = Stack()

for i in range(4,400,25):
    stack_object.push(i)

print(stack_object.show())


st1 = Stack()
st2 = Stack()

for i in range(3,333,3):
    st1.push(i)

for x in st1:
    st2.push(x / 2)

for a,b in zip(st1,st2):
    print(a,'--',b)


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val
    def get_sum(self):
        return self.__sum

stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())