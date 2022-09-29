
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# Было

# n = int(input("Введите число: "))
# a = []
# res = 1
# for i in range(1, n+1):
#     res *= i
#     print(res, end =' ')

# Стало:

# from math import factorial


# def number_factorial(numb):
#     if numb == 1:
#         return 1
#     else:
#         return numb * factorial(numb - 1)

# print(list(map(number_factorial, [i for i in range(1, int(input('Введите число: ')) + 1)])))


# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Было:

# def sum_of_numbers(List): 
#     Summa=0 
#     for i in range(len(List)): 
#         if i %2!=0: 
#             Summa=Summa+List[i] 
#     return Summa

# n = [2, 3, 5, 9, 3]
# sum_of_numbers(n)
# print(n, '->' , sum_of_numbers(n))

# Стало:

# print(sum(list(map(int, input('Введите числа через пробел: ').split()))[1::2]))


#  Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# Было:

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")

# Стало:
# lst = list(map(int, input("Введите числа через пробел: ").split()))
# print(list(filter(lambda x: lst.count(x) == 1, lst)))

# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# Было:

# my_text = 'Привет, меня абв зовут зовабвут Сергей! абв Мнеабв Мне 43абв 34 абв года.'

# def del_some_words(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     return " ".join(my_text)

# my_text = del_some_words(my_text)
# print(my_text)

# Стало:

# words = list(map(str, input('Введите слова(текст) через пробел: ').split()))
# del_word = input('Введите слово или символы, которые нужно убрать из текста: ')
# print(*list(filter(lambda x: x != del_word, words)))