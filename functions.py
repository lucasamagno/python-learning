# basic function summing 2 numbers
def get_sum(num1: int, num2):
    return num1 + num2


print(get_sum(2, 4))


# basic function summing an unknown amount of numbers
def get_sum2(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


print(get_sum2(2, 5, 6, 7))


# returning 2 numbers
def next_2(num):
    return num + 1, num + 2


i1, i2 = next_2(2)

print(i1, i2)


# lambda is an anonymous function
def mult_by(num):
    return lambda x: x * num


# 4 is num, 5 is x being passed into the lambda function
print(mult_by(4)(5))

# function that allows you to pass in a function into a function
def mult_list(list, func):
    for x in list:
        print(func(x))

print()
print("Multiply list")
mult_by_4 = mult_by(4)
mult_list(list(range(0, 5)), mult_by_4)


# list of functions
power_list = [lambda x: x**2,
              lambda x: x**3]

print(power_list[1](9))
