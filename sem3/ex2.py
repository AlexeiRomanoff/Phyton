
# 2-Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import os
clear = lambda: os.system('cls')
clear()

from random import randint

print('-'*60)
genNum = int(input('Сколько элементов будет в Вашем списке: '))
list1 = []
list2 = []

for i in range(genNum):
    list1.append(randint(0, 9))

print(f'Возьмем список чисел: {list1}')

for i in range(len(list1)):
    while i < len(list1)/2 and genNum > len(list1)/2:
        genNum -=1
        a = list1[i] * list1[genNum]
        list2.append(a)
        i += 1

print(f'Вот что у нас получилось: {list2}')
print('-'*60)