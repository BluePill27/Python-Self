'''
Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия,
который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', 
то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, 
кодирует её предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод.
Кодирование должно учитывать регистр символов.

Sample Input 1:

aaaabbcaa
Sample Output 1:

a4b2c1a2
Sample Input 2:

abc
Sample Output 2:

a1b1c1
'''

# put your python code here
lane = input()
old_letter = lane[0]
count = 1
lane+='0'
new_lane = ''
for letter in lane[1:len(lane)]:
    if letter == old_letter:
        count+=1
        
    else:
        new_lane+=old_letter
        new_lane+=str(count)
        old_letter = letter
        count = 1
    if letter == lane[len(lane)-1]:
            new_lane+=old_letter
            new_lane+=str(count)
print(new_lane[:len(new_lane)-2])
            
