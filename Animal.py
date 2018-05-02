class Animal:
    def __init__(self,name='animal',health=150):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print('current health is: '+str(self.health))
        return ('current health is: '+str(self.health))
    def printAll(self):
        print(self.__dict__)
        print('\n')
        return self
Animal().walk().walk().walk().run().run().display_health()
class Dog(Animal):
    def __init__(self,name='dog'):
        super().__init__()
        self.name = name
    def pet(self):
        self.health +=5
        return self
Dog().walk().walk().walk().run().run().pet().display_health()
class Dragon(Animal):
    def __init__(self, name='dragon',health=170):
        super().__init__()
        self.name = name
        self.health = health
    def fly(self):
        self.health -=10
        return self
    def display_health_dragon(self):
        str1 = self.display_health() + ' ROAAAARRRRR'
        print(str1)
        return self
Dragon().fly().walk().display_health_dragon()