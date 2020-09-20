"""
    Singleton and Metaclass ( 싱글톤과 메타클래스 ) 
    메타 클래스는 클래스의 클래스다. 클래스는 자신의 메타클래스의 인스턴스 다.
    메타 클래스를 이용하면 이미 정의된 클래스를 통해 새로운 클래스를 생성할 수 있다.
"""

class MetaSingleton(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        
        return cls._instance[cls]

class TestMetaSingleton(metaclass=MetaSingleton):
    pass 

class SecondTestMetaSingleton(metaclass=MetaSingleton):
    pass 

T1 = TestMetaSingleton()
T2 = TestMetaSingleton()

print(T1, T2)

T3 = SecondTestMetaSingleton()
T4 = SecondTestMetaSingleton() 

print(T3, T4)

print(MetaSingleton._instance)