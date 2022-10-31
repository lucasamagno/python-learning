import sys
import math
import random
import threading
import time
from functools import reduce

l1 = [1, 3.14, "Lucas", True]
print("Length", len(l1))
print("First", l1[0])
print("Last", l1[-1])

l1[0] = 2
print(l1)
l1[2:4] = ["Bob", False]
print(l1)
# inserting an element without deleting it
l1[2:2] = [9]
print(l1)
l2 = l1 + ["Egg", 78]
# l2.remove("Bob") (removing by value)
# l2.pop(0) (removing by an index)
print(l2)

l3 = ["Steve", 78] + l2
print("l3:", l3)

#multidimensional list
l4 = [[1,2],[3,4]]
print("what is [1,1] = ", l4[1][1])

print("1 exists?", 1 in l4)
print("Min", min([1,2,3]))
print("Max", max([1,2,3]))
print("1dt 2", l1[0:2])
print("Every other", l1[0:-1:2])
print("Reverse", l1[::-1])




