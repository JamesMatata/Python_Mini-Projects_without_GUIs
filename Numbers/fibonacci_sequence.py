"""
Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
"""

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


num = int(input("Enter the number of Fibonacci numbers you want to generate: "))

for fib in range(num):
    print(fibonacci(fib))
