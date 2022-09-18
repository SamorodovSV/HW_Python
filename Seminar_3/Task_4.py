# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# Первый вариант решения:

a = int(input("Введите 10-ное число для преобразовывания в двоичное:\n"))
s = ''

while a > 0:
   s = str(a % 2) + s
   a = a // 2

print('Введённое число в двоичной системе =',s)

# Второй вариант решения:

a = int(input("Введите 10-ное число для преобразовывания в двоичное:\n"))
print(bin(a))