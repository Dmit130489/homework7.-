my_dict = {'Tom': 12082016, 'Ten': 28011976, 'Karl': 1140987, 'Katy': 270238}
print(my_dict)
print(my_dict['Ten'])
my_dict['Mark'] = 250365
print(my_dict)
my_dict.update({'Lucy': 120263, 'Lui': 180964})
print(my_dict)
print(my_dict.get('Farhad'))
slaboeZveno = my_dict.pop('Karl')
print(slaboeZveno)
print(my_dict)

my_set = {8, 4, 3, 3, 5, 7, 9, 8, 0, 5}
print(my_set)
my_set.add('Первый пошел')
my_set.add('второй пошел')
my_set.discard(7)
print(my_set)
