import functools
import time 

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'{func.__name__} took {round((time.time() - start), 4)} seconds')
        return result 
    return wrapper 

# timer 데코레이터 적용
@timer 
def huge_add(a, b):
    result = a + b 
    time.sleep(1)
    return result 

@timer
def huge_multiply(a, b):
    result = a * b 
    time.sleep(1)
    return result 

if __name__ == "__main__":
    huge_number = 10e8 
    huge_add(huge_number, huge_number)
    huge_multiply(huge_number, huge_number)

    