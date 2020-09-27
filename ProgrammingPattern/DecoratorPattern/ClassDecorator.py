class Logger(object):
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        print(f"Result : {result}")
        return result 

@Logger
def add(a, b):
    return a + b 

if __name__ == "__main__":
    result = add(20, 22)
    print(result)