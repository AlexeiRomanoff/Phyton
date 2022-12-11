
# 2-Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021(или сколько вы скажете) конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28(или сколько вы зададите в начале) конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сделайте эту игру.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# Если делаете a и b - не нужно создавать отдельных файлов с полностью копированным кодом, лучше выделите в отдельные функции бота и умного бота.


# a) вариант - играем против бота-------------------------------------------------------------------

from random import randint

def input_dat(name):
    x = int(input(f"{name}, какое количество конфет Вы хотите взять? (от 1 до 28): "))
    print()
    while x < 1 or x > 28:
        x = int(input(f"{name}, Пожалуйста, укажите не менее одной конфеты и не более 28-ми: "))
    return x


def p_print(name, k, counter, value):
    print(f"{name} сделал ход и взял себе {k} конфет, теперь у него {counter} конфет. На столе осталось {value} конфет.")
    
player1 = input("Вы - первый игрок. Как Вас зовут?: ")
player2 = "Бот Компьюша"
value = int(input("Введите количество конфет на столе: "))
print()
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")
    

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = randint(1,29)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл игрок по имени {player1}")
else:
    print(f"Выиграл {player2}")    
