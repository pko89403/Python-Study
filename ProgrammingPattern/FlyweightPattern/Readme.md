# Flyweight Pattern
더 가볍게 프로그래밍을 할 수 없을까 해서 만들어진 패턴이다. 공유(Sharing)을 통하여 대량의 객체들을 효과적으로 지원하는 방법        
new 를 통해 객체를 한번만 만들고 필요할 때 마다 사전에 만들어진 객체를 공유하여 제공하는 방법이다.    
다수의 개체의 공통적인 속성을 관리하여 메모리를 아끼는 패턴이다.     
즉, 매우 많은 객체들을 생성해야 할 때 사옹하는 패턴이자, 그 많은 객체를 저장하기에는 메모리가 너무 많이 소모될 때 사용해야하는 패턴

![Flyweight-problem-Diagram](https://media.geeksforgeeks.org/wp-content/uploads/20200204132508/FlyWeight-Class-Diagram.png)
