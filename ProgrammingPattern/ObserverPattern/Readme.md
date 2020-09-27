# Observer Pattern
publish-subscribe 관계.   
중요한 포인트는 멀티플 리스너(Observer)가 싱글 이벤트(Publisher)에 붙을 수 있다는 점이다.   
주체에 종속된 관찰자 들에게 주체가 나 변경됨!을 자동으로 알리는 디자인 패턴    
옵저버의 목록을 객체에 등록하여 상태 변화가 있을 때마다 메소드 등을 통해 객체가 직접 목록의 각 옵저버에게 통지하도록 하는 디자인 패턴    
옵저버(리스너)를 관찰 대상이 되는 객체에 등록시킨다.

- Several Messaging Protocols
- RSS feeds
- Event-Driven Systems

![image]('https://raw.githubusercontent.com/lee-seul/lee-seul.github.com/master/static/img/_posts/observer.png')