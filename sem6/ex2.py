
# 2- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint

import os
clear = lambda: os.system('cls')
clear()

print('-'*100)
print('Привет!')
num = int(input('Укажи четное количество элементов для списка: '))
list1 = []
list2 = []

for i in range(num):
    list1.append(randint(0, 9))
for i in range(len(list1)):
    while i < len(list1)/2 and num > len(list1)/2:
        num = num - 1
        a = list1[i] * list1[num]
        list2.append(a)
        i += 1

print(f'Спасибо! Я сгенерировал такие элементы списка: {list1}')
print(f'Умножил их по заданному принципу: начальный с последним и далее по порядку к середине списка.\nВот что у меня вышло: {list2}')
print('-'*100)