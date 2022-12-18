
# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

import os
clear = lambda: os.system('cls')
clear()

print('-'*75)
z = int(input('Введите размер числа Фибоначчи: '))

if z < 0: z*=-1
x=y=1

list1 = [x, y]

for i in range(2, z):
    x,y = y, x + y
    list1.append(y)

print(f'У нас есть такой список: {list1}')
x=y=1

for i in range(-z, 1):
    x,y = y, x - y
    list1.insert(0, y)

print(f'Решение: {list1}')
print('-'*75)
