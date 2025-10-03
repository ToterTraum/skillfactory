import random

students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
classes = ['Математика', 'Русский язык', 'Информатика']
students.sort()
students_marks = {}
for student in students:
    students_marks[student] = {}

    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks[student][class_] = marks

for student in students:
    print(f'''{student}
    {students_marks[student]}''')


print('''
      Список команд:
1. Удалить/Редактировать данные по оценкам предмета ученика.
2. Вывести информацию по  оценкам ученика.
3. Вывод среднего балла ученика.
4. Выход из программы.
''')

while True:
    command = int(input('Ведите команду: '))
    if command == 1:
        print('1. Удалить/редактировать оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Удалить оценку.'))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].pop(mark)
            print(f'Для {student} по предмету {class_} удалена оценка.')
    elif command == 2:
            print('2. Вывести все оценки определенного ученика.')
            student = input('Введите имя ученика: ')
            if student in students:
                print(f'\nОценки ученика {student}:')
                for class_ in classes:
                    print(f'\t{class_} - {students_marks[student][class_]}')
                print()
            else:
                print('Ученик не найден!')

    elif command == 3:
        print('3. Вывести средний балл по конкретному ученику')
        student = input('Введите имя ученика: ')
        if student in students:
            print(f'\nСредний балл ученика {student}:')
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum//marks_count}')
            print()
    elif command == 4:
        print('4. Выход из программы')
        break