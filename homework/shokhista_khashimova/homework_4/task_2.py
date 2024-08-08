my_dict = {'tuple': (1, "q", "A", "z", "word"), 'list': ["first", "second", "third", "cat", "dog"],
            'dict': {'car1': 'volvo', 'car2': 'bmw'}, 'set': {"white", "black", "yellow", 2, 6.8}}


print(my_dict['tuple'][-1])

my_dict['list'].append('new')
my_dict['list'].pop(1)

my_dict['dict']['i am a tuple'] = False
my_dict['dict'].pop('car1')

my_dict['set'].add("Yes")
my_dict['set'].pop()

print(my_dict)
