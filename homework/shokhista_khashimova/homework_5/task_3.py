# Даны такие списки:
# students = ['Ivanov', 'Petrov', 'Sidorov']
# subjects = ['math', 'biology', 'geography']
# Распечатайте текст, который будет использовать данные из этих списков. Текст в итоге должен выглядеть так:
# Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geography

students = ['Ivanov', 'Petrov', 'Sidorov']
students = ', '.join(students)
subjects = ['math', 'biology', 'geography']
subjects = ', '.join(subjects)
print(students)
my_text = f'Students {students} study these subjects: {subjects}'
print(my_text)
