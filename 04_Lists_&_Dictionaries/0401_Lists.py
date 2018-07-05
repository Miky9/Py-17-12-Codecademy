import random
zoo_animals = ["pangolin", "cassowary", "sloth", "snake"]
zoo2_animals = ["tiger", "snake", "lion", "turtle", "hippo", "antelope", "oryx calf"]
animals = zoo_animals + zoo2_animals

# def print_animals():
#
#     animals_sum = len(animals)
#     print(animals, "\n", animals_sum)


def print_(input_, input2_='items'):
    input_sum = len(input_)
    input_string = input2_ + ": "
    print(input_string, input_, "\n", input_sum)


print_(animals, 'animals')


print('\n//////////////////// Natural disaster hit our Zoos! ////////////////////\n')

animals = zoo_animals + zoo2_animals
random.shuffle(animals)
surviving_animals = animals[0:5]
dead_animals = animals[5:len(animals)]
print_(surviving_animals, 'surviving_animals')
print_(dead_animals, 'dead_animals')
animals = surviving_animals


print('\n//////////////////// Adding new animals ////////////////////\n')

animals.append("gorilla")
animals.append("gorilla")
print_(animals, 'animals')

print('\n//////////////////// Friend for the first animal ////////////////////\n')

print('Who needs friend? ... This one:', animals[0])
animals.insert(0, animals[0])
print_(animals, 'animals')

print('\n//////////////////// We put animals into new zoo randomly. Where are our gorillas? ////////////////////\n')

random.shuffle(animals)
gorilla1_index = animals.index("gorilla")
gorilla2_index = [i for i, n in enumerate(animals) if n == "gorilla"][1]
print('Gorillas are in these enclosures: ', gorilla1_index+1, gorilla2_index+1)
print_(animals, 'animals')

print('\n//////////////////// Actually, we don\'t like gorillas. Removing them... and sorting... ////////////////////\n')

animals.remove("gorilla")
animals.remove("gorilla")
animals.sort()   # alphabetical
print_(animals, 'animals')

print('\n//////////////////// Renaming new enclosures... ////////////////////\n')

start_enclosures = list(range(1, len(animals)+1))
enclosures = []

for number in start_enclosures:
    enclosures.append(str(number) + ' ' + (str(animals[number-1])).upper())

print_(start_enclosures)
print_(enclosures)


'List Methods Summary'
'''
len(list)
random.shuffle(list)
list[0:5]   = slicing
list.append("xxx")
list.insert(0, list[0])    position 0, item
list.index("xxx")   index of first occurrence
list.remove("xxx")
list.sort()    alphabetical
'''












# if len(zoo_animals) > 3:
#     print("The first animal at the zoo is the " + zoo_animals[0])
#     print("The second animal at the zoo is the " + zoo_animals[1])
#     print("The third animal at the zoo is the " + zoo_animals[2])
#     print("The fourth animal at the zoo is the " + zoo_animals[3])


# def animals_print():
#     for x in animals:
#         print(x)
#
#
