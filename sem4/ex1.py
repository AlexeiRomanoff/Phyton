# 1 - Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]
#-------------------------------------------------------------

import os
os.system('cls')
#----------------------
def func1(numN):
    list = []
    listItog = [list.append(i) for i in range(1, numN+1) if numN %i==0]
    return list
#----------------------
def func2(numN):
    primeList = []
    for i in range(2, numN):
        while numN % i == 0:
            numN /= i
            primeList.append(i)
    return primeList
#-----------------------------

print("-"*90)
numN = int(input("Привет, укажи целое число, для которого будем искать простые множители: "))

list1 = func1(numN)
list2 = func2(numN)

print(f'Все множители числа {numN}: {list1},\nиз них простые множители, это: {list2}')
print("-"*90)
print()