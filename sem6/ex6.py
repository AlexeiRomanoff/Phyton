
#6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]


import os
clear = lambda: os.system('cls')
clear()

import random 

lst = []

for i in range(0, 200): 
    lst.append(random.randint(1, 100))
lst_num = list(enumerate(lst, 0))

result_dict = dict()
for index_list, i_value in enumerate(lst):
    if index_list +1:
        result_dict[index_list] = i_value
result = [(i_key, i_value) for i_key, i_value in result_dict.items()]

print(result)


##Пока не понял как сравнить через сложение (( надо немного больше времени вникнуть


