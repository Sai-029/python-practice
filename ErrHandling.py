def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: cannot divide by zero"
    except TypeError:
        return "Error: inputs must be numbers"

print(divide(10, 2))
print(divide(10, 0))
print(divide(10, "x"))