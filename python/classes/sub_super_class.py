class Vehicle:
    print('Vehicle class created')
    print
    def __str__(self):
        return 'Vehicle class printed'


class LandVehicle(Vehicle):
    print('LandVehicle class created')
    print

    def __str__(self):
        return 'LandVehicle class printed'


class TrackedVehicle(LandVehicle):
    print('TrackedVehicle class created')
    print
    def __str__(self):
        return 'TrackedVehicle class printed'

x = k = Vehicle()

print(k)

print(issubclass(TrackedVehicle, LandVehicle))
print(issubclass(TrackedVehicle, Vehicle))
print(issubclass(TrackedVehicle, LandVehicle))

print(issubclass(Vehicle, TrackedVehicle))

print(issubclass(LandVehicle, LandVehicle))

print(isinstance(k, TrackedVehicle))

print(Vehicle is Vehicle)

print('Next class')

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)


obj = Sub("Andy")
obj2 = Super("Bob")

print(obj, obj2)
print(obj.__str__())
print(obj2.__str__())
