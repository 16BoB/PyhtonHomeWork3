# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91
def find_difference_maximum_minimum_fractional(arr):
    '''
    Находит разницу между максимальной и минимальной дробной частью
    '''
    array_length = len(arr)
    max_fractional = arr[0]%1
    min_fractional = arr[0]%1

    for i in range(0, array_length):
        if max_fractional < arr[i]%1:
            max_fractional = arr[i]%1
        elif min_fractional > arr[i]%1:
            min_fractional = arr[i]%1

    result = max_fractional - min_fractional
    return result

user_arr = [1.1, 1.2, 3.1, 5.17, 10.02]

print(find_difference_maximum_minimum_fractional(user_arr))