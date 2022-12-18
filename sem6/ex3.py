
# 3-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

import os
clear = lambda: os.system('cls')
clear()

print('-'*100)
num = int(input("Укажите число элементов последовательности: "))
lst = []
for i in range(num):
    lst.append((-3)**i)
print(f"Вот что из этого вышло: {lst}")
print('-'*100)