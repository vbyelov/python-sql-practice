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


class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()
