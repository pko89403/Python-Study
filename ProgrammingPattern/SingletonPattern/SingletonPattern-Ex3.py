"""
    Monostate Singleton ( 모노스테이트 싱글톤 )
    하나의 객체만 존재해야 한다는 것에 너무 신경쓰지 않고 여러 객체 생성을 허용하더라도 해야한다.
    모노스테이트 싱글톤은 모든 객체가 같은 상태를 공유하는 패턴이다
"""

class MonostateSingleton:
    # __dict__ 에 객체의 상태를 저장하는데
    # __dict__ 를 __shared_state로 지정해서 객체는 2개가 생기지만, 각각의 __dict__는 같다.
    # 모든 객체가 상태를 공유하는 상태가 된다.
    __shared_state = {'a': 'b'}
    def __init__(self):
        self.__dict__ = self.__shared_state

if __name__ == "__main__":
    m1 = MonostateSingleton()
    m2 = MonostateSingleton() 

    print(m1, m2)

    print(m1.__dict__, m2.__dict__) 

    m1.a = 1

    print(m1.__dict__, m2.__dict__) 

    m1.x = 2 

    print(m1.__dict__, m2.__dict__) 
