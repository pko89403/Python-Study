from abc import ABCMeta, abstractmethod

class Pizzastore(metaclass=ABCMeta):
    def orderPizza(self, type):
        pizza = self.createPizza(type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza 

    @abstractmethod
    def createPizza(self, type):
        pass 


class ChicagoPizzaStore(Pizzastore):
    def createPizza(self, type):
        pizza = None 

        if type == 'CHEESE':
            pizza = ChicagoCheesePizza()
        elif type == 'PEPPERONI':
            pizza = ChicagoPepperoniPizza()
        else:
            pizza = ChicagoPizza()

        return pizza 

class NYPizzaStore(Pizzastore):
    def createPizza(self, type):
        pizza = None 

        if type == 'CHEESE':
            pizza = NYCheesePizza()
        elif type == 'PEPPERONI':
            pizza = NYPepperoniPizza()
        else:
            pizza = NYPizza()

        return pizza 


class Pizza(metaclass=ABCMeta):
    def prepare(self):
        print('Prepare {}'.format(self.name))
        print('Dough {}'.format(self.dough))
        print('Sauce {}'.format(self.sauce))
    
    def bake(self):
        print('Bake {}'.format(self.name))
    
    def cut(self):
        print('Cut {}'.format(self.name))
    
    def box(self):
        print('Boxing {}'.format(self.name))

class ChicagoPizza(Pizza):
    def __init__(self):
        self.name = 'Chicago Pizza'
        self.dough = 'None'
        self.sauce = 'None'

class ChicagoCheesePizza(Pizza):
    def __init__(self):
        self.name = 'Chicago Cheese Pizza'
        self.dough = 'Chicago Cheese'
        self.sauce = 'Chicago sauce'

class ChicagoPepperoniPizza(Pizza):
    def __init__(self):
        self.name = 'Chicago Pepperoni Pizza'
        self.dough = 'Chicago Pepperoni'
        self.sauce = 'Chicago sauce'

class NYPizza(Pizza):
    def __init__(self):
        self.name = 'NY Pizza'
        self.dough = 'None'
        self.sauce = 'None'

class NYCheesePizza(Pizza):
    def __init__(self):
        self.name = 'NY Cheese Pizza'
        self.dough = 'NY Cheese'
        self.sauce = 'NY sauce'

class NYPepperoniPizza(Pizza):
    def __init__(self):
        self.name = 'NY Pepperoni Pizza'
        self.dough = 'NY Pepperoni'
        self.sauce = 'NY sauce'

if __name__ == "__main__":
    chicagoStore = ChicagoPizzaStore()
    nyStore = NYPizzaStore()

    nyStore.orderPizza('CHEESE')
    print('######################')
    chicagoStore.orderPizza('PEPPERONI')
    print('######################')
    chicagoStore.orderPizza('CHEESE')