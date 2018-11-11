''' Учитель физики, Алексей Григорьевич, в наказание за невыполненную домашку, задал Васе на выходные спец задачу,
условие которой зашифровал в файле input.txt.
В качестве подсказки для расшифровки текста и решение самой задачи Алексей Григорьевич оставил зеркало.
Помогите бедному школьнику хотя бы прочесть условие задачи, ведь у него дедлайн до понедельника. '''

file = input('Введите имя файла: ')
try:
    input_file = open(file)
except FileNotFoundError:
    print('Файл {} не найден'.format(file))
    exit()
with open('input.txt') as f_in:
    with open('output.txt', 'w') as f_out:
        for line in f_in:
            new_str = ''
            line = line.strip()
            for char in line:
                new_str = char + new_str
            print(new_str, file = f_out)
            print(new_str)