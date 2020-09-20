class BigString:
    def __init__(self):
        self.orders = orders 
    
    def getText(self):
        for order in self.orders:
            factory = BigFactory()
            big_char = factory.making(order)
            self.result_print(big_char)
    
    def result_print(self, big_char):
        print(big_char)

class BigFactory:
    _singletone = None 

    def __init__(self):
        self.array = {} 
    
    def __new__(cls, *args, **kwargs):
        if not cls._singletone:
            cls._singletone = super(BigFactory, cls).__new__(cls, *args, **kwargs)

            return cls._singletone
    
    def making(self, number):
        if number not in self.array.keys():
            self.array[number] = BigChar(number)
        return self.array[number].getBigChar()

class BigChar:
    def __init__(self):
        self.txt = ""
        with open("big" + number + ".txt", 'r') as fp:
            lines = fp.read()
            for line in lines:
                self.txt += line 
    
    def getBigChar(self):
        return self.txt

if __name__ == "__main__":
    numbers = str(input())
    BigString(numbers).getText()