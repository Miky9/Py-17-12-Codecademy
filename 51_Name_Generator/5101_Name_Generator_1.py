import string
import random
# print(help(string))
# https://docs.python.org/2/library/string.html

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)

print(random.choice("pull a letter from here"))
print(random.choice(string.ascii_lowercase))


def gen_length():
    result = random.randint(3,8)
    return result


def gen_vcl():
    result = random.choice('vcl')
    return result


def gen_letter_basic():
    result = random.choice(string.ascii_lowercase)
    return result


###

name_length = gen_length()
name = ''

for x in range(name_length):
    letter = gen_letter_basic()
    name = name + letter



# letter_input1 = gen_vcl()
# letter_input2 = gen_vcl()
# letter_input3 = gen_vcl()
# letter_input4 = gen_vcl()
# letter_input5 = gen_vcl()




vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
letter = string.ascii_lowercase




print(name)