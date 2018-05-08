import math
# from math import sqrt
# from math import *   (without math.)


num = -5.5
num2 = 10


def distance_from_zero(n):
    ev = type(n) == int or type(n) == float
    if ev:  # if ev == True
        return abs(n)
    else:
        return "Nope"

print(distance_from_zero(num))


def square(n):
    squared = n ** 2
    print("%.2f squared is %.2f." % (n, squared))
    return squared

square(num)


def power(base, exponent):
    result = base ** exponent
    print("%d to the power of %d is %d." % (base, exponent, result))

power(37, 4)


# function can call another function
def one_good_turn(n):
    return n + 1


def deserves_another(n):
    print(one_good_turn(n) + 2)

deserves_another(1)


# math library

everything = dir(math)
print(everything)

# square root
print(math.sqrt(25))


# built in functions
def biggest_number(*args):
    print(max(args))
    return max(args)


def smallest_number(*args):
    print(min(args))
    return min(args)


def distance_from_zero(arg):
    print(abs(arg))  # absolute value
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

print(type(100))
print(type(0.1))
print(type("ass"))
