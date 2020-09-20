from abc import * # Abstract Class
from abc import abstractmethod, ABC

"""
    로봇을 조립하는 코드를 만든다고 생각
    로봇 조립에 필요한 각 부품 들에 대한 클래스를 선언한다
"""
class RobotPart(ABC):
    @abstractmethod
    def assemble(self):
        pass 

class HeadPart(RobotPart):
    def assemble(self):
        print("assemble head part")

class WingPart(RobotPart):
    def assemble(self):
        print("assemble wing part")

class LegPart(RobotPart):
    def assemble(self):
        print("assemble leg part")

class BodyPart(RobotPart):
    def assemble(self):
        print("assemble body part")

class ArmPart(RobotPart):
    def assemble(self):
        print("assemble arm part")
"""
    각 로봇들에 대해 클래스를 선언한다
    add_part 로 로봇 별로 필요한 부품을 추가한다
"""
class Robot(ABC):
    def __init__(self):
        self.parts = []
        self.create_robot()

    @abstractmethod
    def create_robot(self):
        pass 

    def add_part(self, part):
        self.parts.append(part)

    def assemble_parts(self):
        for part in self.parts:
            part.assemble()

class DogRobot(Robot):
    def create_robot(self):
        self.add_part(HeadPart())
        self.add_part(BodyPart())
        self.add_part(ArmPart())
        self.add_part(LegPart())

class BirdRobot(Robot):
    def create_robot(self):
        self.add_part(HeadPart())
        self.add_part(BodyPart())
        self.add_part(WingPart())
        self.add_part(LegPart())

"""
    선언한 로봇 클래스의 "assemble_parts" 함수를 이용해 로봇을 조립한다
"""
if __name__ == "__main__":
    dog_robot = DogRobot()
    dog_robot.assemble_parts()

    BirdRobot().assemble_parts()
