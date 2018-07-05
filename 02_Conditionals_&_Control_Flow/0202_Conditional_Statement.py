answer2 = "Left"
if answer2 == "Left":
    print("This is %s" % answer2)
else:
    print("This is %s" % "Right")
print()


def greater_less_equal_5(number):
    if number > 5:
        return 1
    elif number < 5:
        return -1
    else:
        return 0


print(greater_less_equal_5(4))
print(greater_less_equal_5(5))
print(greater_less_equal_5(6))
