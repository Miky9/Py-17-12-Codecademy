# d = {'key1': 1, 'key2': 2, 'key3': 3}
# print(d['key1'])

'creating, adding'''

menu = {}  # Empty dictionary
menu['Chicken Alfredo'] = 14.50  # Adding new key-value pair
menu['Fish & Chips'] = 35.50
menu['Cheese Pizza'] = 28.50
menu['Pitta'] = 5.00
print(menu, '\nnumber of items: ', len(menu))

# remove key pair
del menu['Chicken Alfredo']
print(menu, '\nnumber of items: ', len(menu))

menu['Chicken Alfredo'] = 14.50
menu['Chicken Alfredo'] = 20.50
print(menu, '\nnumber of items: ', len(menu))

# delete the dictionary itself
del squares