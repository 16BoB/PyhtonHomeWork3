# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
def sum_odd_positions(arr):
    '''
    Суммирует элементы массива на нечетных позициях
    '''
    array_length = len(arr)
    sum_nubers = 0
    for i in range(0, array_length):
        if i % 2 != 0 :
            sum_nubers = sum_nubers + arr[i]
    return sum_nubers

user_arr = [2, 8, 5, 22, 3, 9 , 10]

print(sum_odd_positions(user_arr))