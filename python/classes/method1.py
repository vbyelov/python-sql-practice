
class Classy:
    def method(self, par):
        print("method:", par)


obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)

obj2 = Classy()
obj2.method((1,7,7))

class Classy2:
    varia = 2
    def method(self):
        print(self.varia, self.var)


obj = Classy2()
obj.var = 3
obj.method()

class Classy:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()


obj = Classy()
obj.method()

class myclass:
    def __init__(self, arg):
        self.arg = arg

obj1 = myclass("Seven")

print(obj1.arg)

obj1.arg = 12
print(obj1.arg)

print("------")

class Classy:
    def __init__(self, value = 333):
        self.var = value


obj_1 = Classy("Object")
obj_2 = Classy()

print(obj_1.var)
print(obj_2.var)
