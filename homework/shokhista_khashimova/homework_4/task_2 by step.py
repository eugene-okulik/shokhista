# Создайте словарь (и сохраните его в переменную my_dict) с такими ключами:
# ‘tuple’, ‘list’, ‘dict’, ‘set’.
# Для каждого элемента задайте значение соответствующее названию ключа.
# Например в элемент с ключом ‘tuple’ добавьте кортеж в качестве значения.
# Содержимое этого кортежа (или что вы там добавляете) - на вашу фантазию,
# но количество элементов в каждом таком значении должно быть не меньше пяти.
# Т.е. если добавляете кортеж, то в нем как минимум должно быть (1, 2, 3, 4, 5),
# если список, то не меньше пяти элементов, если словарь,
# то не меньше пяти пар ключ-значение, итд.


my_dict = {'tuple': (1, "q", "A", "z", "word"), 'list': ["first", "second", "third", "cat", "dog"],
'dict': {'car1': 'volvo', 'car2': 'bmw'}, 'set': {"white", "black", "yellow", 2, 6.8}}

# Для того, что хранится под ключом ‘tuple’ выведите на экран последний элемент
print(my_dict['tuple'][-1])


# Для того, что хранится под ключом ‘list’:
# добавьте в конец списка еще один элемент
my_dict['list'].append('new')

# удалите второй элемент списка
my_dict['list'].pop(1)


# Для того, что хранится под ключом ‘dict’:
# добавьте элемент с ключом ('i am a tuple',) и любым значением
my_dict['dict']['i am a tuple'] = False

# удалите какой-нибудь элемент
my_dict['dict'].pop('car1')


# Для того, что хранится под ключом ‘set’:
# добавьте новый элемент в множество
my_dict['set'].add("Yes")

# удалите элемент из множества
my_dict['set'].pop()


# В конце выведите на экран весь словарь
print(my_dict)
