logger = lambda fn: lambda *args, **kwargs: print(f"Result : {fn(*args, **kwargs)}")

@logger
def add(a, b):
    return a + b 

if __name__ == "__main__":
    result = add(20, 22)
    print(result)