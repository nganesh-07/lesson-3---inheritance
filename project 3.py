class vehicle:
    def __init__(self, name, mileage, fare):
        self.name = name
        self.mileage = mileage
        self.fare = fare

class bus(vehicle):
    pass

busfare = bus("honda", 15, 10)
print("This bus is a", busfare.name, "and it's mileage is around", busfare.mileage, "leading to the fare being $", busfare.fare)