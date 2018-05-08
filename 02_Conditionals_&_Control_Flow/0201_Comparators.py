bool_one = 3 < 5
bool_two = 7 >= 10
bool_four = 45 >= 45 and 1 == 2 or not(5 > 5)

print(bool_one)
print(bool_two)
print(bool_four)


"""
Equal to (==)
Not equal to (!=)
Less than (<)
Less than or equal to (<=)
Greater than (>)
Greater than or equal to (>=) 

Boolean operators compare statements and result in boolean values. There are three boolean operators:

and, which checks if both the statements are True;
or, which checks if at least one of the statements is True;
not, which gives the opposite of the statement.

Boolean operators aren't just evaluated from left to right. Just like with arithmetic operators, 
there's an order of operations for boolean operators:

not is evaluated first;
and is evaluated next;
or is evaluated last.
For example, True or not False and False returns True
"""

"""
Boolean Operators
------------------------      
True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True

"""