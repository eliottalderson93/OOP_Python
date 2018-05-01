class Bike:
    def __init__(self,o_price=0,max_speed=0,miles=0):
        self.price = o_price
        self.max_speed = max_speed
        self.miles = miles
    def displayinfo(self):
        print(self.price)
        print(self.max_speed)
        print(self.miles)
        return self
    def ride(self):
        self.miles += 10
        print("Yeehaw")
        return self
    def reverse(self):
        self.miles -= 5
        print("Too far!")
        return self
modelOne=Bike(0,0,0)
modelOne.ride().ride().ride().reverse().displayinfo()
modelTwo = Bike(10,0,0)
modelTwo.ride().ride().reverse().reverse().displayinfo()
modelThree = Bike(20,0,0)
modelThree.reverse().reverse().reverse().displayinfo()

