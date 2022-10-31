import sys
import math
import random
import threading
import time
from functools import reduce

# the above imports are called modules!!!

'''
print("Hello World!")
name = input("What is your name?")
print("Hi", name)
'''

v1 = (
        1 + 2 + 3
)
print(v1)

# Valid Syntax, not written like this ever
v2 = 1 + 2 \
     + 3
print(v2)
# ------------------------------------------------------------------------
# data types
# integers, floats, complex numbers, strings, booleans

print("sys.maxsize:", sys.maxsize)

f1 = 1.111111111111111111
f2 = 1.111111111111111111
f3 = f1 + f2

print(f3)

# real part + imaginary part

cn1 = 5 + 6j
print(cn1)

b1 = True
b2 = False

str1 = "Escape Sequences \' \" \t \\ \n"

# with triple quotes, I can enter in ' " without any errors in string
str2 = '''Triple Quoted ' " '''

# type casting
print("Cast", type(int(5.4)))
print("Cast", type(str(5.4)))

# chr returns as a str still
print("Cast", type(chr(9)))
# turns character into an integer
print("Cast", type(ord('a')))

# ------------------------------------------------------------------------
# Output
print(12, 11, 1998, sep='/')
print("No Newline", end='')
print("\n%04d %s %.2f %c" % (1, "Lucas", 1.234, 'A'))

# ------------------------------------------------------------------------
# Math
# Math module
print("5 + 2 =", 5 + 2)
print("5 - 2 =", 5 - 2)
print("5 * 2 =", 5 * 2)
print("5 / 2 =", 5 / 2)
print("5 % 2 =", 5 % 2)
print("5 ** 2 =", 5 ** 2)
print("5 // 2 =", 5 // 2)
print("abs(-2) ", abs(-2))
print("max(5,2) ", max(5, 2))
print("min(5,2) ", min(5, 2))
print("pow(2, 3) ", pow(2, 3))
print("ceil(4.3) ", math.ceil(4.3))  # round up, regardless of rounding rules
print("floor(4.8) ", math.floor(4.8))  # round down, regardless of rounding rules
print("round(4.5) ", round(4.5))  # actually round
print("exp(1) ", math.exp(1))  # e**x
print("log(e) ", math.log(math.exp(1)))  # default is base e
print("log(100) ", math.log(100, 10))  # base 10
print("sqrt(100) ", math.sqrt(100))
print("sin(0) ", math.sin(0))
print("cos(0) ", math.cos(0))
print("tan(0) ", math.tan(0))
print("asin(0) ", math.asin(0))
print("acos(0) ", math.acos(0))
print("atan(0) ", math.atan(0))
print("sinh(0) ", math.sinh(0))
print("cosh(0) ", math.cosh(0))
print("tanh(0) ", math.tanh(0))
print("asinh(0) ", math.asinh(0))
print("acosh(pi) ", math.acosh(math.pi))
print("atanh(0) ", math.atanh(0))
print("hypot(0)", math.hypot(10, 10))  # sqrt(x*x + y*y)
print("radians(0)", math.radians(0))
print("degress(pi)", math.degrees(math.pi))

# random module
print("Random", random.randint(1, 101))

# infinity
print(math.inf > 0)

# NaN = not a number
print("math.inf - math.inf = ", math.inf - math.inf)
