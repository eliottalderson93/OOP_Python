class MathDojo:
    def __init__(self):
      self.sum = 0.0
    def add(self,*mod):
        array = []
        #k=0
        #print(mod)
        for num in mod:
            array.append(num)
        #print(array)
        for num in array:
          self.sum += num
        print(self.sum)
        return self
    def subtract(self,*mod):
        array = []
        #k=0
        #print(mod)
        for num in mod:
            array.append(num)
        #print(array)
        for num in array:
          self.sum -= num
        print(self.sum)
        return self
class Penetrate(MathDojo):
    def __init__(self):
        super().__init__()
    def into_add(self,*arrs):
        array = []
        for arr in arrs:
            if (type(arr)!=type([1])):
                array.append(arr)
            array += arr
            self.add(array)
        return self
    def into_sub(self,*arrs):
        array = []
        for arr in arrs:
            if (type(arr)!=type([1])):
                array.append(arr)
            array += arr
            self.subtract(array)
        return self
                
md = MathDojo().add(5,4,3).add(4).subtract(4,5)
md = Penetrate().into_add([5,4,1],[3,2,6]).into_sub(4,[5,6])

 # if type(arr) == type([1]):
            #     if plus == True:
            #         self.add(arr)
            #     else:
            #         self.subtract(arr)
            # else:
            #     if plus == True:
            #         self.sum += float(arr)
            #     else:
            #         self.sum -= float(arr)