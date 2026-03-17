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

k = TrackedVehicle()
print(k)
