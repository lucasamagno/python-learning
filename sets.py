# a list that is unordered, only has unique values, and while values can change, he values themselves are immutable

s1 = set(["Lucas", 1])
s2 = {"Paul", 1}

print(len(s2))

# get all the values that are in s1 OR s2
s3 = s1 | s2
# get all values that are in s1 AND s2
s4 = s1 & s2
print(s3)
print(s4)
s3.add("Doug")
print(s3)
s3.discard("Lucas")
# reason why this works is because it is in an unordered list
print("Random", s3.pop())
s3 |= s2
print("s3 |= s2", s3)

# returns items that are only contained
print("s1 intersection s2", s1.intersection(s2))

# returns items are the unique in each set, we don't want duplicates
print("s1 symmetric_difference s2", s1.symmetric_difference(s2))

print("s1 difference s2", s1.difference(s2))
s3.clear()

s6 = frozenset(["Paul", 7])







