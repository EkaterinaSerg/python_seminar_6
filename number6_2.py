# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# индексы: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 7 10
# Вывод: [1, 9, 13, 14, 19]


# Вариант 1
"""
list1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_num = 7
max_num = 10
new_list = []
for i in range(len(list1)):
    if list1[i] >= min_num and list1[i] <= max_num:
        new_list.append(i)
print(new_list)
"""

# Вариант 2
"""
list1 = [int(input('введите элементы: ')) for i in range(int(input('введите количество элементов: ')))]
min_num = int(input('введите минимальное число: '))
max_num = int(input('введите максимальное число: '))
new_list = []
for i in range(len(list1)):
    if list1[i] >= min_num and list1[i] <= max_num:
        new_list.append(i)
print(new_list)
"""

# Вариант 3
import random

list1 = [random.randint(-4, 12) for i in range(int(input('введите количество элементов: ')))]
print(list1)
min_num = int(input('введите минимальное число: '))
max_num = int(input('введите максимальное число: '))
new_list = []
for i in range(len(list1)):
    if list1[i] >= min_num and list1[i] <= max_num:
        new_list.append(i)
print(new_list)