from abc import ABCMeta, abstractmethod

class Job(metaclass=ABCMeta):
    @abstractmethod
    def do_something(self):
        pass 

class Student(Job):
    def do_something(self):
        print("Let's do the study")

class Worker(Job):
    def do_something(self):
        print("Let's do the work")

class SimpleFactory(object):
    def do_it(self, object_type):
        return (eval(object_type.capitalize())().do_something())

if __name__ == "__main__":
    job = input("What is your job? Student? Worker?")
    f = SimpleFactory() 
    f.do_it(job)