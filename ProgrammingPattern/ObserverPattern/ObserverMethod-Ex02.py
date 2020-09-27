from abc import ABCMeta, abstractmethod

class Subject:
    __metaclass__=ABCMeta

    @abstractmethod
    def register_observer(self):
        pass 

    @abstractmethod
    def remove_observer(self):
        pass 

    @abstractmethod
    def notify_observer(self):
        pass 

class Observer:
    @abstractmethod
    def update(self):
        pass 

    @abstractmethod
    def register_observer(self, subject):
        pass 

class seokwoo(Subject):
    def __init__(self):
        super(seokwoo, self).__init__()
        self._observer_list = []
        self.happiness = 0
        self.sadness = 0
    
    def register_observer(self, observer):
        if observer in self._observer_list:
            return "Already exist observer!"
        
        self._observer_list.append(observer)
        return "Success register!"
    
    def remove_observer(self, observer):
        if observer in self._observer_list:
            self._observer_list.remove(observer) 
            return "Sucess remove!"
        return "Observer does not exist."
    
    def notify_observer(self): 
        for observer in self._observer_list:
            observer.update(self.happiness, self.sadness)

    def emotionChanged(self):
        self.notify_observer()

    def set_emotional(self, happiness, sadness):
        self.happiness = happiness
        self.sadness = sadness
        self.emotionChanged()

class Emotion(Observer):
    def update(self, happiness, sadness):
        self.happiness = happiness
        self.sadness = sadness
        self.display()
    
    def register_subject(self, subject):
        self.subject = subject 
        self.subject.register_observer(self)
    
    def display(self):
        print('seokwoo emotion happiness : ', self.happiness, '\t sadness : ', self.sadness)
    

def test():
    seokwooObj = seokwoo()
    emotionObj = Emotion()
    emotionObj.register_subject(seokwooObj)

    seokwooObj.set_emotional('good', 'good')
    seokwooObj.set_emotional('Not good', 'Not good')
    seokwooObj.set_emotional('Bad', 'Bad')

if __name__ == "__main__":
    test()