class vehicle:

    def __init__(self, name, maxspeed, mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage

class bus(vehicle):
    pass

schoolbus = bus("volvo", 150, 20)
print("School bus brand:", schoolbus.name)
print("Max speed this bus can go:", schoolbus.maxspeed)
print("Mileage of this bus:", schoolbus.mileage)