
class Car:
    brand = ''
    model = ''
    year = 0
    speed = 0
    mileage = 0
    
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
    
class ElectricCar(Car):
    battery_capacity = 0
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        

class CEngineCar(Car):
    engine_capacity = 0

electric_car = ElectricCar("Tesla", "Model Y", 2020,2000)
electric_car.battery_capacity = 2000

print(f"CEngine car brand: {electric_car.brand} ")
