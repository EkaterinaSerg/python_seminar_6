# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_element = int(input('Введите первый элемент: '))
difference = int(input('Введите разность: '))
amount_of_elements = int(input('Введите количество элементов: '))

arithmetic_progression = []

for i in range(1, amount_of_elements + 1):
    a_p = first_element + (i - 1) * difference
    arithmetic_progression.append(a_p)
print(arithmetic_progression)