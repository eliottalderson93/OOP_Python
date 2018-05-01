import random
class Car:
    def __init__(self,o_price=2000,speed=35,fuel=0,mileage=25,tax = 0.12):
        self.price = o_price
        self.speed = str(speed)+'mph'
        self.fuel = random.random()
        self.mileage = str(mileage)+'mpg'
        self.tax = tax
        if self.price >10000:
            self.tax = 0.15
        else:
            pass#nothing
        if self.fuel< 0.25:
            self.fuel = 'empty'
        elif self.fuel >=0.25 and fuel<0.5:
            self.fuel = 'not full'
        elif self.fuel >=0.5 and fuel <0.75:
            self.fuel = 'kind of full'
        else:
            self.fuel = 'full'
    def printAll(self):
        print(self.__dict__)
#thisObj.__dict__ #returns all values in a dict
Ford = Car(mileage=35).printAll()
print('\n')
Toyota = Car(speed=5,mileage=105).printAll()
print('\n')
Geo = Car(speed=15,mileage=95).printAll()
print('\n')
Motorola = Car(speed=25).printAll()
print('\n')
Model5 = Car(speed=45).printAll()
print('\n')
Model6 = Car(o_price=2000000,mileage=15).printAll()
print('\n')
