


class Car():
    color = ''
    model = ''
    speed = 0
    brand = ''
    fuel_tank = 0
    number_of_wheels = 0
    engine_size = 0
    mileage = 0
    year = 0
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def current_speed(self):
        message = f"Current speed is {self.speed}"
        print(message)
    
    def navigation(self, direction, second_direction):
        print(f"Turn {direction} and Turn {second_direction}")
    


car = Car('Tesla', 'Model S')

car.engine_size = 396
car.number_of_wheels = 4
car.mileage =  0
car.speed = 200
car.color = 'Wine Red'

print(f"Mary's car model: {car.model} \n")
car.current_speed()
car.navigation(second_direction="Left", direction="right")

# abena_car = Car()
# abena_car.brand = 'Toyotal'
# abena_car.model = 'Camry'
# abena_car.year = 2017

    