# Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def sum_of_numbers(List): 
    Summa=0 
    for i in range(len(List)): 
        if i %2!=0: 
            Summa=Summa+List[i] 
    return Summa

n = [2, 3, 5, 9, 3]
sum_of_numbers(n)
print(n, '->' , sum_of_numbers(n))