"Implicit Data Type Conversion (coercion)"""
# without you having to tell the compiler

a_int = 1
b_float = 1.0
c_sum = a_int + b_float
print(c_sum)
print(type(c_sum))

"Explicit Data Type Conversion (type casting)"""
# (required_data_type)(expression)
# you clearly defined it in your program

age = 13
print("I am " + str(age) + " years old!")

number1 = "100"
number2 = "10"
string_addition = number1 + number2  # 10010
int_addition = int(number1) + int(number2)  # 110

string_num = "7.5"
print(int(string_num))  # 7
print(float(string_num))  # 7.5


# Note:If you use int() on a floating point number, it will round the number down.

# Note: as you can imagine, with explicit data type conversion, there is a risk of information loss
# since you're forcing an expression to be of a specific type.

# Tip: you can use the type() function in Python to check the data type of an object.
