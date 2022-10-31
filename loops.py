import sys
import math
import random
import threading
import time
from functools import reduce

w1 = 0
while w1 < 5:
    print("hello world")
    w1 += 1

# only print out even values
w2 = 0
while w2 <= 20:
    if w2 % 2 == 0:
        print(w2)
    elif w2 == 9:
        break
    w2 += 1

l4 = [1, 3.14, "Lucas"]
# range is going to automatically kick out whatever values i specify
# end is a parameter for print so that developers can override the default new line that is used when using print()
for x in range(0, 10):
    print(x, ' ', end="")
print()

for x in l4:
    print(x)

for x in [2, 4, 6]:
    print(x)
