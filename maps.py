from functools import reduce

one_to_4 = range(1, 5)
times2 = lambda x: x * 2
print(list(map(times2, one_to_4)))

# filter
print(list(filter((lambda x: x % 2 == 0), range(1, 11))))


# reduce
print(reduce((lambda x, y: x+y), range(1,6)))
