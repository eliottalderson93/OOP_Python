class Product:
    def __init__(self,price=100,item_name='default',weight=0,brand='default',status=True,ret_reason=False):
        self.price = price
        self.item_name = item_name
        #self.weight = weight
        #self.brand = brand
        self.status = status #True is for sale
        #self.ret_reason = ret_reason
        # if self.status == True:
        #     self.status = 'for sale'
        # else:
        #     self.status = 'sold'
    ##################################################
    def printAll(self):
        print(self.__dict__)
        print('\n')
        return self
    
##################################################
    def buy_sell(self):
        if(type(self.status) == type(True)):
            self.status = not self.status
            if self.status == False:
                print('sold')
                self.price = str(self.price)
            elif self.status == True:
                print('for sale')
        else:
            print(self.status)
            pass
        return self
##################################################
    def increase_price(self,percent):
        if (type(self.price) != type('str')):
            self.price = float(self.price)*(1.0+float(percent))
        return self
##################################################
    def on_sale(self,percent):
        if (type(self.price) != type('str')):
            self.price = float(self.price)*(1.0-float(percent))
        return self
    def display(self):
        return self.printAll()
p1 = Product("iphone", 500.25)
p2 = Product("radio", 20.99)
p3 = Product("laptop", 1599.99)
p1.increase_price(15.0).on_sale(25.3).display()
p2.on_sale(30.0).increase_price(40.2).display()
p3.display().increase_price(30.0).buy_sell().display()
#############################################################
    # def return1(self,defective):
    #     if defective == True:
    #         self.ret_reason = 'defective'
    #         self.price = 0
    #         self.status = False
    #     else:
    #         self.status = 'for sale'
    #         self.status = True
    #         self.price = self.price*0.80
    #     return self
# prod1 = Product().tax(0.15).printAll()
# prod2 = Product().buy_sell().printAll()
# prod3 = Product(status=False).buy_sell().printAll()
# prod4 = Product().buy_sell().return1(defective=prod4.ret_reason).printAll()
# prod5 =  Product().buy_sell().return1(defective=False).printAll()
