
# 5 - Есть список случайных чисел в промежутке от 1 до 100, количеством 200. 
# Создайте список кортежей, первый элемент которого - индекс элемента, а второй - сам элемент, при условии, что они не совпадают.
#[1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]

#---------------------------------------------------------------------------------------------------------------------------------
# Получилось только так, не все лекции пока посмотрел, видимо упустил как это сделать ((
# Не совсем то, что требовалось, но индекс и знаечение вывел. Сравнение пока не понял как сделать. Буду пересматривать лекции. 
# Немного не успеваю смотреть из-за работы.

import os
clear = lambda: os.system('cls')
clear()

import random 

lst = []

for i in range(0, 200): 
    lst.append(random.randint(1, 100))
lst_num = list(enumerate(lst, 0))
print('#'*200)
print(lst_num)
print('#'*200)

# Альтернативный вариант:
result_dict = dict()
for index_list, i_value in enumerate(lst):
    if index_list +1:
        result_dict[index_list] = i_value
result = [(i_key, i_value) for i_key, i_value in result_dict.items()]

print(f"Альтернативный вариант:\n {result}")
print('#'*150)
