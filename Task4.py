# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

num = []
def convert(number):
    '''
    Заполняет список переводя число в двоичную систему, после нужно развернуть список
    '''
    if (number == 0):
        return num
    dig = number % 2
    num.append(dig)
    convert(number // 2)

user_number = int(input("Введите число: "))

convert(user_number)
num.reverse()

print("Двоичная форма числа:")

print(num)