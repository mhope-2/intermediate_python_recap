import functools

def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper


@start_end_decorator
def add5(x: int):
    return x + 5

result = add5(10)
print(result)

print("*********************************************")
print()
# *******************************

def repeat(num_times):
    def decorator_repeat(func):
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")

greet("Alex")

print("*********************************************")
print()

# ***************** CLASS DECORATORS ********************
class CountCalls:
    def __init__(self, func) -> None:
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This has been executed {self.num_calls} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello")

say_hello()
say_hello()
say_hello()