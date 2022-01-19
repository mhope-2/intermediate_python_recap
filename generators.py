from re import A


def my_generator():
    yield 1
    yield 2
    yield 3

g = my_generator()

print(next(g))
print()
# ***********generate fib sequence using generators ***************#
def fibonacci(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a,b = b, a+b

fib = fibonacci(12)
for num in fib:
    print(num)