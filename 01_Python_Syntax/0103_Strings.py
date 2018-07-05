# Escaping characters
string = 'There\'s a snake in my boot!'
print(string)

# Access by Index
"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter = "MONTY"[4]
print(fifth_letter)  # Y

# String methods
parrot = "Norwegian Blue"
print(parrot.lower())  # Methods that use dot notation only work with strings.
print(parrot.upper())
print(len(parrot))

# Explicit String Conversion, String Concatenation
pi = 3.14
print(str(pi) + " " + parrot)

# User Input, String Formatting with %
"""raw_input() was renamed to input()"""

name = input("What is your name? ")
age = int(input("What is your age? "))
color = input("What is your favorite color? ")

print("Ah, so your name is %s, your age is %d, "
      "and your favorite color is %s." % (name, age, color))

# %s  string placeholder
# %d  int placeholder
# %f float placeholder
