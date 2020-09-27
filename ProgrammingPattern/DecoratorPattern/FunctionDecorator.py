def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Result : {result}")
        return result 
    return wrapper

@logger
def add(a, b):
    return a + b 

if __name__ == "__main__":
    result = add(20, 22)
    print(result)