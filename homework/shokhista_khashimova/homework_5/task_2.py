# Допустим, какая-то программа возвращает результат своей работы в таком виде:
# результат операции: 42
# результат операции: 514
# результат работы программы: 9
# С помощью срезов и метода index получите из каждой строки с результатом число,
# прибавьте к полученному числу 10, результат сложения распечатайте.

result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'
# Допустим, что число начинается с позиции 20 в строке, тогда это число из строки достанешь так:
number1 = result_1[20:]
number2 = result_2[20:]
number3 = result_3[20:]
# Так ты срезаешь из этой строки всё, начиная с 20-го символа.
# Мы знаем, что число идет всегда после двоеточия.
# Т.е. определив индекс двоеточия, мы можем вырезать из этой строки всё, начиная с двоеточия:
index_1 = result_1.index(':')
index_2 = result_2.index(':')
index_3 = result_3.index(':')

number1 = result_1[index_1:]
number2 = result_2[index_2:]
number3 = result_3[index_3:]

# С помощью круглых скобок мы передаем какие-то параметры функциям и методам (с ними мы познакомимся позже).
# С помощью квадратных скобок мы обращаемся к элементам строки, списка, кортежа или словаря.

# Но дветочие нам не надо, надо только то, что идет после него.
# То есть нам надо начать не с двоеточия, а после него. Индекс после двоеточия это index_1 + 1
# В итоге, число мы можем получить так
number1 = int(result_1[index_1 + 1:])
number2 = int(result_2[index_2 + 1:])
number3 = int(result_3[index_3 + 1:])

print(number1 + 10)
print(number2 + 10)
print(number3 + 10)
