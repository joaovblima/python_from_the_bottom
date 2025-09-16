class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def drive(self):
        print("The car is driving")


car1 = Car("Volkswagen", "1992")
car1.drive()