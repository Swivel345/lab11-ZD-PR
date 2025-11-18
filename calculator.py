"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def add(a, b): 
    return a+b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        if a == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return b/a # raise ZeroDivisionError if a == 0
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return 0

def log(a, b):
    try:
        if a <= 0:
            raise ValueError("Argument of log must be greater than 0")
        if b <=0 or b == 1:
            raise ValueError("Base of log must be greater than 1")

        return math.log(a, b)
    except ValueError as e:
        print(f"Error: {e}")


def exp(a, b):
    return a**b


