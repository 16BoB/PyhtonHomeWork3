# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
def fibonachi(n):
    if n in [1, 2]:
        return 1
    else:
        return fibonachi(n-1) + fibonachi(n-2)

def get_fibonachi_list(num):
    result_list = []
    for i in range(1, num + 1):
        result_list.append(fibonachi(i))
    return result_list

def get_negafibonachi(list):
    result = []
    for item in range(len(list)):
        if ((len(list) - item) % 2 == 0):
            result.append(list[len(list) - item - 1] * -1)
        else:
            result.append(list[len(list) - item - 1])
    result.append(0)
    for item in range(len(list)):
        result.append(list[item])
    return result


num = int(input("Введите целое число: "))

print(f'Для k = 8 список Негафибоначчи =>  {get_negafibonachi(get_fibonachi_list(num))}')

