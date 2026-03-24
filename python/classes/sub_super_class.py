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



#     def __init__(self, name):
#         super().__init__(name)
#
#
# obj = Sub("Andy")
#
# print(obj)

#
# class Vehicle:
#     pass
#
#
# class LandVehicle(Vehicle):
#     pass
#
#
# class TrackedVehicle(LandVehicle):
#     pass
#
#
# my_vehicle = Vehicle()
# my_land_vehicle = LandVehicle()
# my_tracked_vehicle = TrackedVehicle()
#
# for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
#     for cls in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(isinstance(obj, cls), end="\t")
#     print()
#
# print('_________')
#
# list1 = [1, 2, 3]
# list2 = list1
# print(list1 is list2)


# Testing properties: class variables.
class Super:
    supVar = 1


class Sub(Super):
    subVar = 2


obj = Sub()

print(obj.subVar)
print(obj.supVar)

class Super:
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    def __init__(self):
        super().__init__()



obj = Sub()

print(obj.subVar)
print(obj.supVar)
