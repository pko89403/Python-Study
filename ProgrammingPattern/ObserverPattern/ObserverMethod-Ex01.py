class Observer:
    def __init__(self):
        self.subscriber = []
        self.msg = ""
    
    def notify(self):
        for sub in self.subscriber:
            sub.msg = self.msg 

    def register(self, observer):
        self.subscriber.append(observer)
    
    def unregister(self, observer):
        self.subscriber.remove(observer)
    
# 옵저버로 부터 정보를 전달 받는 친구들 
class Subscriber: 
    def __init__(self):
        msg = ""
    
    def update(self):
        print(self.msg)

# 옵저버에 의해 관찰되는 객체
class Subject:
    def __init__(self):
        self.observer = []
    
    def notify_observer(self, info):
        for obs in self.observer:
            obs.msg = info 
    
    def attach(self, observer):
        self.observer.append(observer)
    
    def dettach(self, observer):
        self.observer.remove(observer)

    
if __name__ == "__main__":
    # 구독자 객체를 생성한다.
    sub1 = Subscriber()
    sub2 = Subscriber()
    sub3 = Subscriber()

    # 이 구독자들을 옵저버에 추가한다
    ob = Observer()
    ob.register(sub1)
    ob.register(sub2)
    ob.register(sub3)

    # 옵저버에 의해 관찰될 객체에 옵저버를 등록 시킨다.
    sub = Subject()
    sub.attach(ob)
    
    sub.notify_observer("Notify MSG")
    ob.notify()
    sub1.update()
    sub2.update()
    sub3.update()