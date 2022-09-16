# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import math

def multiply_numbers_in_pairs(arr):
    '''
    Умножает елементы списка по парно (первый элемент с последним), в списках с нечетным количеством элементов, последний умножается сам на себя
    '''
    array_length = len(arr)

    number_of_iterations = array_length
    if array_length == 2:
        number_of_iterations = array_length - 1
    elif array_length > 2:
        number_of_iterations = math.ceil(array_length / 2)

    if array_length%2 != 0:
        index_last_element = int(array_length / 2)
        number_of_iterations = array_length - index_last_element

    last_index_count = array_length
    result_array = []

    for i in range(0, number_of_iterations):
        last_index_count = last_index_count - 1
        if array_length%2 != 0:
            if i == index_last_element:
                result_array.append(arr[i] * arr[i])
            else:
                result_array.append(arr[i] * arr[last_index_count])
        else:
            result_array.append(arr[i] * arr[last_index_count])
    return result_array
 
user_array = [2, 3, 4, 6]

print(multiply_numbers_in_pairs(user_array))