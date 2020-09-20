"""
    게으른 초기화(lazy initialization)를 이용한 Singletone 구현
    사용할 수 있는 리소스가 제한적인 상황에서 게으른 초기화를 이용해서 꼭 필요한 시점에 객체를 생성할 수 있다.
"""

class Singletone:
    _instance = None
    def __init__(self):
        if not Singletone._instance:
            print("__init__ method called but nothing is created")
        else:
            print("instance already created : ", self.getInstance())
    
    # 정적 메소드를 지원하는 두가지 방법은 @staticmethod 와 @classmethod 가 있다
    # @classmethod는 cls 가 있는데 이것은 class 를 가리킨다.
    @classmethod
    def get_instance(cls):
        if not cls._instance:
            print("create instance")
            cls._instance = Singletone()
        return cls._instance

if __name__ == "__main__":
    s1 = Singletone()
    s2 = Singletone()
    print(s1._instance)
    print(s2._instance)
    s1.get_instance() 
    print(s1._instance)
    print(s2._instance)