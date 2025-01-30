# File: fibrecu.py
# recursively prints a number of fibonacci numbers

def fib(n):
    if n <= 2 and n > 0:
        return 1
    else:
        return fib(n-2) + fib(n-1)

print(fib(0))

