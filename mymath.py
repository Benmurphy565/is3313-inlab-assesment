def add_three(a, b, c):
    return a + b + c

def subtract_three(a, b, c):
    return a - b - c

def multiply_three(a, b, c):
    return a * b * c

def divide_three(a, b, c):
    # Assuming you want to divide a by b, then by c
    if b == 0 or c == 0:
        return "Cannot divide by zero"
    return a / b / c

def square(a):
    return a ** 2

def cube(a):
    return a ** 3
