from abc import ABC, abstractmethod


"""
    각 로봇을 만드는 기계가 있다고 생각한다.
    각각의 가계에선 개 로봇과 새 로봇을 만든다.
"""

class RobotFactory(ABC):
    @abstractmethod
    def create_dog_robot(self):
        pass 

    @abstractmethod
    def create_bird_robot(self):
        pass 

class ARobotFactory(RobotFactory):
    def create_dog_robot(self):
        return BigDog()
    
    def create_bird_robot(self):
        return SlowBird()

class BRobotFactory(RobotFactory):
    def create_dog_robot(self):
        return SmallDog()
    
    def create_bird_robot(self):
        return FastBird() 

"""
    개 로봇은 짖기 기능, 새 로봇은 날기 기능이 있다
"""

class Dog(ABC):
    @abstractmethod
    def bark(self):
        pass 

class BigDog(Dog):
    def bark(self):
        print("Growl")

class SmallDog(Dog):
    def bark(self):
        print("BowBow")

class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass 

class FastBird(Bird):
    def fly(self):
        print("Fly High")

class SlowBird(Bird):
    def fly(self):
        print("Fly Low")


if __name__ == "__main__":
    for factory in [ARobotFactory(), BRobotFactory()]:
        dog = factory.create_dog_robot()
        bird = factory.create_bird_robot()
        dog.bark()
        bird.fly()