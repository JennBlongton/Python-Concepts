class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    def __init__(self):
        super().__init__()

v1 = Bus('Bus',250,15)
print(
    "vehicle Name:", v1.name,
    "Vehicle Speed:", v1.max_speed,
    "vehicle Mileage:", v1.mileage
)