'''
Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где 
mod — это взятие остатка от деления, 
pow — возведение в степень, 
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

Обратите внимание, что на вход программе приходят вещественные числа.

Sample Input 1:

5.0
0.0
mod
Sample Output 1:

Деление на 0!
Sample Input 2:

-12.0
-8.0
*
Sample Output 2:

96.0
Sample Input 3:

5.0
10.0
/
Sample Output 3:

0.5
'''
# put your python code here
import operator
a = float(input())
b = float(input())
c = input()
operDict = {"+":operator.add, "-":operator.sub, "/":operator.truediv,"*":operator.mul,"mod":operator.mod,"pow":operator.pow,"div":operator.floordiv}
if (b == 0 and (c =="/" or c =="mod" or c =="div")):
    print("Деление на 0!")
else:
    print(operDict[c](a,b))
