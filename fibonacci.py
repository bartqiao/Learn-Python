__author__ = 'Bart Qiao'

# The is a simple script to calculate fibonacci number.

def fibonacci(n):
    fib = []
    a, b = 0, 1
    if n == 0 or n == 1:
        fib.append(1)
    else:
        #while b < n:
        #    a, b = b, a + b
        #    fib.append(b)"""
        for i in range(n):
            a, b = b, a + b
            fib.append(b)
        print(fib)




fibonacci(6)