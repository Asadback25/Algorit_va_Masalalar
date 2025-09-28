# Fibonacci

def fibonacci(n):
    i = 1
    fib = 1
    while i <= n:
        fib = fib * i
        i = i + 1
    return fib

print(fibonacci(10))