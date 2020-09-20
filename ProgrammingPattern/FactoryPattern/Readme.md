# Factory Pattern
Factory - 다른 클래스의 객체를 생성하는 클래스를 말한다.   
팩토리는 객체 관련 메소드로 구성되어 클라이언트는 특정 인자와 함께 메소드를 호출하고 팩토리는 해당 객체를 생성하여 반환한다.
## 팩토리가 필요한 이유
- 객체 생성과 클래스 구현을 분리해 상호 의존도를 줄인다
- 객체를 생성할 때 필요한 인터페이스와 메소드, 인자 등의 정보만 알면 되기 때문에 클라이언트의 일이 줄어든다
- 코드를 수정하지 않고 간단하게 팩토리에 클래스를 추가 할 수 있다
- 이미 생성된 객체를 팩토리가 재활용할 수 있으며 클라이언트가 직접 객체를 생성할 경우 매번 새로운 객체가 생성된다
> 두가지 패턴이 존재한다.
> 1. Factory method : input에 따라 객체 생성이 달라지는 방식
> 2. Abstract factory : 여러 객체 생성을 연관된 그룹 별로 묶어서 객체를 생성하는 방식

## 1. Factory
- 객체 생성을 한 군데로 모아서 객체 추적을 더 쉽게 만듬
- 인스턴스 화가 아닌 상속으로 객체를 생성한다.
- 유동적인 디자인으로 특정 객체가 아닌 인스턴스나 서브 클래스 객체를 반환
- 인터페이스를 통해 객체를 생성하지만 팩토리가 아닌 서브 클래스가 해당 객체 생성을 위해 어떤 클래스를 호출 할지 결정한다.
### 장점
- 유연성과 포괄성을 갖추며 한 클래스에 종속되지 않는다.
- 객체를 생성하는 코드와 활용하는 코드를 분리하여 의존성을 줄인다.
- 새로운 클래스 추가 등의 유지보수가 쉽다.

## 2. Abstract Factory  
- 클래스를 직접 호출하지 않고 관련 객체를 생성하는 인터페이스를 제공한다.
- 팩토리 메소드는 인스턴스 생성을 서브 클래스에 맡기는 반면 추상 팩토리는 관련된 객체의 집합을 생성한다.
- 클라이언트는 객체 생성 로직과 상관없이 생성된 객체를 사용하며, 오직 인터페이스를 통해 객체에 접근할 수 있다.
### 장점
- 추상 팩토리 패턴은 확장에 매우 용의한 패턴이다.
- 추상 팩토리 패턴은 기존 팩토리 패턴의 if-else 로직에서 벗어날 수 있게 해준다.
- 구체적인 클래스는 분리 되어있다