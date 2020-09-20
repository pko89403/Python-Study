# Singleton Pattern
class가 단 한 개의 instance 만 가지도록 제한하는 패턴    
주로 logging 이나 DB 작업 등 에서 한 개의 객체만 허용하여 동일한 리소스에 대해 동시 요청으로 인한 충돌을 막을 때 사용된다.     
오로지 하나의 인스턴스만 유지하기 위해 생성자에 접근 제한을 두고, 유일한 단일 객체를 반환하기 위해 정적 메소드를 사용한다. 또한, 유일한 단일 객체 역시 정적 참조 변수가 필요하다.      

- 클래스에 대한 단일 객체 생성
- 전역 객체 제공
- 공유된 리소스에 대한 동시 접근 제어

### Monostate Singleton 은 borg pattern(Alex Martelli)과 같다.
보그 패턴은 여러 개의 인스턴스에서 하나의 상태(state)를 공유 한다는게 차이점이다.    
하나의 인스턴스를 공유하는게 아니고 하나의 상태(state)를 공유 하는 것이다.

### Singletone and metaclass    

## 싱글톤 패턴의 단점

- 전역 변수의 값이 실수로 변경된 것을 모르고 사용될 수 있다
- 한 개의 객체만을 만들기 때문에 같은 객체에 대한 여러개의 참조자가 생긴다
- 전역 변수에 종속적인 모든 클래스 간 상호관계가 복잡해 질 수 가 있다. 따라서 전역 변수의 수정이 의도치 않게 다른 클래스에도 영향을 줄 수 있다.

![singleton-class-diagram](https://media.geeksforgeeks.org/wp-content/uploads/20200122161234/singleton-class-diagram.png)