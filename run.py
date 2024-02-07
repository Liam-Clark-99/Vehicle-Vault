# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
print("Hello world")

class Car:
    def __init__(self, make, model, year, colour, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        self.mileage = mileage

car1 = Car("Ford", "Focus", 2020, "Blue", 40000)
car2 = Car("Vauxhall", "Astra", 2021, "Silver", 30000)

car_inventory = [car1, car2]
print(car_inventory)