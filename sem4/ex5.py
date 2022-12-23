
# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# 12A11B10C6D5E4FG python is s7o c7ol
# Первая функция - текст зашифровывает
# Вторая - расшифровывает
# Две промежуточные - считывают с файла и записывают в файл

import os
os.system('cls')
#----------------------

def encode(s):
	encoding = ""
	i = 0
	while i < len(s):
		count = 1
		while i + 1 < len(s) and s[i] == s[i + 1]:
			count = count + 1
			i = i + 1
		encoding += str(count) + s[i]
		i = i + 1
	return encoding

def unzip(string):
    out_string =''
    multiplier = ''
    for e in string:
        if e.isdigit():
                multiplier +=e
        else:
            out_string+=e*int(multiplier)
            multiplier = ''
    return out_string

#---------------------------------------------------------------------

path1 = 'E:\\QA\\Python\\semPython\\sem4\\DATA\\ex5_1.txt'
path2 = 'E:\\QA\\Python\\semPython\\sem4\\DATA\\ex5_2.txt'
path3 = 'E:\\QA\\Python\\semPython\\sem4\\DATA\\ex5_3.txt'

with open(path1,'w') as f:
    f.write ('AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool') 

while True:
    print('Для вывода на экран введите - 1 \nЧто бы записать в файл - 2\nДля распаковки - 3\nДля выхода - 4\n')
    menu = input('Выбранный режим: ').lower()
    print()
    
    if menu == '4':
        break
    elif not (menu == '1' or menu == '2' or menu == '3'):
        continue
    if menu == '1':
        with open(path1,'r') as file_in:
            data = file_in.read()
            print(f'>>> Результат сжатия:\n{data}\n{encode(data)}\nПОВТОРИМ?')
            print('-'*50)
    elif menu == '2':
        with open(path1,'r') as file_in:
            data = file_in.read()
        with open(path2,'w') as file_out:
            file_out.write(encode(data))
        print(f'>>> Результат сжатия записан в файлы в папке DATA\nПОВТОРИМ?')
        print('-'*50)
    else:
        try:
            file_in =  open(path2,'r')
        except:
            print ('>>> Упс, отсутствует файл в директории DATA!')
            break
        data = file_in.read()
        file_in.close()
        with open(path3,'w') as file_out:
            file_out.write(unzip(data))
        print(f'>>> Результат сжатия {data}\nзаписан в файл: ex5_3.txt в директории DATA \nПОВТОРИМ?')
        print('-'*50)