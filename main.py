# Return Hello World!
import commit
from pip._internal.vcs import git


def hello():
    return "Hello"


# Return Hello World! with a newline char
def helloline():
    return "Hello"


# Return the sum of two numbers
def addTwoNumbers(a, b):
    return a


# Return the difference of two numbers
def subtractTwoNumbers(a, b):
    return a


# Return the quotient of a dividend and divisor
def divideTwoNumbers(a, b, c=None):
    return c


# Return the power of a base raised to an exponent
def exponent(a, b):
    return a


# check output
print(hello())
print(helloline())
print(addTwoNumbers(1, 2))
print(subtractTwoNumbers(1, 2))
print(divideTwoNumbers(10, 3))
print(exponent(2, 3))
