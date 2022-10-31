import sys
import math
import random
import threading
import time
from functools import reduce

# raw strings: ignoring escape sequences: literal string output
print(r"I'll be ignored \n")

print("Hello" + "You")
str3 = "Hello You"
print("Length", len(str3))

print("first character", str3[0])
print("last character", str3[-1])

print("1st 3", str3[0:3])
print("Every other", str3[0:-1:2]) # first, last, every other

str4 = str3.replace("Hello", "Goodbye")
print(str4)

print(str3[:6] + "y" + str3[7:])

#testing if a string exists in a string
print("you" in str3)
print("you" not in str3)

print("You Index:", str3.find("You"))
print("       Hello!!!       ".strip())

print(" ".join(["Hello", "Lucas", "Derek"]))

print("Wow this is crazy".split(" "))

int1 = int2 = 5

# fstring allows you to interpolate
print(f"{int1} + {int2} = {int1 + int2}")

print("String".upper())
print("String".lower())

# Boolean if all are alphanumeric
print("String123".isalnum())
# boolean if alphabetical
print("String".isalpha())
# boolean if all are digits
print("123".isdigit())




