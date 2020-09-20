"""
    python의 __new__ 함수를 이용하면 쉽게 구현할 수 있다
    객체가 아닌 클래스 내부에 instance가 존재하면 생성된 instance를 반환하고 없다면 새로운 객체를 생성해서 instance에 담고 반환한다.
    __new__ 는 새로운 인스턴스를 만들 때, 제일 처음으로 실행되는 메소드이다. __new__ 함수는 return을 하지 않으면 객체를 반환하지 않기 때문에 꼭 return을 해야한다.
"""


class Singletone:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            print("Create an instance")
            cls.instance = super(Singletone, cls).__new__(cls)
        return cls.instance 

if __name__ == "__main__":
    s1 = Singletone()
    s2 = Singletone() 

    print(s1)
    print(s2)