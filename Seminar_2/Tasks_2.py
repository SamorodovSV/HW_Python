# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11



# N = input()
# sum = 0

# for result in N:
#     if result.isdigit():
#         sum += int(result)

# print('Сумма', sum)


# ------------------------------------------------------------------


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input("Введите число: "))
# a = []
# res = 1
# for i in range(1, n+1):
#     res *= i
#     print(res, end =' ')