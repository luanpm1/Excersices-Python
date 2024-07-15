# object car
class Car:
    num_wheels = 4

    def __init__(self, color, style, speed):
        self.color = color
        self.style = style
        self.speed = speed

    def changed_color(self, color):
        self.color = color

    def changed_styleI(self, style):
        self.style = style

    def changed_speed(self, maxSpeed):
        self.speed = 45
        self.maxSpeed = maxSpeed


class FuelCar(Car):
    def __init__(self, color, style, speed, fuel_type):
        super().__init__(color, style, speed)
        self.fuel_type = fuel_type

    def changed_fuel_type(self, fuel_type):
        self.fuel_type = fuel_type


class ElectricCar(Car):
    def __init__(self, color, style, speed, electric_type):
        super().__init__(color, style, speed, electric_type)
        self.electric_type = electric_type

    def changed_electric_type(self, electric_type):
        self.electric_type = electric_type


myCar = Car("while", "sedan", 30)
newCar = FuelCar("red", "sedan", 50, "oil")
print(newCar.color, newCar.style, newCar.speed, newCar.fuel_type)
myCar.changed_color("black")
# myCar.changed_speed(200)
# print("My car is {}, it is {}, with speed {},and max speed {} km/h".format(myCar.style, myCar.color, myCar.speed,
#                                                                            myCar.maxSpeed))
# print(myCar.style, myCar.color, myCar.speed, myCar.maxSpeed)

# myCar.changed_speed()
# print(myCar.speed)

# object Animal
class Dog():
    def speak(self):
        print("Quack")

