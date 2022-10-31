import sys
import math
import random
import threading
import time
from functools import reduce

# Conditionals
# -----------------------------------------------------
# operators: < > <= >= != ==

age = 8

if age > 21:
    print("You can drive a tractor trailer")
elif age >= 16:
    print("You can drive a car")
else:
    print("You can't drive anything")

# logical operators: and or not

if age < 5:
    print("Stay at home")
elif (age >= 5) and (age <= 6):
    print("Go to kindergarten")
elif (age > 6) and (age <= 17):
    print("Grade", (age - 5))
else:
    print("College")

# ternary operator: condition true if condition else condition_false
canVote = True if age >= 18 else False
print(canVote)


