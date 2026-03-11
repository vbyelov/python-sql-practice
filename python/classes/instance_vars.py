# class ExampleClass:
#     def __init__(self, val = 1):
#         self.first = val
#
#     def set_second(self, val):
#         self.second = val
#
#
# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
#
# example_object_2.set_second(3)
#
# example_object_3 = ExampleClass(4)
# example_object_3.third = {'ABC': 'ERD'}
#
# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)
#
# for key, value in example_object_3.__dict__.items():
#     print(key, '--' ,value)
#
#
# class ExampleClass:
#     def __init__(self, val = 1):
#         self.__first = val
#
#     def set_second(self, val = 2):
#         self.__second = val
#
#
# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
#
# example_object_2.set_second(3)
#
# example_object_3 = ExampleClass(4)
# example_object_3.__third = 5
#
#
# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)

class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)
example_object_4 = ExampleClass(5)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)


# class ExampleClass:
#     varia = 1
#     def __init__(self, val):
#         ExampleClass.varia = val
#
#
# print(ExampleClass.__dict__)
# example_object = ExampleClass(2)
#
# print(ExampleClass.__dict__)
# print(example_object.__dict__)

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
print(example_object.a)

if hasattr(example_object, 'b'):    print(example_object.b)

