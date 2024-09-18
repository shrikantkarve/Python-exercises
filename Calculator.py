# Suggested code may be subject to a license. Learn more: ~LicenseLog:2079782331.
import math

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Division by zero error"
        return x / y

    def square(self, x):
        return x * x

    def square_root(self, x):
        if x < 0:
            return "Cannot calculate square root of a negative number"
        return math.sqrt(x)

    def exponential(self, x, y):
        return x ** y

    def log(self, x):
        if x <= 0:
            return "Cannot calculate log of a non-positive number"
        return math.log(x)

mycalc = Calculator()
print(mycalc.add(2,3))