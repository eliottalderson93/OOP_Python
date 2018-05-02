class Product:
    def __init__(self,price=100,item_name='default',weight=0,brand='default',status=True,ret_reason=False):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status
        self.ret_reason = ret_reason
        if self.status == True:
            self.status = 'for sale'
        else:
            self.status = 'sold'
    ##################################################
    def printAll(self):
        print(self.__dict__)
        print('\n')
        return self
    #################################################
    def buy_sell(self):
        if(type(self.status) == type(True)):
            self.status = not self.status
            if self.status == False:
                self.status = 'sold'
            elif self.status == True:
                self.status = 'for sale'
        else:
            print(self.status)
            pass
        return self
    #################################################
    def tax(self,percent):
        self.price = float(self.price)*(1.0+float(percent))
        return self
    #################################################
    def return1(self,defective):
        if defective == True:
            self.ret_reason = 'defective'
            self.price = 0
            self.status = False
        else:
            self.status = 'for sale'
            self.status = True
            self.price = self.price*0.80
        return self
prod1 = Product().tax(0.15).printAll()
prod2 = Product().buy_sell().printAll()
prod3 = Product(status=False).buy_sell().printAll()
prod4 = Product().buy_sell().return1(defective=prod4.ret_reason).printAll()
prod5 =  Product().buy_sell().return1(defective=False).printAll()
