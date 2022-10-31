print(list(range(0, 5)))

# in a list or in this scenario, a range, first value passed in is start, second value passed in is end, 3rd is a step
print(list(range(0, 15, 3)))

l6 = [[1, 2, 3], [100, 200, 300], [1000, 2000, 3000]]

for x in range(0, 3):
    for y in range(0,3):
        print(l6[x][y])
